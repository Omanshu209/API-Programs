from requests import get

#setup
apiLink = "https://api.funtranslations.com/translate/shakespeare.json?text="
print(f"{'-'*20}\nShakespeare Converter\n{'-'*20}")

while(True):
	
	#preparing the data
	wordsInSentence = input(f"{'-'*20}\nEnter the sentence/s you want to translate to shakespeares's language : ").split(' ')
	for i in range(len(wordsInSentence)):
		apiLink += wordsInSentence[i] + "%20"
	print('-'*20)
	
	#posting a https request using requests module
	responce = get(apiLink).json()
	try:
		print(f"{'-'*20}\nTranslated Sentence : {responce['contents']['translated']}\n{'-'*20}")
	except KeyError:
		print(f"{'-'*20}\nError (Try after an hour) :\n{responce}\n{'-'*20}")
	
	apiLink = "https://api.funtranslations.com/translate/shakespeare.json?text="

#Developed By Omanshu