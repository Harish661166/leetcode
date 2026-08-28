import random
class RandomizedSet:

    def __init__(self):
        self.list=[]
        self.map={}

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val]=len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            i=self.map[val]
            self.map[self.list[-1]]=i
            del self.map[val]
            self.list[i]=self.list[-1]
            self.list.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()