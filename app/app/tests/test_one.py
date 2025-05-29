from django.test import SimpleTestCase

from app import calc


class Calc_Test(SimpleTestCase):

    def test_calc(self):
        res = calc.add_numbers(5, 6)

        self.assertEquals(res, 11)
