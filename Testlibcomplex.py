import unittest
import Libcomplex as lc

class TestCplx(unittest.TestCase):

    def test_cplxsum(self):
        suma = lc.sumacplx((3,4),(-4,6.7))
        self.assertAlmostEqual(suma,(-1,10.7))

    def test_restacplx(self):
        resta = lc.restacplx((3, 2), (-5,6.4))
        self.assertAlmostEqual(resta[0], 8)
        self.assertAlmostEqual(resta[1], -4.4)

    def test_multicplx(self):
        producto = lc.multicplx((4, 5), (-5, 5.8))
        self.assertAlmostEqual(producto[0], -49)
        self.assertAlmostEqual(producto[1], -1.8)

    def test_divcplx(self):
        division = lc.divcplx((3,8,2),(-7,5.5))
        self.assertAlmostEqual(division[0], 0)
        self.assertAlmostEqual(division[1], -1)

    def test_modulocplx(self):
        modulo = lc.modulocplx((3),(-6.7))
        self.assertAlmostEqual(modulo, 16)

    def test_conjugadocplx(self):
        conjugado = lc.conjugadocplx((3),(-7.2))
        self.assertAlmostEqual(conjugado[0], 3)
        self.assertAlmostEqual(conjugado[1], 7.2)

    def test_conversptoccplx(self):
        conversion = lc.conversptoccplx(2,-75)
        self.assertAlmostEqual(conversion[0], 1)
        self.assertAlmostEqual(conversion[1], -2)

    def test_conversctopcplx(self):
        conversion = lc.conversctopcplx((3*((3)**(1/2))),(3))
        self.assertAlmostEqual(conversion[0], 6)
        self.assertAlmostEqual(conversion[1], 30)

    def test_fasecplx(self):
        fase = lc.fasecplx((3),(-5.2))
        self.assertAlmostEqual(fase, 420)

        fase2 = lc.fasecplx(-1, -1)
        self.assertAlmostEqual(fase2, 225)



if __name__ == '__main__':
    unittest.main()