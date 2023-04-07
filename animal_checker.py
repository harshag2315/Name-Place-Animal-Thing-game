import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet

# ask the user to input an animal name
def is_animal(animal):
# check if the animal is in the WordNet database
    if len(wordnet.synsets(animal)) > 0:
        return True
    else:
        return False