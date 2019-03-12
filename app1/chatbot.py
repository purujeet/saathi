from chatterbot import ChatBot
import json
from chatterbot.trainers import ChatterBotCorpusTrainer
from .speech import translate

def bot_start(x):
	print("Status: Reading file")

	fp=open('/home/ubuntu/Desktop/chatbot_hindi/website_saathi/saathi/static/app1/hinglish.json','r')
	dic=json.load(fp)
	fp.close()
	#print(dic)
	print("Status:Reading file completed")
	print("Initializing bot")
	y=ChatBot("y")

	print("\n\n\nStatus:Training dataset\n\n\n")
	trainer=ChatterBotCorpusTrainer(y)
	trainer.train(
		"/home/ubuntu/Desktop/chatbot_hindi/website_saathi/saathi/static/app1/export.json"
		#"chatterbot.corpus.hindi.greetings"
		)

	#trainer.export_for_training('./export.json')
	print("\n\n\nStatus:Training completed\n\n\n")
	
	#x=input('Enter text:')
	x=x.strip().split()
	tx=''
	for i in x:
		try:
			tx+=dic[i]+'\t'
		except KeyError as e:
			print('error: taking it same ')
			tx+=i
	print('Translated Text: ',tx)
	resp=y.get_response(tx)
	print('\t\t\t\t\t\t\t\t',translate(resp),end="\n\n")
	print('\t\t\t\t\t\t\t\tResponse:',resp,end="\n\n")

	return [translate(resp),resp]


if __name__=="__main__":
	bot_start(input())
