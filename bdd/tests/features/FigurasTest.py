'''
Jared
Erick Raul Ibarra Perez 
'''
import unittest
from fig import Figuras


class FiguraTest (unittest.TestCase):

    def setUp(self):
        self.fig=Figuras()


    def test_calcular_circulo(self):
        self.fig.calcular_area_circulo(10)
        self.assertEqual(98.69604401089359, self.fig.get_area())

    def test_cuadrado(self):
        self.fig.calcular_area_cuadrado(5)
        self.assertEqual(25, self.fig.get_area())

    def test_rectangulo(self):
        self.fig.calcular_area_rectangulo(10,5)
        self.assertEqual(50, self.fig.get_area())

    def test_trapecio(self):
        self.fig.calcular_area_trapecio(3, 4, 5.0)
        self.assertEqual(13.5, self.fig.get_area())
if __name__ == '__main__':
    unittest.main()


