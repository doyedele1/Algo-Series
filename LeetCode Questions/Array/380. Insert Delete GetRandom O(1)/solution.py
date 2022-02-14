import random

class RandomizedSet:
    def __init__(self):
        self.hash_map = dict()
        self.array_list = []
        
    def insert(self, val: int) -> bool:
        if val in self.hash_map: return False
        self.array_list.append(val)
        self.hash_map[val] = len(self.array_list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map: return False
        
        # extract the index of the value to be removed from the hash_map
        index = self.hash_map[val]
        
        # get the last element in the array list and copy the last element to the index
        self.array_list[index], self.array_list[-1] = self.array_list[-1], self.array_list[index]
        
        # update the last element index in the hash_map
        self.hash_map[self.array_list[index]] = index
        
        # remove the last element in the array_list and remove the entry containing the key equal to the value to be removed in the hash_map
        del self.hash_map[self.array_list.pop()]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.array_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()