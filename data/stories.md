## complete path 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_location
	- slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
	- slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
	- slot{"location": "delhi"}
	- utter_send_mail
* send_email{"mailid": "abc.gmail.com"}
	- slot{"mailid": "abc.gmail.com"}
	- action_send_email
* affirm		
    - utter_goodbye
    - export
## complete path 15
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_location
	- slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
	- slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
	- slot{"location": "delhi"}
	- utter_send_mail
* deny		
    - utter_goodbye
    - export	
## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_check_location
	- slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
	- slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
	- slot{"location": "mumbai"}
	- utter_send_mail
* send_email{"mailid": "xyz.gmail.com"}
	- slot{"mailid": "xyz.gmail.com"}
	- action_send_email
* affirm		
    - utter_goodbye
    - export
	
## complete path 16
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_check_location
	- slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
	- slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
	- slot{"location": "mumbai"}
	- utter_send_mail
* deny		
    - utter_goodbye	
	
## complete path 3
* greet
    - utter_greet
* restaurant_search{"location": "banglore"}
    - slot{"location": "banglore"}
	- action_check_location
	- slot{"location": "banglore"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
	- slot{"budget": "More than Rs. 700"}
    - action_search_restaurants
	- slot{"location": "banglore"}
	- utter_send_mail
* send_email{"mailid": "xyz.gmail.com"}
	- slot{"mailid": "xyz.gmail.com"}
	- action_send_email
* affirm		
    - utter_goodbye
    - export	
	
## complete path 4
* greet
    - utter_greet
* restaurant_search{"location": "warangal"}
    - slot{"location": "warangal"}
	- action_check_location
	- slot{"location": "warangal"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
	- slot{"budget": "More than Rs. 700"}
    - action_search_restaurants
	- slot{"location": "warangal"}
	- utter_send_mail
* send_email{"mailid": "kyc.gmail.com"}
	- slot{"mailid": "kyc.gmail.com"}
	- action_send_email
* affirm		
    - utter_goodbye
    - export	

## complete path 5
* greet
    - utter_greet
* restaurant_search{"location": "warangal"}
    - slot{"location": "warangal"}
	- action_check_location
	- slot{"location": "warangal"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
	- slot{"budget": "More than Rs. 700"}
    - action_search_restaurants
	- slot{"location": "warangal"}
	- utter_send_mail
* send_email{"mailid": "kyc.gmail.com"}
	- slot{"mailid": "kyc.gmail.com"}
	- action_send_email
* affirm		
    - utter_goodbye
    - export
## complete path 6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mbusmkwoid"}
    - slot{"location": "mbusmkwoid"}
	- action_check_location
	- slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "anantapur"}
    - slot{"location": "anantapur"}
	- action_check_location
	- slot{"location": null}
    - slot{"location_found": "tier3"}	
    - utter_foodie_not_working	
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}	
	- action_check_location
	- slot{"location": "hyderabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
	- slot{"budget": "More than Rs. 700"}	
    - action_search_restaurants
	- slot{"location": "hyderabad"}
	- utter_send_mail
* send_email
	- action_send_email	
    - utter_goodbye	

## complete path 7
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location	
* restaurant_search{"location": "anantapur"}
    - slot{"location": "anantapur"}
	- action_check_location
	- slot{"location": null}
    - slot{"location_found": "tier3"}	
    - utter_foodie_not_working
* restaurant_search{"location": "mbusmkwoid"}
    - slot{"location": "mbusmkwoid"}
	- action_check_location
	- slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound	
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"} 
	- action_check_location
	- slot{"location": "hyderabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine	
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
	- slot{"budget": "More than Rs. 700"}	
    - action_search_restaurants
    - slot{"location": "hyderabad"}
	- utter_send_mail
* send_email
	- action_send_email	
    - utter_goodbye	
	
	
## complete path 8
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location	
* restaurant_search{"location": "haridwar"}
    - slot{"location": "haridwar"}
	- action_check_location
	- slot{"location": null}
    - slot{"location_found": "tier3"}	
    - utter_foodie_not_working
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"} 
	- action_check_location
	- slot{"location": "hyderabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine	
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
	- slot{"budget": "More than Rs. 700"}	
    - action_search_restaurants
    - slot{"location": "hyderabad"}
	- utter_send_mail
* send_email
	- action_send_email	
    - utter_goodbye		

## complete path 9
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location	
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
	- action_check_location
	- slot{"location": null}
    - slot{"location_found": "tier3"}	
    - utter_foodie_not_working
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"} 
	- action_check_location
	- slot{"location": "hyderabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine	
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
	- slot{"budget": "More than Rs. 700"}	
    - action_search_restaurants
    - slot{"location": "hyderabad"}
	- utter_send_mail
* send_email
	- action_send_email	
    - utter_goodbye		
## complete path 12
* greet
    - utter_greet
* restaurant_search{"location": "anantapur"}
    - slot{"location": "anantapur"}
	- action_check_location
	- slot{"location": null}
    - slot{"location_found": "tier3"}	
    - utter_foodie_not_working
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
	- action_check_location
	- slot{"location": "hyderabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine	
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "More than Rs. 700"}
	- slot{"budget": "More than Rs. 700"}	
    - action_search_restaurants
    - slot{"location": "hyderabad"}
	- utter_send_mail
* send_email
	- action_send_email	
    - utter_goodbye	
	
## complete path 13
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
	- action_check_location
	- slot{"location": null}
    - slot{"location_found": "tier3"}	
    - utter_foodie_not_working
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_location
	- slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
	- slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
	- slot{"location": "delhi"}
	- utter_send_mail
* send_email{"mailid": "abc.gmail.com"}
	- slot{"mailid": "abc.gmail.com"}
	- action_send_email
* affirm		
    - utter_goodbye	
	
	
