import sys
import string


#Le script doit etre utilise de cette façon : python PASS-checker.py Password123

#a partir de la, le programme recupere le mdp et le met dans une variable str et on créer stop

mot_de_passe=sys.argv[1]

stop=False

if len(sys.argv) != 2:
      print("Usage : python PASS-checker.py <mot_de_passe>")
      sys.exit(1)

#Avant toute chose, il regarde si le mot de passe est dans rockyou et dans une wordlist FR



#ouverture du fichier francais
with open("francais.txt", "r", encoding="utf-8", errors="ignore") as francais:
    if mot_de_passe in francais.read():
            stop=True
            
#ouverture de rockyou.txt            
with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as rockyou:
    if mot_de_passe in rockyou.read():
            stop=True

#Si le mdp est dans une wordlist, on affiche un message special disant qu'il faut surtout pas utiliser ce mdp
if stop==True:
    print("Votre mot de passe est crackable et ne doit pas etre utilisé")
    print("")
    print("Merci d'avoir utiliser PASS-checker")
    sys.exit()

#Si ce n'est pas le cas, on evalue la robustesse en calculant un score
#Creation de variable int score
score=0

if len(mot_de_passe) <= 6 :
    score +=0
elif len(mot_de_passe)>6 and len(mot_de_passe)<=9 :
    score +=1
elif len(mot_de_passe)>9 and len(mot_de_passe)<=12:
    score +=3
elif len(mot_de_passe)>=12:
    score +=5
    
#Ensuite on compte le nombre de caractere speciaux et on rajoutera un point a chaque caractere special en plus

special = sum(1 for char in mot_de_passe if char in string.punctuation)
score = score + special

#Compter le nombre de majuscule

majuscule = sum(1 for char in mot_de_passe if char in string.ascii_uppercase)

if majuscule == 0:
    score+=0
elif majuscule <= 2:
    score+=1
elif majuscule >= 3:
    score+=2

#ensuite on compte le nombre de chiffre :

chiffre = sum(1 for char in mot_de_passe if char.isdigit())
if chiffre == 0:
    score +=0
elif chiffre <=3:
    score +=1
elif chiffre > 3 and chiffre <=6:
    score += 3
elif chiffre > 6:
    score +=5
    
#On teste s'il existe des répétitions dans le mdp et on reduit le score en cas de repet

repet=0
for i in range(1,len(mot_de_passe)):
    if mot_de_passe[i] == mot_de_passe[i-1]:
        repet+=1
score=score-repet    

#On calcule le score :
if score <=4:
    print("le mot de passe est faible")
elif score > 4 and score <=8:
    print("le mot de passe est moyen")
elif score > 8:
    print("le mot de passe est fort")
    
print("")
print("Merci d'avoir utiliser PASS-checker")