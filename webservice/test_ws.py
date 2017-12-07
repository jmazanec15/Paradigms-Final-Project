import unittest
import json
import requests

class TestPlanetApi(unittest.TestCase):
        def load(self):
                self.url = 'http://student04.cse.nd.edu:51020/planets/'

        def reset_data(self):
                self.url = 'http://student04.cse.nd.edu:51020/planets/'
                requests.post(self.url + 'reset')
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
                r = requests.get(self.url + key)
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['mass'], '0.18')
                self.assertEqual(resp['radius'], '1.37')
                self.assertEqual(resp['period'], '4.178062')
                self.assertEqual(resp['visitors'], '1')
                # self.assertTrue(self.is_json(r.content.decode()))
                ## Made up planet
                key = 'this is definitely not a planet'
                r = requests.get(self.url + key)
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'error')
        def test_get(self):
                self.reset_data()
                r = requests.get(self.url)
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['planets']['WASP-127 b']['mass'], '0.18')
                self.assertEqual(resp['planets']['WASP-127 b']['radius'], '1.37')
                self.assertEqual(resp['planets']['WASP-127 b']['period'], '4.178062')
                self.assertEqual(resp['planets']['WASP-127 b']['visitors'], '0')


        def test_set_planet(self):
                self.reset_data()
                key = 'WASP-127 b'
                m = dict()
                new_mass = "-5000"
                new_radius = "-500"
                new_period = "-50"
                new_vis = "-5"
                m['mass'] = new_mass
                m['radius'] = new_radius
                m['period'] = new_period
                m['visitors'] = new_vis
                r = requests.put(self.url + key , data =json.dumps(m))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.get(self.url + key)
                resp = json.loads(r.content.decode())

                self.assertEqual(resp['mass'], new_mass)
                self.assertEqual(resp['radius'], new_radius)
                self.assertEqual(resp['period'], new_period)
                self.assertEqual(resp['visitors'], "-4")


        def test_planet_delete(self):
                self.reset_data()
                key = 'WASP-127 b'
                r = requests.get(self.url + key)
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['mass'], '0.18')

                r= requests.delete(self.url + key)
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'],'success')


                r = requests.get(self.url + key)
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'error')

        def test_planets_delete(self):
                self.reset_data()
                r= requests.delete(self.url)
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'],'success')

                key = 'WASP-127 b'
                r = requests.get(self.url + key)
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'error')

        def test_scale_to_earth(self):
                self.reset_data()
                key = 'Kepler-452 b'

                r = requests.get(self.url + 'scaled/'+key)
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['scaled_to_earth'], 19.33)



if __name__ == "__main__":
        unittest.main()