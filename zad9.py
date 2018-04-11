import unittest


class Prostokat:
    def __init__(self, bok_a: [float, int],
                 bok_b: [float, int]) -> None:
        if not isinstance(bok_a, (float, int)) or not \
                isinstance(bok_b, (float, int)):
            raise TypeError

        if bok_a <= 0 or bok_b <= 0:
            raise ValueError
        self.bok_a = bok_a
        self.bok_b = bok_b

    def pole(self):
        return self.bok_b * self.bok_a

    def obwod(self):
        return 2 * (self.bok_a + self.bok_b)

    def __str__(self):
        return f'Prostokąt(a={self.bok_a}, b={self.bok_b})'

class ProstokatTest(unittest.TestCase):


    def setUp(self):
        self.prostokat = Prostokat(2, 3)

    def test_tworzenia_nieprawidlowego_prostokata(self):
        with self.assertRaises(ValueError):
            Prostokat(0, 1)
        with self.assertRaises(ValueError):
            Prostokat(0, -1)
        with self.assertRaises(TypeError):
            Prostokat([0, 9])
        with self.assertRaises(TypeError):
            Prostokat([0, 9], [9, 8])

    def test_tworzenia_prostokata(self):
        self.prostokat = Prostokat(2, 3)
        self.assertEqual(self.prostokat.bok_a, 2)
        self.assertEqual(self.prostokat.bok_b, 3)

    def test_pola(self):
        self.assertEqual(self.prostokat.pole(), 6)

    def test_obwodu(self):
        self.assertEqual(self.prostokat.obwod(), 10)

    def test_prostokat_to_string(self):
        self.assertEqual(str(self.prostokat), 'Prostokąt(a=2, b=3)')


if __name__ == '__main__':
     unittest.main()