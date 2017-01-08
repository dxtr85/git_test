#!/usr/bin/python

import unittest
from mock import MagicMock as MM
from mock import patch
import sys, mock

b_mock = MM()
orig_import = __import__
def import_mock(name, *args):
    print('importing %s\n'%name)
    if name == 'test':
        return b_mock
    return orig_import(name, *args)

class TestStringMethods(unittest.TestCase):

    def test_funkcja(self):
            sys.modules['test'] = MM()
            from test2 import funkcja
            funkcja()
            
    def test_xml(self):
        XML = '''<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
'''
        import xml.etree.ElementTree as ET
        from mock import patch, mock_open
        
        with patch("__builtin__.open", mock_open(read_data=XML)) as mock_file:
            tree = ET.parse('country_data.xml')
            root = tree.getroot()
            print('root: %s' %root.tag)
            for child in root:
                print child.tag, child.attrib
        
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
