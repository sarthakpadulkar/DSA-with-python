import random

class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.map = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            return False

        self.map[val] = len(self.nums)
        self.nums.append(val)

        return True

    def remove(self, val):
        
        if val not in self.map:
            return False

        index = self.map[val]
        last_val = self.nums[-1]

        self.nums[index] = last_val
        self.map[last_val] = index

        self.nums.pop()
        del self.map[val]

        return True

    def getRandom(self):
       
        return random.choice(self.nums)
