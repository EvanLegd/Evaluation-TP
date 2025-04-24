import logging
import random

from character import Character

log = logging.getLogger(__name__)


class FightSimulator:

    def __init__(self, fighters: list[Character]):
        if len(fighters) < 2:
            raise AttributeError(f"Number of fighters to small: {fighters}")

        self._fighters = fighters
        self._round = 0
        self.print_state()

    def play_round(self):
        self._round += 1

        shuffled_fighters = random.sample(self._fighters, k=len(self._fighters))
        log.debug(f"Round order: {shuffled_fighters}")

        for attacker in shuffled_fighters:
            if attacker.is_dead:
                continue

            for defender in shuffled_fighters:
                if attacker == defender:
                    # attacker doesn't attack itself
                    continue

                if defender.is_dead:
                    continue

                attacker.attack(defender)

    @property
    def is_fight_over(self) -> bool:
        number_of_living_fighters = 0
        for fighter in self._fighters:
            if not fighter.is_dead:
                number_of_living_fighters += 1

        return number_of_living_fighters <= 1

    def print_state(self):
        print(f"Round: {self._round}")
        for fighter in self._fighters:
            print(fighter)

        print("-----")

    def print_end_game(self):
        if self.is_fight_over:

            winner = None
            for fighter in self._fighters:
                if not fighter.is_dead:
                    winner = fighter

            if winner:
                print(f"{winner.name} has won the battle!")

            else:
                print("No one has won the fight...")

        else:
            print("Fight has been interrupted")

    def run(self):

        keep_playing = True

        while keep_playing:

            player_input = input('Press "enter" to play next round or "e" to exit game: ')
            if player_input == "e":
                keep_playing = False

            self.play_round()

            if self.is_fight_over:
                keep_playing = False

            self.print_state()

        self.print_end_game()
