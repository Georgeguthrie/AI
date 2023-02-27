from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Test')

conversation = {
    "Hello",
    "How are you?",
    "I am struggling with uni",
    "I am very sorry to hear that. Would you like to talk about it?",
    "Yes."
}
conversation2 = {
    "Did you see the stars tonight?",
    "Yeah they were pretty",
    "I heard there is an eclipse later",
    "That sounds cool"
}

trainer = ListTrainer(chatbot)

trainer.train(conversation)
trainer.train(conversation2)

while True:
    try:
        user_input = input()

        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break