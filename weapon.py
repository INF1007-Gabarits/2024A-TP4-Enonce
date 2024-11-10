import random

class Weapon:
    """
    Constructeur de la classe Weapon

    Args:
        name (str): Nom de l'arme
        damage (int): Dégats infligés par l'arme
        durability (int): Durabilité de l'arme
        hit_chance (float) [0.0-1.0]: Chance de toucher l'adversaire
    """
    def __init__(self, name, damage, durability, hit_chance):
        self._name = name
        self._damage = damage
        self._durability = durability
        self._hit_chance = hit_chance

    """
    Méthode pour utiliser l'arme
    Perds 1 point de durabilité à chaque utilisation
    Returns:
        bool: True si le coup a touché et si elle a assez de durabilité, False sinon
    """
    def use(self):
        # TODO: Implémenter la méthode pour utiliser l'arme
        pass

    # TODO: Ajouter des getters pour les attributs name, damage et durability
    
    # TODO: Ajouter une surcharge de l'opérateur str pour afficher le nom et les dégats de l'arme
