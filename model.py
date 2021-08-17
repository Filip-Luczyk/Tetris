import random

class Brick():			
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def Falling(self):
		self.y = self.y + 50
	
	def MoveLeft(self):
		self.x = self.x - 50
		
	def MoveRight(self):
		self.x = self.x + 50

class Manager():
	
	def __init__(self):
		self.objects_list = []
		self.shape1 = [[(200,  -50), (0, 0), (50, 0), (0, 50), (50, 50)]]
		self.shape2 = [[(200, -150), (0, 0), (0, 50), (0, 100), (0, 150)], [(200, 0), (0, 0), (50, 0), (100, 0), (150, 0)]]	
		self.shape3 = [[(200, -50), (0, 0), (50, 0), (50, 50), (100, 50)], [(200, -100), (50, 0), (0, 50), (50, 50), (0, 100)]]
		self.shape4 = [[(200, -50), (50, 0), (100, 0), (0, 50), (50, 50)], [(200, -100), (0, 0), (0, 50), (50, 50), (50, 100)]]
		self.shape5 = [[(200, -100), (0, 0), (0, 50), (50, 50), (0, 100)], [(200, -50), (0, 0), (50, 0), (100, 0), (50, 50)],
		[(200, -100), (50, 0), (0, 50), (50, 50), (50, 100)], [(200, -50), (50, 0), (0, 50), (50, 50), (100, 50)]]
		self.shape6 = [[(200, -100), (0, 0), (0, 50), (0, 100), (50, 100)], [(200, -50), (0, 0), (50, 0), (100, 0), (0, 50)],
		[(200, -100), (0, 0), (50, 0), (50, 50), (50, 100)], [(200, -50), (100, 0), (0, 50), (50, 50), (100, 50)]]
		self.shape7 = [[(200, -100), (50, 0), (50, 50), (0, 100), (50, 100)], [(200, -50), (0, 0), (0, 50), (50, 50), (100, 50)],
		[(200, -100), (0, 0), (50, 0), (0, 50), (0, 100)], [(200, -50), (0, 0), (50, 0), (100, 0), (100, 50)]] 
		self.shapes = [self.shape1, self.shape2, self.shape3, self.shape4, self.shape5, self.shape6, self.shape7]
		self.reference_coordinate_x = 0
		self.reference_coordinate_y = 0
		
	def NewShape(self):
		self.shape = random.choice(self.shapes)
		self.shape = random.choice(self.shape)
		for i in range(1, 5):
			self.reference_coordinate_x = self.shape[0][0]
			self.reference_coordinate_y = self.shape[0][1]
			self.x = self.reference_coordinate_x + self.shape[i][0]
			self.y = self.reference_coordinate_y + self.shape[i][1]
			self.objects_list.append(Brick(self.x, self.y))		
	
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
			self.NewShape()
			
		if self.ShouldFall():
			self.objects_list[-1].Falling()
			self.objects_list[-2].Falling()
			self.objects_list[-3].Falling()
			self.objects_list[-4].Falling()
			self.reference_coordinate_y = self.reference_coordinate_y + 50
		else:
			self.NewShape()
			
	def MoveLeft(self):
		if self.objects_list[-1].x > 0:
			self.objects_list[-1].MoveLeft()
			self.objects_list[-2].MoveLeft()
			self.objects_list[-3].MoveLeft()
			self.objects_list[-4].MoveLeft()
			self.reference_coordinate_x = self.reference_coordinate_x - 50
	
	def MoveRight(self):
		if self.objects_list[-1].x < 450:
			self.objects_list[-1].MoveRight()
			self.objects_list[-2].MoveRight()
			self.objects_list[-3].MoveRight()
			self.objects_list[-4].MoveRight()
			self.reference_coordinate_y = self.reference_coordinate_y + 50
			
	def GetPositions(self):
		list_to_return = []
		for obj in self.objects_list:
			list_to_return.append((obj.x, obj.y))
		return list_to_return

Manage = Manager() #This object is to be imported
Manage.NewShape()
