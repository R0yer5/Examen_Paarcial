import unittest
import Horizonte

class TestTrabajador(unittest.TestCase):
    def setUp(self):
        self.trabajador = Horizonte.Trabajador("Juan", 2000, 2, 15, 10)

    def test_calcular_bonificaciones(self):
        bonificaciones, remuneracion_computable = self.trabajador.calcular_bonificaciones()
        self.assertEqual(bonificaciones, 1185.0)
        self.assertEqual(remuneracion_computable, 3108.3333333333335)

    def test_calcular_descuentos(self):
        bonificaciones, remuneracion_computable = self.trabajador.calcular_bonificaciones()
        descuentos = self.trabajador.calcular_descuentos(bonificaciones, remuneracion_computable)
        self.assertEqual(descuentos, 207.1875)

    def test_calcular_sueldo_neto(self):
        sueldo_neto = self.trabajador.calcular_sueldo_neto()
        self.assertEqual(sueldo_neto, 2977.8125)

if __name__ == '__main__':
    unittest.main()
