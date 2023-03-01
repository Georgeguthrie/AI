from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Test",
                  storage_adapter="chatterbot.storage.SQLStorageAdapter",
                  logic_adapters=
                  [
                      {
                          "import_path": "chatterbot.logic.BestMatch"
                      },
                      {
                          "import_path": "chatterbot.logic.SpecificResponseAdapter",
                          "input_text": "Red Rum",
                          "output_text": "All work and no play makes Jack a dull boy"
                      },
                      {
                          "import_path": "chatterbot.logic.SpecificResponseAdapter",
                          "input_text": "Is this real life",
                          "output_text": "or is this just fantasy"
                      }
                  ]
                  )

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
    user_input = input()
    bot_response = chatbot.get_response(user_input)
    print(bot_response)

