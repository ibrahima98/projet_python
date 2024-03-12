'''
    cette classe permets de recuperer tout les données invalides et le stockers dans un liste ou dictionnaires 
    ceci pour le but de faire un archivage  

'''
import csv
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
with open("/workspaces/projet_python/src/Donnees_Projet_Python_Dev_Data.csv", 'r') as f:
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