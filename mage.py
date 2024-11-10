from character import Character
from weapon import Weapon
from constants import *

class Mage(Character):
    def __init__(self, name):
        # TODO: Appeller le constructeur de la classe mère
        # TODO: Ajouter un attribut 'mana' initialisé à MAGE_MANA disponible dans le fichier constants.py
        # TODO: Ajouter un attribut 'weapon' initialisé à une nouvelle instance de Weapon avec les paramètres appropriés 
        # disponibles dans le fichier constants.py
        pass

    """
    Méthode pour attaquer un autre personnage, consomme de la mana

    Args:
        other_character (Character): Personnage à attaquer
    """
    def attack(self, other_character):
        # TODO: Vérifier si le personnage a assez de mana pour attaquer
        
        # TODO: Appeller la méthode attack de la classe mère
        pass

    """
    Méthode pour vérifier si le personnage peut attaquer

    Returns:
        bool: True si le personnage peut attaquer, False sinon
    """
    def can_attack(self):
        # TODO: Vérifier si le personnage peut attaquer et si le personnage a assez de mana
        pass

    # TODO: Implementer la méthode reset
    # Cette méthode doit appeller le constructeur
    
    # TODO: Implementer la méthode say_hello pour afficher un message personnalisé pour chaque type de personnage
    # Le message personnalisé peut être celui de votre choix