from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, hp, max_hp):
        self._name = name
        self._hp = hp
        self._max_hp = max_hp
        self._weapon = None

    """
    Méthode pour attaquer un autre personnage

    Args:
        other_character (Character): Personnage à attaquer

    Returns:
        None
    """
    def attack(self, other_character):
        # TODO: Vérifier si l'arme est cassée ou si le personnage est mort
        # TODO: Utiliser l'arme pour attaquer l'autre personnage (Appeller la méthode use de l'arme)
        # TODO: Afficher un message pour indiquer les dégats infligés
        pass

    """
    Méthode pour vérifier si le personnage peut attaquer

    Returns:
        bool: True si le personnage peut attaquer, False sinon
    """
    def can_attack(self):
        # TODO: Vérifier si l'arme a assez de durabilité pour attaquer
        pass

    # TODO: Ajouter une méthode abstraite 'reset' pour réinitialiser le personnage
    # TODO: Cette méthode a pour but d'appeller le constructuer afin de "réinitialiser" le personnage
    """
    Méthode pour réinitialiser le personnage

    Returns:
        None
    """
    

    # TODO: Ajouter une méthode abstraite 'say_hello' pour afficher un message personnalisé pour chaque type de personnage
    """
    Méthode pour afficher un message personnalisé pour chaque type de personnage

    Returns:
        None
    """
    

    # TODO: Ajouter une méthode pour vérifier si le personnage est en vie (points de vie supérieurs à 0)
    """
    Méthode pour vérifier si le personnage est en vie

    Returns:
        bool: True si le personnage est en vie, False sinon
    """
    

    # TODO: Ajouter des getters et setters pour les attributs name, hp et weapon

    # TODO: Ajouter une surcharge de l'opérateur str pour afficher le nom et les points de vie du personnage