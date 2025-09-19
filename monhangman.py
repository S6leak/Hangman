# 1. imports et dépendances
import random
from english_words import get_english_words_set

# construit un set de mots depuis la wordlist "web2", en minuscules et A–Z uniquement
WORDS = get_english_words_set(['web2'], lower=True, alpha=True)
WORDS_LIST = list(WORDS)  # on liste une fois pour accélérer random.choice

def random_word() -> str:
    return random.choice(WORDS_LIST)

# fonction qui affiche la lettre si elle a été devinée une fois, meme si elle est présente plusieurs fois
def is_word_guessed(secret: str, guesses: set[str]) -> bool:
    return all(ch in guesses for ch in set(secret))

# fonction qui affiche le mot avec les lettres devinées et des "_" pour les lettres non devinées
def render_mask(secret: str, guesses: set[str]) -> str:
    return " ".join(ch if ch in guesses else "_" for ch in secret)

# fonction qui affiche des "_" n fois
def display_underscores(word: str) -> str:
    n = len(word)
    return "_ " * n

# 2. initialisation des variables de base
secret = random_word().upper()
guesses = set()
penalties = 0
max_penalties = 12 

# 3. Intro
print("👾Bienvenue dans le jeu du Pendu !👾") 

print()

# 4. boucle principale du jeu
while penalties < max_penalties:
    print(render_mask(secret, guesses), "/", max_penalties - penalties, "essais restants")
    if guesses:
        print("Lettres proposées :", ", ".join(sorted(guesses)))
    print()
    guess = input("Proposez une lettre ou un mot : ").strip().upper()
    print("Tu as proposé :", guess)
    # invalid input
    if not guess.isalpha():
        print("Veuillez entrer uniquement des lettres (A-Z).")
        continue
    # Chemin LETTRE
    if len(guess) == 1:
        # Déjà proposée ?
        if guess in guesses:
            print("Vous avez déjà proposé cette lettre.")
            continue
        # ajouter la lettre aux propositions maintenant qu'elle est validée
        guesses.add(guess)
        # Lettre est dans le mot ?
        if guess in secret:
            count = secret.count(guess)
            print(f"Bien joué ! La lettre {guess} apparaît {count} fois.")
            # Victoire si toutes les lettres sont révélées
            if is_word_guessed(secret, guesses):
                print(f"Félicitations ! Vous avez deviné le mot : {secret}")
                break
        else:
            # Mauvaise lettre → +1 pénalité
            penalties += 1
            print(f"Dommage ! La lettre {guess} n'est pas dans le mot.")
            if penalties >= max_penalties:
                print(f"Perdu... Le mot était : {secret}")
                break

    #  Chemin MOT
    else:
        if guess == secret:
            print(f"Félicitations ! Vous avez deviné le mot : {secret}")
            break
        else:
            # règle du sujet : mot incorrect = +5 pénalités
            penalties += 5
            print(f"Presque... ou pas, {guess} n'est pas le mot 🤷‍♂️.")
            if penalties >= max_penalties:
                print(f"Ohhh nooo la polizia noooooo... Le mot était : {secret}")
                break


