# --- Daily Challenge: Translator --- #
# Time to finish: 
# Instructions :
# 1) Consider this list
#    – french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
# 2) Look at this result :
#    – {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
# 3) You have to recreate the result using a translator module.

# IMPORT

from googletrans import Translator

# CODE

translator = Translator()

french_dict = {}
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
translation = translator.translate("Bonjour", src='fr')

for word in french_words:
  french_dict[word] = translator.translate(word, src='fr').text

print(french_dict) # -> {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}