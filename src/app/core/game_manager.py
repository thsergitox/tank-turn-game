import pygame
from enum import Enum


class EPhase(Enum):
    MOVEMENT = 0
    AIM = 1
    SHOOT = 2
    WAITING_SHOOT = 3


class GameManager:
    turn = 0
    phase = EPhase.MOVEMENT
    players = []
    key = None

    def GetCurrPlayer(self):
        return self.players[self.turn]

    def NextPlayer(self):
        self.turn = (self.turn + 1) % len(self.players)
        self.players[self.turn].actual_movement = self.players[self.turn].movement
        return self.GetCurrPlayer()

    def AddPlayer(self, player):
        self.players.append(player)

    def MovementPhase(self):
        # print(f"Player {self.turn} moving")
        direction = self.key[pygame.K_RIGHT] - self.key[pygame.K_LEFT]

        self.players[self.turn].move(direction)

    def AimPhase(self):
        # print(f"Player {self.turn} aiming")

        direction = self.key[pygame.K_RIGHT] - self.key[pygame.K_LEFT]

        self.players[self.turn].aim(direction)

    def ShootPhase(self):
        # print(f"Player {self.turn} Shooting")
        self.players[self.turn].shoot()
        self.NextPhase()

    def Update(self):
        self.key = pygame.key.get_pressed()
        if self.phase == EPhase.MOVEMENT:
            self.MovementPhase()
        elif self.phase == EPhase.AIM:
            self.AimPhase()
        elif self.phase == EPhase.SHOOT:
            self.ShootPhase()

    # call it when bullet despawns
    def end_turn(self):
        self.NextPlayer()
        self.phase = EPhase.MOVEMENT

    def NextPhase(self):
        if self.phase == EPhase.WAITING_SHOOT:
            return
        self.phase = EPhase(self.phase.value + 1)
