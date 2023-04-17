#!/usr/bin/python3


import unittest
import sys


sys.path.insert(0, '../../')


from models.base import Base


class TestBaseClass(unittest.TestCase):
    
    def setUp(self):
        self.base1 = Base()
        self.base2 = Base(22)
        self.base3 = Base()

    def tearDown(self):
        del self.base1
        del self.base2
        del self.base3

    def test_id_set(self):
        print(self.base3.id)
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 22)
        self.assertEqual(self.base3.id, 2)

    def test_instance_base(self):
        self.assertIsInstance(self.base1, Base)
        self.assertIsInstance(self.base2, Base)
        self.assertIsInstance(self.base3, Base)


if __name__ == '__main__':
    unittest.main()
