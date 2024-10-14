
class GameMannager():
	turn = 0
	phase = 0
	players = []

	def GetCurrPlayer(self):
		return self.players[self.turn]
	
	def NextPlayer(self):
		self.turn = (self.turn + 1) % len(self.players)
		return self.GetCurrPlayer()
	
	def AddPlayer(self, player):
		self.players.append(player)

	def MovementPhase(self):
		self.players[self.turn].Move()

	def AttackPhase(self):
		pass
		self.players[self.turn].Attack()

	def Update(self):
		if(self.phase == 0):
			self.MovementPhase()
		elif(self.phase == 1):
			self.AttackPhase()
	
	def NextPhase(self):
		self.phase += 1
		if(self.phase > 1):
			self.phase = 0
			self.NextPlayer()
		