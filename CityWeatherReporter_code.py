from requests import get

print("Welcome to City Weather Reporter ! ")

def Location(city_name):
	
	apiKey="d60918d6f3604a6c9e9134244230403"
	url = f"https://api.weatherapi.com/v1/current.json?key={apiKey}&q={city_name}&aqi=no"
	responce = get(url).json()
	
	try:
		location = f'{responce["location"]["name"]} , {responce["location"]["region"]} , {responce["location"]["country"]}'
		latitude = responce["location"]["lat"]
		longitude = responce["location"]["lon"]
		localtime = responce["location"]["localtime"]
		info_last_updated = responce["current"]["last_updated"]
		Temperature_C = f'{responce["current"]["temp_c"]} °C'
		Temperature_F = f'{responce["current"]["temp_f"]} °F'
		
		if responce["current"]["is_day"] == 0:
			is_day="No"
		elif responce["current"]["is_day"] == 1:
			is_day="Yes"
			
		WindSpd_kmp = f'{responce["current"]["wind_kph"]} km/hr'
		WindSpd_mph = f'{responce["current"]["wind_mph"]} m/hr"'
		
		return f"\033[35m********************\nLocation : {location}\nLatitide : {latitude}\nLongitude : {longitude}\nLocal Time : {localtime}\nInformation Last Updated : {info_last_updated}\nTemperature(in Celcius) : {Temperature_C}\nTemperature(in Ferheinheit) : {Temperature_F}\nIs it day? : {is_day}\nWind Speed(in kmp) : {WindSpd_kmp}\nWind Speed(in mph) : {WindSpd_mph}"
		
	except:
		return "ER : Location Not Found"

run = True
while run:
	print("\033[36m********************")	
	print(Location(input("Enter City's Name : ")))