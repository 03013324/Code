import unittest
import IF97

shuju1=[0.0010021516796866943,115.3312730214384,112.32481798237833,0.39229479240262427,4.173012184067783,1507.7392096690312]
shuju2=[0.0009711808940216297,184.14282773425438,106.44835621252402,0.36856385239848066,4.010089869646331,1634.6905431116586]
shuju3=[0.001202418003378339,975.5422390972251,971.9349850870901,2.58041912005181,4.6558068221112086,1240.7133731017252]

class Volume(unittest.TestCase):
    def test_Volume1(self):
        self.assertEqual(IF97.Volume(3, 300),shuju1[0])
    def test_Volume2(self):
        self.assertEqual(IF97.Volume(80, 300),shuju2[0])
    def test_Volume3(self):
        self.assertEqual(IF97.Volume(3, 500),shuju3[0])

class Enthalpy(unittest.TestCase):  
    def test_Enthalpy1(self):
        self.assertEqual(IF97.Enthalpy(3, 300),shuju1[1])
    def test_Enthalpy2(self):
        self.assertEqual(IF97.Enthalpy(80, 300),shuju2[1])     
    def test_Enthalpy3(self):
        self.assertEqual(IF97.Enthalpy(3, 500),shuju3[1])   

class InternalEnergy(unittest.TestCase):  
    def test_InternalEnergy1(self):
        self.assertEqual(IF97.InternalEnergy(3, 300),shuju1[2])
    def test_InternalEnergy2(self):
        self.assertEqual(IF97.InternalEnergy(80, 300),shuju2[2])
    def test_InternalEnergy3(self):
        self.assertEqual(IF97.InternalEnergy(3, 500),shuju3[2])
 
class Entropy(unittest.TestCase):
    def test_Entropy1(self):
        self.assertEqual(IF97.Entropy(3, 300),shuju1[3])
    def test_Entropy2(self):
        self.assertEqual(IF97.Entropy(80, 300),shuju2[3])
    def test_Entropy3(self):
        self.assertEqual(IF97.Entropy(3, 500),shuju3[3])

class IHCapacity(unittest.TestCase): 
    def test_IHCapacity1(self):
        self.assertEqual(IF97.IHCapacity(3, 300),shuju1[4])
    def test_IHCapacity2(self):
        self.assertEqual(IF97.IHCapacity(80, 300),shuju2[4])
    def test_IHCapacity3(self):
        self.assertEqual(IF97.IHCapacity(3, 500),shuju3[4])

class Sound(unittest.TestCase):
    def test_Sound1(self):
        self.assertEqual(IF97.Sound(3, 300),shuju1[5])
    def test_Sound2(self):
        self.assertEqual(IF97.Sound(80, 300),shuju2[5])
    def test_Sound3(self):
        self.assertEqual(IF97.Sound(3, 500),shuju3[5])

class Buchong_BE3a(unittest.TestCase):
    def test_Buchong_BE3a1(self):
        self.assertEqual(IF97.Buchong_BE3a(50, 2000),690.5721252159439)
    def test_Buchong_BE3a2(self):
        self.assertEqual(IF97.Buchong_BE3a(100,2100),733.9305075450569)
    
class Buchong_BE3b(unittest.TestCase):
    def test_Buchong_BE3b1(self):
        self.assertEqual(IF97.buchong_BE3b(50,2400),735.1848617922307)
    def test_Buchong_BE3b2(self):
        self.assertEqual(IF97.buchong_BE3b(100,2700),842.046087633262)


def suitetext():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Volume))
    suite.addTest(unittest.makeSuite(Enthalpy))
    suite.addTest(unittest.makeSuite(InternalEnergy))
    suite.addTest(unittest.makeSuite(Entropy))
    suite.addTest(unittest.makeSuite(IHCapacity))
    suite.addTest(unittest.makeSuite(Sound))
    suite.addTest(unittest.makeSuite(Buchong_BE3a))
    suite.addTest(unittest.makeSuite(Buchong_BE3a))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suitetext')

