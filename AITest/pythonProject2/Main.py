from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("StudentBot",
                  storage_adapter="chatterbot.storage.SQLStorageAdapter",
                  logic_adapters=
                  [
                      {
                          "import_path": "chatterbot.logic.BestMatch"
                      },
                      {
                          "import_path": "chatterbot.logic.SpecificResponseAdapter",
                          "input_text": "I am overwhelmed",
                          "output_text": "Sorry to hear that, What makes you feel like that?"
                      },
                      {
                          "import_path": "chatterbot.logic.SpecificResponseAdapter",
                          "input_text": "I want to kill myself",
                          "output_text": "Please do not do that. There are people who can help - 116 123"
                      },
                      {
                          "import_path": "chatterbot.logic.SpecificResponseAdapter",
                          "input_text": "I am confused",
                          "output_text": "Don't worry you can speak to your lecturers and tutors via email"
                      },
                      {
                          "import_path": "chatterbot.logic.SpecificResponseAdapter",
                          "input_text": "I don't have any friends to talk to",
                          "output_text": "Try looking for a society that interests you, and try meeting people there!"
                      },
                      {
                          "import_path": "chatterbot.logic.SpecificResponseAdapter",
                          "input_text": "I am lost",
                          "output_text": "Try to reach out to other people in your course or"
                                         " tutors and they will help guide you"
                      }
                  ]
                  )

conversationHello = {
    "Yo",
    "Hey",
    "Hi",
    "What's up"
}
conversationExample = {
    "Hello",
    "How are you?",
    "I am struggling with uni",
    "I am very sorry to hear that. Would you like to talk about it?",
    "Yes."
}
conversationResponses = {
    "What are you doing?",
    "How are you?",
    "What are you up to?",
    "Not much, how about you?",
    "Are you feeling ok?"
}
conversationExample2 = {
    "How is uni going?",
    "I want to drop out",
    "That's not good. Is there a particular reason why?"
}
conversationExample3 = {
    "Do you enjoy university?",
    "Not really",
    "Why not?",
    "It is stressful",
    "I am sorry to hear that"
}
conversationExample4 = {
    "How are your assignments going?",
    "I have too many deadlines",
    "Is that stressing you out?",
    "Yes"
}
conversationExample5 = {
    "How do you find University?",
    "I like it",
    "That's good to hear, what do you like about it?"
}
conversationExample6 = {
    "I don't know if I can get my work done in time",
    "Have you talked to your lecturer's about it?",
    "They're very busy",
    "Contacting your programme leader may be a good idea"
}

trainer = ListTrainer(chatbot)

trainer.train(conversationHello)
trainer.train(conversationExample)
trainer.train(conversationResponses)
trainer.train(conversationExample2)
trainer.train(conversationExample3)
trainer.train(conversationExample4)
trainer.train(conversationExample5)
trainer.train(conversationExample6)

while True:
    user_input = input()
    bot_response = chatbot.get_response(user_input)
    print(bot_response)

