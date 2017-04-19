class Box():
    
    def __init__(self, length, width, height):
        self.length = length
        self.height = height
        self.width = width
        
    def calVol(self):
        return self.length * self.height * self.width
    
    def __add__(self, otherbox):
        return self.calVol() + otherbox.calVol()
    
        
box1 = Box(2, 3, 4)
box2 = Box(3, 4, 5)
box3 = box1 + box2 #or box1.add(box2)
print(box3)        