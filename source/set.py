from source.hashtable import HashTable


class Set(object):

    def __init__(self, elements=None):
        """ Initialize a new empty set structure, and add
        each element if a sequence is given """
        self.size = 0
        self.table = HashTable()
        for element in elements:
            self.add(element)

    def __str__(self):
        return str(self.table.keys())

    def contains(self, element):
        """ Return a boolean indicating whether element is in set"""
        return self.table.contains(element)

    def add(self, element):
        """ add element in this set, if not present already """
        if self.contains(element):
            return None
        self.table.set(element, None)

    def remove(self, element):
        """ Remove element from this set, if present, or else raise KeyError """
        self.table.delete(element)

    def union(self, other_set):
        """ Return a new set that is a union of this set and other_set """
        set_new = Set(self.table.keys())
        for key in other_set.table.keys():
            set_new.add(key)
        return set_new

    def intersection(self, other_set):
        """ Return a new set that is the intersection of this set and other_set """
        lt = list()
        for key in other_set.table.keys():
            if self.contains(key):
                lt.append(key)
        return Set(lt)

    def difference(self, other_set):
        """ Return a new set that is the difference of this set and other_set """
        lt = list()
        for key in other_set.table.keys():      # All keys in other set
            if self.contains(key):
                continue
            else:
                lt.append(key)

        for key in self.table.keys():           # All keys in other set
            if other_set.contains(key):
                continue
            else:
                lt.append(key)
        return Set(lt)

    def is_subset(self, other_set):
        """ Return a boolean indicating whether other_set is a subset of this set """
        for key in self.table.keys():
            if other_set.contains(key) is False:
                return False
        return True


items_A = Set([1, 2, 3, 4, 5, 6, 7])
items_B = Set([1])
print(items_A.is_subset(items_B))






