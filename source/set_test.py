
from source.set import Set
import unittest

class SetTest(unittest.TestCase):


    def test_contains(self):
        s = Set(['A, B, C'])
        assert s.contains('A') == True
        assert s.size == 1
        assert s.contains('B') == True
        assert s.size == 2
        assert s.contains('C') == True
        assert s.size == 3
        assert s.contains('D') == False
        assert s.size == 3

    def test_add(self):
        s = Set()
        pass

    def test_remove(self):
        s = Set()
        pass

    def test_union(self):
        s = Set()
        pass

    def test_intersection(self):
        s = Set()
        pass

    def test_difference(self):
        s = Set()
        pass

    def test_is_subset(self):
        s = Set()
        pass


if __name__ == '__main__':
    unittest.main()

