class LRU:

    def __init__(self):
        self.list = []

    def put(self,a):
        self.list.append(a)   
    def get(self):
        return self.list.pop()
        
    def getcache(self):
        return self.list    


    
class LRU_test:

    def __init__(self):
        self.toy = LRU()
        self.total = 0

    def test_put(self):
        self.toy.put(3)
        try:
            assert self.toy.list == [3]
            self.total = self.total+1
        except Exception as e:
            print("failput")    

    def test_get(self):
        value = self.toy.get()

        try:
            assert self.toy.list == []
            self.total = self.total+1
        except Exception as e:
            print("failget")    
        
    def test_getcache(self):
        newvalue = self.toy.getcache()

        try:
            assert self.toy.list == newvalue
            self.total = self.total+1
        except Exception as e:
            print("failgetcache")  


def main():
    box = LRU_test()
    box.test_put()
    box.test_get()
    box.test_getcache()
    if box.total == 3:
        print("All test cases are passed")
if __name__ == "__main__":
    main()
               





