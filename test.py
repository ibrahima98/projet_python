'''
    essayons de manipuler les donnees du fichiers csv.
    importons le package csv et manipulons le fichier csv Donnees_Projet_Python_Dev_Data.csv
    parcourir chaque ligne ensuite affichers le resultats sous formats de dictionnaires
'''
import csv
import json 
donnees_tab = []

with open("Donnees_Projet_Python_Dev_Data.csv", newline='', encoding='utf-8') as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=",")

        for ligne in reader:  
                donnees_tab.append(ligne)
                numb = donnees_tab[0]
        print(json.dumps(numb, indent=3) )

