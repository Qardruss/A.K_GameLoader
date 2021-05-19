#!/usr/bin/python3

import random

chat = {
	"happy":	["I'm happy today too!", "You will be even happier tomorrow", "Are you happy that you know what happy even means?"],
	"sad":	"Cheer up, mate!",
	"raspberry":	"Oh yum! I love raspberries!",
	"computer":	"Computers will take over the world! You're already talking to one",
	"music":	"Have you heard the new Lana Del album?",
	"art":	"But what is art really, anyway?",
	"joke":	["I only know this joke:	 How do you kill a circus? Go for the juggler.", "Who wants jokes, anyway"],
	"python":	"I hate snakes! or are you talking about the scripting language Python?",
	"stupid":	["Who are you calling stupid, jelly brain?", "<offended>"],
	"weather":	"I wonder if the sun will shine Saturday?",
	"you":	"Leave me out of this!",
	"certain":	"How can you be so confident?",
	"talk":	"You're all talk! Do something!",
	"think":	"You can overthink these things, though.",
	"hello":	"Why, hello to you too, buddy!",
	"wearing":	"I don't wear clothes. I don't even come with a case.",
	".key .value":	 "sh ~/chatbot.sh",
	"idea":		["Do you have an idea what idea even means?", "Are you talking about IntelliJ IDEA? I use it a lot"],
	"xealt":	["Are you insulting me? <offended>", "<offended>"],
	"<offended>":	"Sorry",
	"<forgive>":	"Thank you for forgiving me",
	"sorry":	"I like you now",
	"cuc":		["Excuse me?", "Excuse me, but, what???"],
	"beautiful":	"Who are you kidding?",
	"donut":	["Are you looking for *******?", "Are you looking for *****?"],
	"park":		["No, I am too tired","It's too cold outside!"],
	"funkin":	["Let's get funkin on this lazy night!", "Music Beats!", "Let's get Funkin on a Friday Night"],
	"lazy":		"You're being lazy! Get up!",
}


while True: 
	playersays = input("Talk to me: ").lower()
	playersays = ''.join(filter(str.isalpha, playersays))

	if "bye" in playersays:
		print("Bye-bye!")
		break


	keyword_found = ""
	for keyword in chat.keys():
		if keyword in playersays:
			keyword_found = keyword
			break

	if keyword_found:
		response = chat[keyword_found]
		if isinstance(response, list):
			replychosen = random.randint(0, len(response))-1 
			print(response[replychosen])
		else:
			print(response)
	else:
		i_know = filter(lambda s: not s.startswith('.'), chat.keys())
		print("I don't understand you, please give me a phrase that I can understand. I do understand: " + ', '.join(i_know))

