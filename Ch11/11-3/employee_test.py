import unittest
from employee import Employee as em

class TestEmployeeClass(unittest.TestCase):
    """Tests for the employee class"""

    def setUp(self):
        """ Create employees with different raises """
        first_name = "Doe"
        last_name = "John"
        anual_salary = 100000
        self.custom_raise_ammount = 7000
        self.john_doe = em(first_name, last_name, anual_salary)
        self.default_raise = 105000
        self.custom_raise = 107000

    def test_default_raise(self):
        """Test defau;t raise"""
        self.john_doe.give_raise()
        self.assertEqual(self.john_doe.give_raise(), self.default_raise)

    def test_custom_raise(self):
        """Test custom raise"""
        self.john_doe.give_raise(self.custom_raise)
        self.assertEqual(self.john_doe.give_raise(self.custom_raise_ammount), self.custom_raise)

if __name__ == '__main__':
    unittest.main()