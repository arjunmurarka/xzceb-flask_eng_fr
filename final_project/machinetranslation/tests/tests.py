import unittest

from translator import english_to_french, french_to_english

class Test_englishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("hello"),"Bonjour")
        self.assertNotEqual(english_to_french('null'),'null')

class Test_frenchToEnglish(unittest.TestCase):        
    def test1(self): 
        self.assertEqual(french_to_english("bonjour"),"Hello") 
        self.assertNotEqual(french_to_english('null'),'null')

if __name__ == '__main__':
    unittest.main()
