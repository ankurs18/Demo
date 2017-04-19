from threading import Thread
class Resource():
    
    def produceNum(self, i):
        self.num = i
    def consumeNum(self):
        pass

class Consumer(Thread):
    def __init__(self, res):
        Thread.__init__(self)
        self.res = res
    
    def run(self):
       for i in [11,22,33,44,55]:
           self.res.consumeNum()
        
class Producer(Thread):
    def __init__(self, res):
        Thread.__init__(self)
        self.res = res
    
    def run(self):
       for i in range(5):
           self.res.produceNum(i)
        
res = Resource()
producer = Producer(res)
consumer = Consumer(res)
consumer.start()
producer.start()

