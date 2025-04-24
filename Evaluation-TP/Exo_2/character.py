import logging
import random

log = logging.getLogger(__name__)


class CharacterError(Exception):
    pass


class Character: 
    def __init__(self, name: str, life: float = 100.0, attack: float = 20.0, defense: float = 0.1): # Question 1
        self._name = name
        self._life = life
        self._attack = attack
        self._defense = defense

    def take_damages(self, damage_value: float): # Question 2
        actual_damage = damage_value * (1 - self._defense)
        self._life -= actual_damage
        if self._life < 0:
            self._life = 0

    def attack(self, target): # Question 3
        damage = self._attack
        target.take_damages(damage)

    def __str__(self): # Question 4
        return f"{self._name} <{self._life:.3f}>"

    @property
    def name(self): # Question 5
        return self._name

    @property
    def is_dead(self): # Question 6
        return self._life <= 0


class Weapon:
    def __init__(self, name: str, attack: float): # Question 7
        self._name = name
        self.attack = attack

    @classmethod
    def default(cls): # Question 8
        return cls("Wood stick", 1.0)

    @property
    def name(self): # Question 9
        return self._name


class Warrior(Character):
    def __init__(self, name: str, weapon: Weapon = None): # Question 10
        base_life = 100 * 1.5
        base_defense = 0.1 * 1.2
        super().__init__(name, life=base_life, defense=base_defense)
        self.weapon = weapon if weapon is not None else Weapon.default()

    def attack(self, target):
        damage = self._attack + self.weapon.attack
        if self.is_raging:
            damage *= 1.2
        target.take_damages(damage)

    @property
    def is_raging(self): # Question 11
        return self._life < (100 * 1.5 * 0.2)


class Magician(Character):
    def __init__(self, name: str): # Question 13
        base_life = 100 * 0.8
        base_attack = 20 * 2
        super().__init__(name, life=base_life, attack=base_attack)

    def _activate_magical_shield(self) -> bool: # Question 14
        return random.randint(1, 3) == 1  # 1 chance sur 3

    def take_damages(self, damage_value: float): # Question 15
        if self._activate_magical_shield():
            log.debug(f"{self._name} activated magical shield!")
            return
        super().take_damages(damage_value)