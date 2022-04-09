import unittest

from star_wars import nave_estelar_cercana

class TestMision(unittest.TestCase):
    def test_true(self):
        self.assertEqual(nave_estelar_cercana([32638, 205, 258, 71115],250),True)
        self.assertEqual(nave_estelar_cercana([32638, 205, 258, 71115],280),True)
        self.assertEqual(nave_estelar_cercana([3],3),True)

    def test_false(self):
        self.assertEqual(nave_estelar_cercana([32638, 205, 258, 71115],4),False)
        self.assertEqual(nave_estelar_cercana([32638, 205, 258, 71115],1),False)
        self.assertEqual(nave_estelar_cercana([3],2),False)

unittest.main()

