# ImageBoet
## A simple python bot for Telegram for having a nice little chit chat with.

### What is ChatBoet?
ChatBoet is a chat bot for telegram that is funny to chat to!

### How does it work?
ChatBoet will listen for all messages in a given chat (either directly with him or in a chat room which you invite him to) starting with "/get".
tl;dr: Look at one of the existing commands, you must have a run(bot, chat_id, user, request_text, keyConfig, number_of_results) function.

### How do I make my own bot using this?
Go to https://console.developers.google.com and create a Google App Engine project. Then take that project id (it might be two random words and a number eg. gorilla-something-374635) and your Telegram Bot ID which the Bot Father gave you and do the following:

1. Copy keys.ini.template and rename the copy to keys.ini.
2. Update {Your Telegram Bot ID here} in keys.ini

OPTIONAL:
3. Update the rest of keys.ini with keys for each command you want to use.
4. Copy pre-push to the .git\hooks folder.
5. In .git\hooks\pre-push change were it says [[PythonInstallation]] to your Python install location in bash notation (e.g. /C/Python27) and your 
6. In .git\hooks\pre-push change were it says [[GoogleCloudSDKInstallation]] to your Google Cloud SDK install location in bash notation (e.g. /C/Program Files (x86))
7. In .git\hooks\pre-push change were it says [[GoogleAppEngineProjectName]] to your Google App Engine Project ID in bash notation (e.g. /C/Program Files (x86))
8. Now when you push it will automagicly build and deploy ChatBoet to the cloud! To the hindenpeter!

```bash
git clone (url for your ChatBoet fork) ~/bot
cd ~/bot
(PATH TO PYTHON27 INSTALL)\scripts\pip.exe install -t lib python-telegram-bot google-api-python-client
(PATH TO GOOGLE APP ENGINE LAUNCHER INSTALL)appcfg.py -A {GOOGLE APP ENGINE PROJECT ID} update .
```

Finally go to https://{GOOGLE APP ENGINE PROJECT ID}.appspot.com/set_webhook?url=https://{GOOGLE APP ENGINE PROJECT ID}.appspot.com/webhook (replace both {GOOGLE APP ENGINE PROJECT ID}s with the Google App Engine Project ID) to tell Telegram where to send web hooks. This is all that is required to setup web hooks, you do not need to tell the Bot Father anything about web hooks.

### Why the name ChatBoet?
Boet is Afrikaans for brother. This bot is integrated with chatgpt, talking to him is like joking around with your "boet".
