# Hack-a-thing 2: Travel Needs
## Helen He and Jiyun Sung 

### Usage 

We created a Facebook page called Travel Needs that hosts an intelligent chat bot! You just have to message the page to interact with the chat bot (but it only works for the Admin account because it's not a published chat bot).

### What we built

For this assignment, we decided to build a Facebook Messenger chat bot that helps the user determine various travel necessities they must keep in mind for their next vacation.

The user provides their citizenship, countries they plan on traveling to, and the dates of their stay. The chat bot will then respond with information including:  
	-visa requirements  
	-currency and exchange rate information  
	-weather  
	-plug types and voltage for outlets  

Typically, a traveler would have to search each of these pieces of information separately, which requires not a small amount effort on their part. This chat bot compiles all of this information, making it easy and convenient for someone to begin planning their travel!


### Who did what

Jiyun built the Python Flask app on pythonanywhere, allowing us to host a WebApp without building a server.

Helen set up the Facebook Messenger Platform and linked the WebHook between Messenger and the WebApp.

We both contributed to training the chat bot on api.ai to respond appropriately to user input.

### What we learned

We learned:  
	-that it's pretty straightforward and pain-free to set up a Facebook for developers account.   
	-about api.ai, a technology that gives allows users to build conversational apps that can be used on multiple platforms, including Twitter, Facebook Messenger, Skype, and Slack.  
	-that NLP has its pros and cons:  
		-pros: deciphering misspelled words  
		-cons: makes it difficult more difficult to guide the conversation than if you were hardcoding the flow  


### What didn't work

We originally tried following Hartley Brody's messenger bot tutorial found at https://blog.hartleybrody.com/fb-messenger-bot/, but we ran into trouble with the virtualenvwrapper shell. Nothing we did could get the command to be recognized, so we abandoned that avenue and used a different tutorial.

### Acknowledgements 

We followed two guides to create our chat bot:

1. Facebook for Developer's Messenger Platform set-up guide
2. A messenger bot tutorial found at https://chatbotnewsdaily.com/build-a-facebook-messenger-chat-bot-in-10-minutes-5f28fe0312cd
