import utils as u
import unittest
from worldModel import ItemCreation, World, NotExistItemCreation
API_VERSION = 10

class TestWorldCreation(unittest.TestCase):
    
    def setUp(self): #Before
        self.beatrix = ItemCreation("Beatrix", u.createPowerLvl(), "[/]", u.createUid(), "[\]")
        self.samael = ItemCreation("Samael", u.createPowerLvl(), "Arcangel", u.createUid(), "Fire and Shadows")
        self.world = World("Nivel IV")    
        self.world.creations  = u.createListCreatures()
        self.world.add_creation(self.beatrix)
    def tearDown(self): #After
        pass

    def test_checkPowerBeatrix(self):
        assert self.beatrix.power > 0

    def test_checkNameBeatrix(self):
        self.assertEqual(self.beatrix.name, "Beatrix")

    def test_checkNameBellia(self):
        self.assertNotEqual(self.beatrix.name, "Bellia")

    def test_worldContainsCreations(self):
        self.assertTrue(self.world.contains_creations())
    
    def test_worldNotContainsCreations(self):
        self.world.creations = []
        self.assertFalse(self.world.contains_creations())

    def test_obtenerBeatrix(self):
        item = self.world.get_creation(self.beatrix)
        self.assertIs(item, self.beatrix)
        self.assertIsNot(item, self.samael)

    def test_samaelnotexist(self):
        with self.assertRaises(NotExistItemCreation):
            self.world.get_creation(self.samael)

    def test_correctcodefirst(self):
        # print(self.world.creations[0])
        self.assertRegex(self.world.creations[0].uid, "XID")

    def test_failCreation(self):
        total = len(self.world.creations)
        print("TOTAL: "+str(total))
        if total < 11:
            self.fail("No se han creado todos")

    @unittest.skip("Skipped porque la propiedad no existe.")
    def test_takePowers(self):
        for power in self.beatrix.powers:
            print(power)

    @unittest.skipIf(API_VERSION>=10, "Se omite por la version de la api") #Se skippea si es true
    # @unitest.skipUnless(False, "Se skippea si el resultado es false")
    def test_samael(self):
        print(self.samael)


    def test_showall(self):
        for c in self.world.creations:
            print(c)

if __name__ == '__main__':
    unittest.main()