import unittest
import main


class TestMain(unittest.TestCase):
    def test_one_do_stuff(self):
        self.assertEqual(main.do_stuff(5), 3)

    def test_two_do_stuff(self):
        self.assertEqual(main.do_stuff('5'), 3)

    def test_three_do_stuff(self):
        self.assertEqual(main.do_stuff('umar'), 'Please enter a number.')

    def test_four_do_stuff(self):
        self.assertIsInstance(main.do_stuff(0), ZeroDivisionError)

    def test_five_do_stuff(self):
        self.assertEqual(main.do_stuff(''), 'Please enter a number.')


unittest.main()
