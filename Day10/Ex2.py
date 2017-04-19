import unittest

class FileUtil():
    
    def __init__(self):
        self.fh = None
        
    def readFile(self):
        self.fh=open('test.txt', 'r')
        return self.fh.read()
    
    def closingFh(self):
        self.fh.close()
        
#---------------------   

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.fh=FileUtil()
    
    def tearDown(self):
        self.fh= None
        
    def testReadFile(self):
        pass
    
if __name__=='__main__':
    unittest.main()      