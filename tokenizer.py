import random
import hashlib
from uuid import uuid4

class Tokenizer():
    def __init__(self):
        self.id = uuid4()
        print ("[INFO] Tokenizer Inizialized")
    def getToken(self):
        k = uuid4()
        k1 = str(k)
        key = hashlib.md5(k1.encode()).hexdigest()
        return str(key)
    def changeId(self):
        self.id = uuid4()
        return True
