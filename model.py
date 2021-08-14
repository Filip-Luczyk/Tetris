class Brick():			
	def __init__(self, number=0):
		self.x = 250
		self.y = 0
		self.number = number
		
		
	def Falling(self):
		self.y = self.y + 50

class Ruler():
	
	def __init__(self):
		self.objects_list = []
	
	def NewBrick(self):
		self.objects_list.append(Brick(len(self.objects_list)))
		
	#def ReturnPositions(self):
	#	for i in objects_list:
	
	def ShouldFall(self):
		self.x = self.objects_list[-1].x
		self.y = self.objects_list[-1].y
		for obj in range(len(self.objects_list) - 1):
			if obj.x == self.x:
				if obj.y == self.y:
					return False
		if self.y == 750:
			return False
		return True
					
	def Fall(self):
		if len(self.objects_list) == 0:
			self.NewBrick()
			
		if self.ShouldFall():
			self.objects_list[-1].Falling()
		else:
			self.NewBrick()
		print(self.ShouldFall())
		print(self.objects_list[0].y)
ruler = Ruler()			
ruler.Fall()
ruler.Fall()

print(ruler.objects_list[0].y)
