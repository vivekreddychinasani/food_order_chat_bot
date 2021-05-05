from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import smtplib
from city_check import check_location
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class ActionSearchRestaurants(Action):

	def filter_result(self,budget, restaurants_list_final):
		restaurants_filtered = []

		if budget == '299':			
			for restaurant in restaurants_list_final :

				if int(restaurant[2]) < 300:
					restaurants_filtered.append(restaurant)
		elif budget == '700':
			for restaurant in restaurants_list_final :		
				if int(restaurant[2]) >= 300 and int(restaurant[2]) < 700:
					restaurants_filtered.append(restaurant)	
		else :
			for restaurant in restaurants_list_final :

				if int(restaurant[2]) > 700:
					restaurants_filtered.append(restaurant)	
		return 	restaurants_filtered
		
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"5e0769e4bb8fc52ee03aa5be599e1b69"}
		try :
			zomato = zomatopy.initialize_app(config)
			loc = tracker.get_slot('location')		
			cuisine = tracker.get_slot('cuisine')
			budget = tracker.get_slot('budget')
			location_detail=zomato.get_location(loc, 1)
		
			d1 = json.loads(location_detail)
			lat=d1["location_suggestions"][0]["latitude"]
			lon=d1["location_suggestions"][0]["longitude"]
			cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
			
			results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 100)
		except:
			print('some error occured')
		d = json.loads(results)
		response="------------------------  TOP 5 RESTAURANTS FOUND ------------------ \n"
		restaurants_list_final = []
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				restaurant_single=[]

				restaurant_single.append(restaurant['restaurant']['name'])
				restaurant_single.append([restaurant['restaurant']['location']['address']])
				restaurant_single.append(restaurant['restaurant']['average_cost_for_two'])
				restaurant_single.append(float(restaurant['restaurant']['user_rating']['aggregate_rating']))

				restaurants_list_final.append(restaurant_single)				
				
		restaurants_list_filtered = self.filter_result(budget,restaurants_list_final)

		if len(restaurants_list_filtered) == 0 :
			response = " Restaurants are not found in this budget range ,Please try again with different Budget."
		restaurants_list_sorted = sorted(restaurants_list_filtered , key = lambda x : x[3] ,reverse=True)
		for restaurant_final in restaurants_list_sorted[0:5]:
			str1 = ","
			str2 = str1.join(restaurant_final[1])
			response=response+ "Found "+ restaurant_final[0]+ " in "+ str2 + " costs  " + str(restaurant_final[2])+ " for 2 and has a rating " + str(restaurant_final[3]) +"\n"

		dispatcher.utter_message(response)
		return [SlotSet('restaurants',restaurants_list_sorted[0:10])]
		
class ActionSendEmail(Action):	

	def name(self):
		return 'action_send_email'
		
	def run(self,dispatcher,tracker,domain):
		mail_content = tracker.get_slot('restaurants')

		#The mail addresses and password
		sender_address = 'upgradbot1@gmail.com'
		sender_pass = 'upgrad2110'
		receiver_address = tracker.get_slot('mailid')
		#Setup the MIME
		message = MIMEMultipart()
		message['From'] = sender_address
		message['To'] = receiver_address
		message['Subject'] = 'An Automated mail sent from Foodie Bot with the Restaurant Details'   #The subject line

		response = "Top 10 Restaurants in the town:  \n \n"
		for restaurant_final in mail_content:
			str1 = ""
			str2 = str1.join(restaurant_final[1])
			response=response+ "Found "+ restaurant_final[0]+ " in "+ str2 + " costs  " + str(restaurant_final[2])+ " for 2 and has a rating " + str(restaurant_final[3]) +"\n"

		message.attach(MIMEText(response, 'plain','utf-8'))
		#Create SMTP session for sending the mail
		try :
			session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
			session.starttls() #enable security
			session.login(sender_address, sender_pass) #login with mail_id and password
			text = message.as_string()
			session.sendmail(sender_address, receiver_address, text)
			session.quit()
		except :
			print('Something went wrong...')
		dispatcher.utter_message("message sent to " + receiver_address)		
		
class Check_location(Action):
	def name(self):
		return 'action_check_location'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
	
		check = check_location(loc)
		
		return [SlotSet('location',check['location_new']), SlotSet('location_found',check['location_f'])]		
				
