import unittest

def add(x,y):
    return  x-y

class AddTest(unittest.TestCase):
    
    def testAdd(self):
        self.assertEqual(-20, add(40, 60))
        
if __name__=='__main__':
    unittest.main()        