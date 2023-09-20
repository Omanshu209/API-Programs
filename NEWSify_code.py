import requests
import os
from dotenv import load_dotenv

load_dotenv()

def bot(a):
	print(f"NewsBot : {a}\n********************")
	
def getNews():
	
	apiKey=f"{os.getenv('NEWSIFYAPIKEY')}"
	
	while True:
		q=input("USER : ")
		print("********************")
		
		if q == "exit()":
			bot('Thank you for using NEWSify ! ')
			break
			
		url=f'https://newsapi.org/v2/everything?q={q}&apiKey={apiKey}'
		bot('Searching.....')
		
		try:
			response = requests.get(url).json()
			bot("News -")
			#print(response)
			news=response
			
			for article in response['articles']:
				print('Source	:   ',article['source']['name'])
				print('Title :      ',article['title'])
				print('Description :',article["description"])
				print('URL :        ',article['url'])
				print("---------------------")
				
			print("********************")
			
		except:
			bot("! ERROR !")

if __name__=="__main__":
	bot("Welcome To NEWSify , I'm NewsBot and can give you news of a specific Topic ! [Enter exit() to leave]")
	getNews()