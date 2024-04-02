# https://leetcode.com/problems/insert-delete-getrandom-o1

import random
class RandomizedSet:
    def __init__(self):
        self.theSet = dict()

    def insert(self, val: int) -> bool:
        if val in self.theSet:
            return False
        self.theSet[val] = True
        return True

    def remove(self, val: int) -> bool:
        if val not in self.theSet:
            return False
        self.theSet.pop(val)
        return True

    def getRandom(self) -> int:
        keys = list(self.theSet.keys())
        return random.choice(keys)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()