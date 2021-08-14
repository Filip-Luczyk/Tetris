class Brick():			
	def __init__(self, number=0):
		self.x = 250
		self.y = 0
		
	def Falling(self):
		self.y = self.y + 50


class Manager():
	
	def __init__(self):
		self.objects_list = []
	
	def NewBrick(self):
		self.objects_list.append(Brick(len(self.objects_list)))
	
	def ShouldFall(self):
		self.x = self.objects_list[-1].x
		self.y = self.objects_list[-1].y
		self.last_object = self.objects_list.pop()
		for obj in self.objects_list:
			if obj.x == self.x:
				if obj.y == self.y + 50:
					self.objects_list.append(self.last_object)
					return False
		if self.y == 750:
			self.objects_list.append(self.last_object)
			return False
		self.objects_list.append(self.last_object)
		return True
					
	def Fall(self):
		if len(self.objects_list) == 0:
			self.NewBrick()
			
		if self.ShouldFall():
			self.objects_list[-1].Falling()
		else:
			self.NewBrick()
	
	def GetPositions(self):
		list_to_return = []
		for obj in self.objects_list:
			list_to_return.append((obj.x, obj.y))
		print(list_to_return)
		return list_to_return

Manage = Manager() #This object is to be imported

