import random

class RandomizedCollection(object):

    def __init__(self):
        self.nums = []
        self.map = {}

    def insert(self, val):
       
        if val not in self.map:
            self.map[val] = set()

        self.map[val].add(len(self.nums))
        self.nums.append(val)

        return len(self.map[val]) == 1

    def remove(self, val):
       
        if val not in self.map or not self.map[val]:
            return False

        index = self.map[val].pop()
        last_val = self.nums[-1]
        last_index = len(self.nums) - 1

        if index != last_index:
            self.nums[index] = last_val

            self.map[last_val].remove(last_index)
            self.map[last_val].add(index)

        self.nums.pop()

        if not self.map[val]:
            del self.map[val]

        return True

    def getRandom(self):
       
        return random.choice(self.nums)
