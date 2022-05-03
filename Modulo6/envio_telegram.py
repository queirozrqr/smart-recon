import telegram

message = "Teste de mensagem"
bot = telegram.Bot(token='5180853037:AAEAQVVNAil6Y99Gw1Xlnn1SIHOjrJBYXFc')
bot.send_message(text=message, chat_id=35130497)

#pip3 install python-telegram-bot --upgrade
