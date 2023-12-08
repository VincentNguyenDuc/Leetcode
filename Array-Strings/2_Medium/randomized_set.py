import random


class RandomizedSet:

    def __init__(self):
        self.indices_map = {}
        self.elems = []

    def __contains__(self, val: int) -> bool:
        """
        True if the set contains the item.
        """
        return val in self.indices_map

    def insert(self, val: int) -> bool:
        """
        Return true if value is not in the set,
        and we successfully insert value into the set
        """
        if val not in self:
            self.elems.append(val)
            self.indices_map[val] = len(self.elems) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Return true if value is in the set,
        and we successfully remove value from the set
        """
        if val in self:
            # swap the value that we need to delete, with the value at the end
            # of the list self.elems
            val_index = self.indices_map[val]
            last_index = len(self.elems) - 1
            self.indices_map[self.elems[last_index]] = val_index
            self.elems[val_index], self.elems[last_index] = self.elems[last_index], self.elems[val_index]
            
            # delete the that last item from both the indices map and the elems list
            self.indices_map.pop(self.elems.pop())
            return True
        return False

    def getRandom(self) -> int:
        random_index = random.randrange(0, len(self.elems))
        return self.elems[random_index]


if __name__ == "__main__":

    obj = RandomizedSet()
    param_1 = obj.insert(1)
    param_2 = obj.remove(1)
    obj.insert(2)
    obj.insert(5)
    param_3 = obj.getRandom()
    print(param_1, param_2, param_3)
