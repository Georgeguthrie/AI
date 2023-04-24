import chatterbot.comparisons
import chatterbot.response_selection
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot import filters

chatbot = ChatBot("StudentBot",
                  read_only=True,
                  filters=filters.get_recent_repeated_responses,
                  storage_adapter="chatterbot.storage.SQLStorageAdapter",
                  logic_adapters=
                  [
                      {
                          "import_path": "chatterbot.logic.BestMatch",
                          "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,
                          "response_selection_method": chatterbot.response_selection.get_most_frequent_response


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
    "What's up",
}
conversationExample = {
    "Hello",
    "How are you?",
    "I am struggling with uni",
    "I am very sorry to hear that. Would you like to talk about it?",
    "Yes.",
}
conversationResponses = {
    "What are you doing?",
    "How are you?",
    "What are you up to?",
    "Not much, how about you?",
    "Are you feeling ok?",
}
conversationExample2 = {
    "I'm feeling overwhelmed",
    "How is uni going?",
    "I want to drop out",
    "That's not good. Is there a particular reason why?",
}
conversationExample3 = {
    "I'm unhappy",
    "Do you enjoy university?",
    "Not really",
    "Why not?",
    "It is stressful",
    "I am sorry to hear that",
}
conversationExample4 = {
    "I'm stressed",
    "How are your assignments going?",
    "I have too many deadlines",
    "Is that stressing you out?",
    "Yes",
}
conversationExample5 = {
    "I'm doing well",
    "How do you find University?",
    "I like it",
    "That's good to hear, what do you like about it?",
}
conversationExample6 = {
    "I don't know if I can get my work done in time",
    "Have you talked to your lecturer's about it?",
    "They're very busy",
    "Contacting your programme leader may be a good idea",
}
conversationExample7 = {
    "Hi",
    "Hello, how are you?",
    "I'm fine",
    "Just fine? Why?",
    "I'm a bit stressed",
    "What is making you feel stressed?",
    "University",
    "Is it exams?",
    "Yes, I am feeling anxious about them",
    "That's ok, everyone feels at least a little anxious about exams",
    "Thanks, but I feel really worried about them",
    "Have you tried talking to any support services at your university?",
    "No, I haven't tried that",
    "You should look at your universities website, there will be support available there",
}

trainer = ListTrainer(chatbot)

training_data_convo1 = open('training_data/ConversationExample1.txt').read().splitlines()
training_data_convo2 = open('training_data/ConversationExample2.txt').read().splitlines()
training_data_convo3 = open('training_data/ConversationExample3.txt').read().splitlines()
training_data_convo4 = open('training_data/ConversationExample4.txt').read().splitlines()
training_data_convo5 = open('training_data/ConversationExample5.txt').read().splitlines()
training_data_convo6 = open('training_data/ConversationExample6.txt').read().splitlines()
training_data_convo7 = open('training_data/ConversationExample7.txt').read().splitlines()

training_data = training_data_convo1 + training_data_convo2 + training_data_convo3 + training_data_convo4 + training_data_convo5 + training_data_convo6 + training_data_convo7

trainer.train(training_data)

while True:
    user_input = input()
    bot_response = chatbot.get_response(user_input)
    print(bot_response)

