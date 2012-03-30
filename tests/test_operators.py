from unittest import TestCase
import operators

class OperatorsTests(TestCase):
    def test_add(self):
        self.assertEquals(operators.add(2,3),5)
