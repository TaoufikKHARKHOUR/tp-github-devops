utilisateurs = []

def ajouter_utilisateur(nom, email):
    utilisateurs.append({"nom": nom, "email": email})
    return utilisateurs
# Mise à jour API
def lister_utilisateurs(): return utilisateurs
def supprimer_utilisateur(email): pass
