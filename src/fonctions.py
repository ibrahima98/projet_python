'''
    creation de tout les fonctions qui permette de verifier les validités 

'''

def numero(number):
  return number.isalnum() and len(number) ==7 and number.isupper()

def nom(nom):
  return nom[0].isalpha() and len(nom) >= 2

def prenom(prenom):
  return prenom[0].isalpha() and len(prenom) >= 3




