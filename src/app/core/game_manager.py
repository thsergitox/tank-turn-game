import pygame
from enum import Enum


class EPhase(Enum):
    MOVEMENT = 0
    AIM = 1
    SHOOT = 2
    WAITING_SHOOT = 3


TURN = 0
PHASE = EPhase.MOVEMENT
PLAYERS = []
KEY = None


class GameManager:
    def GetCurrPlayer(self):
        return PLAYERS[TURN]

    def NextPlayer(self):
        global TURN, PLAYERS
        TURN = (TURN + 1) % len(PLAYERS)
        PLAYERS[TURN].actual_movement = PLAYERS[TURN].movement
        return self.GetCurrPlayer()

    def AddPlayer(self, player):
        PLAYERS.append(player)

    def MovementPhase(self):
        # print(f"Player {TURN} moving")
        direction = KEY[pygame.K_RIGHT] - KEY[pygame.K_LEFT]

        PLAYERS[TURN].move(direction)

    def AimPhase(self):
        # print(f"Player {TURN} aiming")

        direction = KEY[pygame.K_RIGHT] - KEY[pygame.K_LEFT]

        PLAYERS[TURN].aim(direction)

    def ShootPhase(self, target):
        # print(f"Player {TURN} Shooting")
        PLAYERS[TURN].shoot(target)
        self.NextPhase()

    def Update(self):
        global KEY
        KEY = pygame.key.get_pressed()
        if PHASE == EPhase.MOVEMENT:
            self.MovementPhase()
        elif PHASE == EPhase.AIM:
            self.AimPhase()
        elif PHASE == EPhase.SHOOT:
            targetIndex = (TURN + 1) % len(PLAYERS)
            self.ShootPhase(PLAYERS[targetIndex])

        if self.check_win():
            # Do something when winning
            return

    # call it when bullet despawns
    def end_turn(self):
        global PHASE
        if PHASE == EPhase.WAITING_SHOOT:
            PHASE = EPhase.MOVEMENT
            self.NextPlayer()

    def NextPhase(self):
        global PHASE
        if PHASE == EPhase.WAITING_SHOOT:
            return
        PHASE = EPhase(PHASE.value + 1)
        print(f"Phase: {PHASE}")

    def check_win(self):
        alive = 0
        for player in PLAYERS:
            if player.is_alive:
                alive += 1
        if alive == 1:
            print(f"Player {TURN} wins!")
            return True
        return False
