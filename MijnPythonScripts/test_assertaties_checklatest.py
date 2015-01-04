#-*- coding: utf8 -*-

import assertaties
import unittest

class TestGemiddelde(unittest.TestCase):

    def setUp(self): 
        self.usecase1 = [5]
        self.usecase2 = [6,8]
        self.usecase3 = [6,7,14]
        self.usecase4 = []
        self.usecase5 = [6,'z',14]
        pass

    def test_usecase1(self):
        res = assertaties.gemiddelde(*self.usecase1)
        self.assertEqual(res, 5)

    def test_usecase2(self):
        res = assertaties.gemiddelde(*self.usecase2)
        self.assertEqual(res, 7)

    def test_usecase3(self):
        res = assertaties.gemiddelde(*self.usecase3)
        self.assertEqual(res, 9)

    def test_usecase4(self):
        res = assertaties.gemiddelde(*self.usecase4)
        self.assertEqual(res, None)
        
    def test_usecase5(self):
        try:
          assertaties.gemiddelde(*self.usecase5)
        except TypeError as e:
            assert str(e) == "'z' is geen geheel getal"

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
