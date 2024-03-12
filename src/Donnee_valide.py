'''
    recuperer tout les données valides et le stocker dans un liste contenant des dictionnaires et se servir de ce fichiers pour faire 
    le traitements des données 
'''
'''import csv

def numero(number):
  return number.isalnum() and len(number) ==7 and number.isupper()

donnees_valide = []

with open("/workspaces/projet_python/src/chantillons_Donnees.csv") as fichier_csv:
    donnees = csv.DictReader(fichier_csv, dialect='unix')
    for ligne in donnees:
        if numero(ligne["Nom"]):
            donnees_valide.append(ligne)

# Affichage des données valides une fois après avoir parcouru toutes les lignes
print(donnees_valide)'''

import csv
import csv
import datetime
"""def gestion_notes(notes):
    s_notes = notes.split("#")
    new = str(s_notes)
    new = new.split("[]")
    return new

with open('/home/adama/Documents/Project_Python_Dev1/Donnees_Projet_Python_Dev_Data.csv', 'r') as f:
    # Créer un lecteur CSV qui permet de lire ligne par ligne le fichier
    lecteur = csv.DictReader(f, dialect='unix')

    # Lecture par ligne et vérification de la validité des données
    # Lecture par ligne et vérification de la validité des données
    for ligne in lecteur:
        n_notes = gestion_notes(ligne['Note'])
        ligne['Note'] = n_notes
        print(ligne['Note'])
"""

'''def format_classe(classe):
    classe.strip()
    if classe[0].isdigit() and classe:
        classe.replace("i", "")
        nouvelle_classe = classe[0:2] + "e" + classe[4:]


'''
def number(num):
    """
    Fonction qui permet de verifier la validité
        * Le Numéro doit contenir des lettres en majuscules et des chiffres
        * Le numéro doit avoir une longueur de 7 (len(num) == 7)
    param: 
        num : le numero à vérifier
    """
    """
    Function that verifies the validity
    * The number must contain uppercase letters and digits
    * The number must have a length of 7 (len(num) == 7)
    param:
    num : the number to be checked
    """
    return num.isalnum() and len(num) == 7 and num.isupper()
valide = []
invalide = []
# Ouvrir le fichier en mode lecture et le lire
with open('/workspaces/projet_python/src/chantillons_Donnees.csv', 'r') as f:
    # Créer un lecteur CSV qui permet de lire ligne par ligne le fichier
    lecteur = csv.DictReader(f, dialect='unix')

    # Lecture par ligne et vérification de la validité des données
    for ligne in lecteur:
        if number(ligne['Numero']) :
            # Formater la date correctement
        
                valide.append(ligne)
           
        else:
            # Si la date n'est pas valide, ajouter la ligne à la liste des invalides
            invalide.append(ligne)

print("Les données valides: ")
print(valide, end="\n"*3)
print(invalide, end="\n"*3)



