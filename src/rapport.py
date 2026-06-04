from app import calculer_imc
from src.api import utilisateurs

def generer_rapport():
    nb = len(utilisateurs)
    return {
        "total_utilisateurs": nb,
        "version": "1.1.0",
        "statut": "actif"
    }
