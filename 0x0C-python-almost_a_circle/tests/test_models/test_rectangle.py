#!/usr/bin/python3


import unittest
import sys


sys.path.insert(0, '../../')


from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    
    def setUp(self):
        self.rectangle1 = Rectangle(1, 2)
        self.rectangle2 = Rectangle(2, 3, 2, 3, 22)
        self.rectangle3 = Rectangle(3, 2, 3, 2)

    def tearDown(self):
        Rectangle.reset_nb_objects()
        del self.rectangle1
        del self.rectangle2
        del self.rectangle3

    def test_id_set(self):
        self.assertEqual(self.rectangle1.id, 1)
        self.assertEqual(self.rectangle2.id, 22)
        self.assertEqual(self.rectangle3.id, 2)

    def test_instance_rectangle(self):
        self.assertIsInstance(self.rectangle1, Rectangle)
        self.assertIsInstance(self.rectangle2, Rectangle)
        self.assertIsInstance(self.rectangle3, Rectangle)

    def test_subclass_base(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_parameters_assigned(self):
        self.assertTrue(self.rectangle1.x == 0)
        self.assertTrue(self.rectangle1.width == 1)
        self.assertTrue(self.rectangle3.x == 3)

    def test_raises_error_bad_arguments(self):
        with self.assertRaises(TypeError) as result:
            rectangle = Rectangle(10, "2")
        self.assertEqual(str(result.exception), "height must be an integer")


if __name__ == '__main__':
    unittest.main()
