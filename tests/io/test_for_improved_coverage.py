import unittest
import os
import topyc.io.Map as Map
import topyc.io.Config as Conf


class TestDumb(unittest.TestCase):
    def test_map(self):
        m = Map.Map({'first_name': 'Eduardo'}, last_name='Pool',
                    age=24, sports=['Soccer'])

        self.assertEqual(m.sports, ['Soccer'])

    def test_config(self):
        cf = Conf.Config()

        self.assertEqual(cf.os, os.name)
        self.assertGreaterEqual(len(cf.sections()), 2)
        self.assertTrue(os.path.exists(cf.path_research_root))

        subsection = cf.paths_research
        keys = [key for key in subsection]
        self.assertGreaterEqual(len(keys), 3)
