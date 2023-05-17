
# --- 🌟 Exercise 1 – Random Sentence Generator ---
# Instructions
# Description: In this exercise we will create a random sentence generator. 
# We will do this by asking the user how long the sentence should be and then printing the generated sentence.
# Hint : The generated sentences do not have to make sense.
# 1) Download this word list
# 2) Save it in your development directory.
# 3) Create a function called get_words_from_file. This function should read the file’s content and
#    return the words as a collection. What is the correct data type to store the words?
# 4) Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# 5) use the words list to get your random words.
#    the amount of words should be the value of the length parameter.
# 6) Take the random words and create a sentence (using a python method), the sentence should be lower case.
# 7) Create a function called main which will:
#    Print a message explaining what the program does.
# 8) Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. 
#    Validate your data and test your validation!
# 9) If the user inputs incorrect data, print an error message and end the program.
#    If the user inputs correct data, run your code.


# 🌟 Exercise 2: Working With JSON
# Instructions
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""


# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.