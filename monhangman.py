# initialisation des variables de base
secret = random_word().upper()
guesses = set()
penalties = 0
max_penalties = 12 

print("👾Bienvenue dans le jeu du Pendu !👾")
print(render_mask(secret, guesses),"/", max_penalties - penalties, "essais restants") 

while penalties < max_penalties:
    print(render_mask(secret, guesses),"/", max_penalties - penalties, "essais restants")
    guess = input("Proposez une lettre ou un mot : ").strip().upper()
    print("Tu as proposé : ", guess)
    if not guess.isalpha():
        print("Veuillez entrer uniquement des lettres.")
        continue
    if len(guess) == 1:
        print("C'est une lettre.") #a revoir car il manque le traitement de si c'est une erreur ou pas
    else: 
        print("C'est un mot.") #a revoir car il manque le traitement de si c'est une erreur ou pas
    if guess in guesses:
        print("Vous avez déjà proposé cette lettre/mot.")
        continue
    guesses.add(guess)

