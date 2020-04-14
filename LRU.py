class LRU:

    def _init_(self):
        self.list = []

    def put(self):
        pass   
    def get(self):
        pass
    def getcache(self):
        pass    


class LRU_test:

    def _init_(self):
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
if__name__ == "__main__":
    main()
               






