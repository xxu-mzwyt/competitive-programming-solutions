# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed

class RandomizedCollection:
    def __init__(self):
        self.theSet = []

    def insert(self, val: int) -> bool:
        isPresent = val in self.theSet
        self.theSet.append(val)
        return not isPresent

    def remove(self, val: int) -> bool:
        isPresent = val in self.theSet
        if isPresent:
            self.theSet.remove(val)
        return isPresent

    def getRandom(self) -> int:
        return random.choice(self.theSet)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()