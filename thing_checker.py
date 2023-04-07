import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn

def is_thing(input_str):
    """
    Returns True if the input_str is a valid noun,
    False otherwise.
    """
    synsets = wn.synsets(input_str, pos=wn.NOUN)
    return len(synsets) > 0
