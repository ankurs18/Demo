from contextlib import contextmanager

@contextmanager
def formattedOp(char):
    print(char * 30)
    yield
    print(char * 30)
    
with formattedOp('-') : print('Welcome to decorators')   

@contextmanager
def fileOpener(path):
    try:
        fh = open(path, 'w')
        yield fh
    finally:
        fh.close() 
    
with fileOpener('test3.txt') as fobj : fobj.write('Using context manager')