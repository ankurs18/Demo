from threading import Thread

class Mythread(Thread):
    
    def __init__(self, tname):
        Thread.__init__(self, name=tname)
        
    def run(self):
        print('Thread started', self.getName())
        
t1 = Mythread('T1')
t1.start()

t2 = Mythread('T2')
t2.start()

