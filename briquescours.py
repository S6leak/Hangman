# brick 1 : fonction qui affiche "You loose!" si le nombre passé en argument est supérieur ou égal à 12
def check_loose(num: int) -> None:
    if num >= 12:
        print("You loose!")

# brick 2 : import random et fonction qui retourne un nombre aléatoire entre 1 et 6 (inclus)
import random

def roll_d6() -> int:
    return random.choice({1, 2, 3, 4, 5, 6})

# brick 3 : import du pack english_words + print d'un mot aléatoire de la liste
from english_words import english_words_lower_set
def print_random_word():
    stri = random.choice(list(english_word_lower_set))
    print(stri)
    return stri
word = stri
# brick 4 : fonction la string en parametre, trouve lenght n de lastring et affiche des "_" n fois
def display_underscores(word: str) -> None:
    n = len(word)
    print("_ " * n)

