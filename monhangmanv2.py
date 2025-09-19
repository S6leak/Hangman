# 1. imports et dépendances
import random
import random
try:
    from english_words import english_words_lower_set
except Exception:
    # Fallback minimal si le package n’est pas disponible
    english_words_lower_set = {"apple", "python", "school", "hangman", "butterfly"}


# fonction qui retourne un mot aléatoire de la liste
def random_word() -> str:
    return random.choice(list(english_words_lower_set))

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


# 4. boucle principale du jeu
while penalties < max_penalties:
    print(render_mask(secret, guesses), "/", max_penalties - penalties, "essais restants")
    def show_board(secret: str, guesses: set[str], penalties: int, max_penalties: int) -> None:
        print()  # espace avant le board
    if guesses:
        print("Lettres proposées :", ", ".join(sorted(guesses)))
    print()  # espace après le board
    show_board(secret, guesses, penalties, max_penalties)
    guess = input("Proposez une lettre ou un mot : ").strip().upper()
    print("Tu as proposé :", guess)
    # invalid input
    if not guess.isalpha():
        print("Veuillez entrer uniquement des lettres (A–Z).")
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
                print("You loose!")
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
                print(f"Ohhh nooo la policia noooooo... Le mot était : {secret}")
                break


