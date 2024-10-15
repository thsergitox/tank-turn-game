import pygame


class GameMannager:
    turn = 0
    phase = 0
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
        direction = 0
        if self.key[pygame.K_LEFT]:
            direction = -1
        elif self.key[pygame.K_RIGHT]:
            direction = 1

        self.players[self.turn].move(direction)

    def AimPhase(self):
        # print(f"Player {self.turn} aiming")

        direction = 0
        if self.key[pygame.K_LEFT]:
            direction = -1
        elif self.key[pygame.K_RIGHT]:
            direction = 1

        self.players[self.turn].aim(direction)

    def ShootPhase(self):
        # print(f"Player {self.turn} Shooting")
        self.players[self.turn].shoot()

    def Update(self):
        self.key = pygame.key.get_pressed()
        if self.phase == 0:
            self.MovementPhase()
        elif self.phase == 1:
            self.AimPhase()
        elif self.phase == 2:
            self.ShootPhase()

    def NextPhase(self):
        self.phase += 1
        if self.phase > 2:
            self.phase = 0
            self.NextPlayer()
