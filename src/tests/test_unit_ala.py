import unittest
from oxrse_unit_conv.units import ala, candela


class TestAla(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(ala.si_unit.matches(candela))

    def test_basic_conversion(self):
        self.assertEqual(ala.to_si(1), 1000)


if __name__ == '__main__':
    unittest.main()