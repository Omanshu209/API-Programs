from requests import get

#function to get the current train details by PNR
def getData(pnr):
	URL = f"https://pnr-status-indian-railway.p.rapidapi.com/pnr-check/{pnr}"
	HEADERS = {
		"X-RapidAPI-Key": "feaaad2b53msh311ff44e1515795p1f08abjsn48bdf7d48c68",
		"X-RapidAPI-Host": "pnr-status-indian-railway.p.rapidapi.com"
	}
	RESPONCE = get(URL, headers = HEADERS)
	return RESPONCE.json()

PNR = int(input(f"{'*'*20}\n\nPNR CHECKER\n\n{'*'*20}\nEnter the PNR of your ticket : "))#

DATA = getData(PNR)#retreiving data from the API

#preparing the output data
OUTPUT_STRING = f"{'*'*20}\n\nTRAIN INFO : \n\n\tTrain Name : {DATA['data']['trainInfo']['name']}\n\tPNR : {PNR}\n\n{'*'*20}\n\nBOARDING INFO : \n\n\tBoarding Station : {DATA['data']['boardingInfo']['stationName']} ({DATA['data']['trainInfo']['boarding']})\n\tArrival Time : {DATA['data']['boardingInfo']['arrivalTime']}\n\tDeparture Time : {DATA['data']['boardingInfo']['departureTime']}\n\n{'*'*20}\n\nDESTINATION INFO :\n\n\tDestination Station : {DATA['data']['destinationInfo']['stationName']} ({DATA['data']['trainInfo']['destination']})\n\tArrival Time : {DATA['data']['destinationInfo']['arrivalTime']}\n\tDeparture Time : {DATA['data']['destinationInfo']['departureTime']}\n\n{'*'*20}\n\nPASSENGER INFO : \n\n\t"
for i in range(DATA['data']['seatInfo']['noOfSeats']):
	OUTPUT_STRING += f"PASSENGER {i+1} :\n\t\tCoach : {DATA['data']['passengerInfo'][i]['currentCoach']}\n\t\tBerth No. : {DATA['data']['passengerInfo'][i]['currentBerthNo']}\n\t"
OUTPUT_STRING += f"\n{'*'*20}\nDEVELOPED BY OMANSHU\n{'*'*20}"

print(OUTPUT_STRING)
#Developed by Omanshu