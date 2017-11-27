import unittest
import _planets_database as pd
import json

class TestPlanetApi(unittest.TestCase):
        def load(self):
                self.planets = pd._planets_database()
                self.planets.load_planets('oec.csv')

        def reset_data(self):
                self.planets = {}
                self.load()
        # def is_json(self, resp):
        #         try:
        #                 json.loads(resp)
        #                 return True
        #         except ValueError:
        #                 return False

        def test_get_planet(self):
                self.reset_data()
                # First test
                # WASP-127 b,0,0.18,1.37,4.178062,0.052,,,,,88.7,,,
                # transit,2016,16/07/27,10 42 14,-03 09 54,,1.08,1.39,,5620,11.41
                # ,Confirmed planets
                key = 'WASP-127 b'
                # self.assertTrue(self.is_json(r.content.decode()))
                resp = self.planets.get_planet(key)
                resp = self.planets.get_planet(key)
                self.assertEqual(resp['mass'], '0.18')
                self.assertEqual(resp['radius'], '1.37')
                self.assertEqual(resp['period'], '4.178062')
                self.assertEqual(resp['visitors'], '2')
                # self.assertTrue(self.is_json(r.content.decode()))
                ## Made up planet
                key = 'this is definitely not a planet'
                resp = self.planets.get_planet(key)
                self.assertEqual(resp, None)

        def test_set_planet(self):
                self.reset_data()
                key = 'WASP-127 b'
                m = [''] * 25
                new_mass = "-5000"
                new_radius = "-500"
                new_period = "-50"
                new_vis = "-5"
                m[1] = new_mass
                m[2] = new_radius
                m[3] = new_period
                m[24] = new_vis
                self.planets.set_planet(key, m)
                resp = self.planets.get_planet(key)
                self.assertEqual(resp['mass'], new_mass)
                self.assertEqual(resp['radius'], new_radius)
                self.assertEqual(resp['period'], new_period)
                self.assertEqual(resp['visitors'], "-4")


        def test_planet_delete(self):
                self.reset_data()
                key = 'WASP-127 b'
                resp = self.planets.get_planet(key)
                self.assertEqual(resp['mass'], '0.18')
                self.planets.delete_planet(key)
                resp = self.planets.get_planet(key)
                self.assertEqual(resp, None)

        def test_planets_delete(self):
                self.reset_data()
                self.planets.delete_planets()
                self.assertEqual(len(self.planets.planets), 0)

        def test_scale_to_earth(self):
                self.reset_data()
                key = 'Kepler-452 b'
                ratio = self.planets.scale_to_earth(key)
                self.assertEqual(ratio, 19.33)



if __name__ == "__main__":
        unittest.main()