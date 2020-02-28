# Bar-Bot
A Restro Bar  BOT TO SAVE NAME, EMAIL AND CAR CHOICE OF THE USER. It saved data into a google sheet. Also It makes an api call from another google sheet to suggest car based on the choices chosen by him during conversation.

We will have various subsequent videos where we will understand the actions.py file, how to get credentials for google sheet to import data from rasa chatbot, understanding nlu data, pipelines and finally deploying the files in local using socket.io and also on server and connecting to website.

Youtube link below.


______________________________________________________________________________

To learn how to build your own Rasa chatbot the checkout this link : 
 https://www.youtube.com/playlist?list...
______________________________________________________________________________

Github : https://github.com/prescient-automation/Bar-Bot

Make sure the github repo doesnt have credentials file for the bot to communicate with the bot so when you clone the repo it wont save data but bot will work.
_______________________________________________________________


Running
Assuming you have the requirements installed - if you would like to run the code without going through the tutorial and building it from scratch run the following commands:

Train the chatbot:
$ rasa train
Launch the action server:
$ rasa run actions
Launch the chatbot in a different terminal:
$ rasa shell --endpoint endpoints.yml
Files
workspace
├── data
│ ├── nlu.md
│ └── stories.md
├── __init__.py
├── .gitignore
├── actions.py
├── config.yml
├── credentials.yml
├── domain.yml
├── endoints.yml
├── LICENCE
└── README.rst

 For any doubts or queries related to the topic, feel free to leave a comment below in the comment section.  For any further information or queries you can also connect with us at info@prescient-automation.com

Lets Learn For Free...
