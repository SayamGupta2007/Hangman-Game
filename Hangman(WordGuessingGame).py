                        #HANGMAN GAME : WORD GUESSING GAME

#CENTRAL IDEA FOR MAKING:
#Random meanings along with their respective random word ---> Dictionary usage
#Level Every time gets increased by 1 with every question answered correctly ---> for loop or while True
# user will give the word ---> taking input
# checking the user given word with the correct respective word of the meaning ---> if loop and may be found method
#Length shall be given to the user of the word of which the meaning has been given to him/her and he/she has to guess the word correctly.


import random
from words import WORDS #I have to create a file words.py from which i will import words

import requests

current_index = 0 #firstly we will be at the index = 0 
print("Welcome to the Hangman Game.\n Guess the correct words and win rewards.")
Level = 0

while True:
   
    S = input("Do you want to Start the game ?\n 1.start 2.exit \n")
    

    if S.lower()=="start":

         def get_word():
             global current_index #I have used global keyword(global keyword is used because we are inside a function agar pehle define kiya hua hai toh loop mein global keyword lgane ki zarurat nhi hoti)as the function will think that it is a new term inside the function but I kniow that it is a global thing which is defined outside already
             
             if current_index >= len(WORDS): 
                 current_index = 0 #THIS MEANS THAT IF I HAVE reached the end of the list WORDS That is if i have reached above the 1000 words then it will restart the game
            
             word_len = len(WORDS[current_index]) #defined the term word_len

             same_length_words = [] # I have made a list same_length_words which will gather each word of same length together and then will randomly choose a word from that list

             while current_index < len(WORDS) and len(WORDS[current_index]) == word_len:
                 same_length_words.append(WORDS[current_index])
                 current_index += 1


             word = random.choice(same_length_words)

             return word

                 
        
         def Meaning(word):  
            #by putting word inside the meaning function I mean to say that the word that arrives from the above function gets into this function and only then the meanings can be found
             while True:
                 url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
                 response = requests.get(url).json()
                 #when response is a list with atleast one element
                 if not response or not isinstance(response, list):
                     word = get_word()
                     continue
                 # not isinstance(response, list) means that if the response is not a list then retry and find a new reponse until it could find the response which is a list i can also use isinstance(response, dict)(this means that if the response is a dictionary) instead of not isinstance(response, list) as the response here can only be a list or dictionary 
                 
                 
            #We have used if not response because API does not always provide a definition and in case if there is no response the program can return None
               #   meanings = response[0].get('meanings', []) this thing will not work now as it will return an empty list if there is no meanings in the response list now I have used the if not meanings then it will retry not return a empty list
               #Now thsi if not response[0].get("meanings"): means that does the key 'meanings' exist and is it non empty here response is a dictionary
                 
                 meanings = response[0].get("meanings")
                 if not meanings:
                     word = get_word()
                     continue
                 
                 definitions = meanings[0].get("definitions")

                 if not definitions:
                     word = get_word()
                     continue
                 
                 meaning = definitions[0].get("definition")

                 if not meaning:
                     word = get_word()
                     continue

                 return meaning                     
                 #I have used if not definitions so that if definitions does not exist then again  a new word has to be find out 
                 
                 
             #here response is as follows and then I have done the folowing 6 steps:
#              response = [
#                  {
#                    "meanings": [
#                      {
#                          "definitions": [
#                            {
#                              "definition": "To compute the average of something",
#                              "example": "...",
#                              "synonyms": []
#                          }
#                     ]
#                }
#           ]
#      }
# ]

             #we have not used return response[0].get("meanings")[0] because get() returns None if no meanings exist and get() is used for checking and applying all those if not will get the meaning then only the the meaning gets returned as I have told to retry every time if I don't get the meaning
                 
         #we have written empty list after meanings in get bracket to demonstrate that if meanings does not exist give me an empty list instead and now meanings are itself a list and I only want one meaning then i will return meaning[0] which is the first meaning of the word provided
         #response in this dictionary API can be either a dictionary or can be a list as well
        #response[0] is done because the response is a list with a dictionary inside it having different meanings of a single word or response can be a dictionary itself

         while True:
            correct_answer = get_word()
            meaning = Meaning(correct_answer)
            #here inside while true loop is also used beacuse it will help to get new word each time 
            #here while true will call the function every time you start the game

            
         #we have used while true because this dictionary api not always have the meaning of the random word so this loop (while true) will run until it finds a meaning as it will break only when meaning of random word is found as if we not use this loop then the function in case if it doesn't find the meaning will return none which is a bad thing  of the game  and due to this if we apply while true it will run un til it finds a random word whose meaning is present in the dictionary api
            while True:
                #this above while True is used so that the same word from the above called function repeats if there is an incorrect answer given by the user which just happens same in the real hangman game which we play
                #if the user input is correct then this while true loop (at 116 line) will break and the new word comes but if the user input is incorrect this loop will not break and this while loop(116 line) will run again with the same word until the user provides the correct answer
                print("Meaning of the word: ", meaning)
                print("The length of the word is", len(correct_answer))
                print(f"Current Level = {Level}")
                user_answer = input("Guess the word and Enter your answer: ")

                if user_answer.lower() == correct_answer.lower() :
                    Level = Level + 1
                    print(f"Correct Answer.You reached the Level: {Level}")
                    n = input("Do yo want to go to the next Level ?\n 1.yes  2.no \n")
                    if n.lower() == "yes":
                        break
                    elif n.lower() == "no":
                        exit()
                    else:
                        print("Invalid Input. Please give your answer in the terms of yes or no")

                else:
                    print("Incorrect answer. Try Again")

    elif S.lower()=="exit":
         exit()

    else:
         print("Invalid Input. Please provide a correct input")
