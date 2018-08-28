import unittest
from application.DataBase.DataBase import DataBase
 
class TestDataBase(unittest.TestCase):
    def setUp(self):
        self.data_base = DataBase()
 
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test_add(self):

        #Test integers
        self.data_base.add(1)
        
        self.assertEqual(self.data_base.elements[0], 1)
        self.assertEqual(self.data_base.number_of_elements, 1)
        
        #Test string
        self.data_base.add("a")
        
        self.assertEqual(self.data_base.elements[1], "a")
        self.assertEqual(self.data_base.number_of_elements, 2)
        
        #Test dictionarry
        test_dict = {"test": 2}
        
        self.data_base.add(test_dict)
        
        self.assertDictEqual(self.data_base.elements[2], test_dict)
        self.assertEqual(self.data_base.number_of_elements, 3)
        
    def test_remove(self):
        #Test integers
        self.data_base.add(1)
        
        
        #Test string
        self.data_base.add("a")
                
        #Test dictionarry
        test_dict = {"test": 2}
        
        self.data_base.add(test_dict)
        
        self.data_base.remove("b")
        self.assertEqual(self.data_base.number_of_elements, 3)
        
        self.data_base.remove("a")
        self.assertEqual(self.data_base.number_of_elements, 2)
        
        self.data_base.remove(test_dict)
        self.assertEqual(self.data_base.number_of_elements, 1)
        
        self.data_base.remove(1)
        self.assertEqual(self.data_base.number_of_elements, 0)
        
        self.data_base.remove(1)
        self.assertEqual(self.data_base.number_of_elements, 0)

            
         
    def test_get_number_of_elements(self):
        
        self.assertEqual(self.data_base.get_number_of_elements(), 0)
        
        #Test integers
        self.data_base.add(1)
        
        self.assertEqual(self.data_base.get_number_of_elements(), 1)
        
        #Test string
        self.data_base.add("a")
        
        self.assertEqual(self.data_base.get_number_of_elements(), 2)
        
        #Test dictionarry
        test_dict = {"test": 2}
        
        self.data_base.add(test_dict)
        
        self.assertEqual(self.data_base.get_number_of_elements(), 3)


    def test_find_elements(self):
        
        self.assertFalse(self.data_base.find_elements(1))
        
        #Test integers
        self.data_base.add(1)
        
        self.assertTrue(self.data_base.find_elements(1))
        
        #Test string
        self.data_base.add("a")
        
        self.assertTrue(self.data_base.find_elements("a"))
        
        #Test dictionarry
        test_dict = {"test": 2}
        
        self.data_base.add(test_dict)
        
        self.assertTrue(self.data_base.find_elements(test_dict))
        
        self.assertFalse(self.data_base.find_elements(7))      
        
        self.data_base.add(1)
        self.assertEqual((self.data_base.find_elements(1)).get_elements(), [1, 1])
        
        
    def test_str(self):
        
        self.assertFalse(self.data_base.find_elements(1))
        
        #Test integers
        self.data_base.add(1)
        
        self.assertEqual(str(self.data_base), "1")
        
        #Test string
        self.data_base.add("a")
        
        self.assertEqual(str(self.data_base), "1\r\na")
        
        #Test dictionarry
        test_dict = {"test": 2}
        
        self.data_base.add(test_dict)
        
        self.assertEqual(str(self.data_base), "1\r\na\r\n" + str(test_dict))
        
    def test_get_elements(self):
        
        test_elements = [1 , "a", {"test": 2}]
        
        self.data_base.add(test_elements[0])
        
        self.assertEqual(self.data_base.get_elements(), test_elements[0:1])
        
        self.data_base.add(test_elements[1])
        
        self.assertEqual(self.data_base.get_elements(), test_elements[0:2])
        
        self.data_base.add(test_elements[2])
        
        self.assertEqual(self.data_base.get_elements(), test_elements)
        
        self.data_base.remove(1)
        
        self.assertEqual(self.data_base.get_elements(), test_elements[1:3])       
         
if __name__ == '__main__':
    unittest.main()