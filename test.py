'''
    essayons de manipuler les donnees du fichiers csv.
    importons le package csv et manipulons le fichier csv Donnees_Projet_Python_Dev_Data.csv
    parcourir chaque ligne ensuite affichers le resultats sous formats de dictionnaires
'''
import csv
import json 


with open("Donnees_Projet_Python_Dev_Data.csv", newline='', encoding='utf-8') as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=",")
        for ligne in reader:  
                print(json.dumps(ligne, indent=3) )

