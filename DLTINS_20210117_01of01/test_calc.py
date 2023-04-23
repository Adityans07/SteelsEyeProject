import unittest
import os

import Aditya_Raj_Data_Engineer
from Aditya_Raj_Data_Engineer import *

class MyTestCase(unittest.TestCase):
    def test_valid_xml_file(self):
        file = Aditya_Raj_Data_Engineer.get_root_xml()
        file_name = "DLTINS_20210117_01of01.xml"
        root = file.get_xml_root(file_name)
        self.assertNotEqual(root, None)


if __name__ == '__main__':
    unittest.main()
