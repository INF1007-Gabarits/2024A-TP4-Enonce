from constants import *

class Arena:
    # TODO: Ajouter un attribut statique pour stocker les joueurs

    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2
        # TODO: Ajouter les joueurs à la liste des joueurs de l'arène
        pass

    # TODO: Ajouter un destructeur qui réinitialise les joueurs et les retire de la liste des joueurs de l'arène

    """
    Méthode pour faire combattre les joueurs jusqu'à ce qu'un des joueurs n'ait plus de points de vie
    ou que les deux joueurs ne puissent plus attaquer

    Returns:
        None
    """
    def fight(self):
        # TODO: Faire attaquer au tour par tour les joueurs jusqu'à ce que l'un d'eux n'ait plus de points de vie
        # ou que les deux joueurs ne puissent plus attaquer

        # TODO: Afficher que le combat est terminé et réinitialiser les joueurs
        pass

    # TODO: Ajouter une méthode statique pour obtenir le nombre de joueurs
    """
    Méthode statique pour obtenir le nombre de joueurs

    Returns:
        int: Le nombre de joueurs
    """
