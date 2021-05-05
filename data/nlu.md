## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Anantapur](location).
- I am looking for some restaurants in [Rishikesh](location).
- I am looking for some restaurants in [Haridwar](location).
- I am looking for some restaurants in [kjahshdf](location).
- I am looking for some restaurants in [mbusmkwoid](location).
- I am looking for some restaurants in [Bangalore](location)
- I am looking for some restaurants in [Banghaslur](location)
- [jhskhafaskf](location)
- [kjaskhflajskjaskdklf](location)
- [akjsknf](location)
- [bergshadhh](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [low]{"entity": "budget", "value": "Lesser than Rs. 300"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- can you book a table in [hyderabad](location) in a [moderate]{"entity": "budget", "value": "Rs. 300 to 700"} price range with [chinese](cuisine) 
- can you book a table in [chennai](location) in a [high]{"entity": "budget", "value": "More than Rs. 700"} price range with [chinese](cuisine) 
- please show me some restaurants in [More than Rs. 700](budget) price range in [Delhi](location)
- please show me some restaurants in [low]{"entity": "budget", "value": "Lesser than Rs. 300"} price range in [Delhi](location)
- please help me to find restaurants in [pune](location)
- Please find me a restaurant in [bangalore](location)
- Please find me a restaurant in [banglaisur](location)
- Please find me a restaurant in [chekasf](location)
- Please find me a restaurant in [kahsni](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- please find me [mecican](cuisine) restaurant in [dehli](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)

## intent:send_email
- yes.send mail to [xyz@gmail.com](mailid)
- yeah mail it to [abc@yahoo.com](mailid)
- ok.mail it to [abc.red@yahoo.com](mailid)
- fine.please send mail to [xyz@gmail.com](mailid)
- mail it to [a1c@yahoo.com](mailid)

## intent:deny
- No
- Nah
- not needed
- do not send.


## lookup:locations
- Ahmedabad
- Bengaluru
- Chennai 
- Delhi 
- Hyderabad
- Kolkata
- Mumbai 
- Pune
- Agra
- Ajmer
- Aligarh
- Amravati
- Amritsar
- Asansol
- Aurangabad
- Bareilly
- Belgaum
- Bhavnagar
- Bhiwandi
- Bhopal
- Bhubaneswar
- Bikaner
- Bilaspur
- Bokaro Steel City
- Chandigarh
- Coimbatore
- Cuttack
- Dehradun
- Dhanbad
- Bhilai
- Durgapur
- Dindigul
- Erode
- Faridabad
- Firozabad
- Ghaziabad
- Gorakhpur
- Gulbarga
- Guntur
- Gwalior
- Gurgaon
- Guwahati
- Hamirpur
- Hubli–Dharwad
- Indore
- Jabalpur
- Jaipur
- Jalandhar
- Jammu
- Jamnagar
- Jamshedpur
- Jhansi
- Jodhpur
- Kakinada
- Kannur
- Kanpur
- Karnal
- Kochi
- Kolhapur
- Kollam
- Kozhikode
- Kurnool
- Ludhiana
- Lucknow
- Madurai
- Malappuram
- Mathura
- Mangalore
- Meerut
- Moradabad
- Mysore
- Nagpur
- Nanded
- Nashik
- Nellore
- Noida
- Patna
- Pondicherry
- Purulia
- Prayagraj
- Raipur
- Rajkot
- Rajahmundry
- Ranchi
- Rourkela
- Salem
- Sangli
- Shimla
- Siliguri
- Solapur
- Srinagar
- Surat
- Thanjavur
- Thiruvananthapuram
- Thrissur
- Tiruchirappalli
- Tirunelveli
- Ujjain
- Bijapur
- Vadodara
- Varanasi
- Vasai-Virar City
- Vijayawada
- Visakhapatnam
- Vellore
- Warangal

## synonym:4
- four

## synonym:Delhi
- New Delhi
- Dilli

## synonym:Bangalore
- Bengaluru

## synonym:Chennai
- Madras

## synonym:Mumbai
- Bombay

## synonym:Kolkata
- Calcutta

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:Mexican
- Mihican
- Mecican

## synonym:Italian
- Italia
- Italy




## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## regex:location
- [a-zA-Z]+

## regex:mailid
- [a-zA-Z0-9_.+]+@[a-zA-Z]+[.][a-zA-Z0-9-.]+$