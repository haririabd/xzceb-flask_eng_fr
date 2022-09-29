import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
    def test2(self): 
        self.assertEqual(englishToFrench("My name is Hariri, I live in Malaysia"), "Mon nom est Hariri, je vis en Malaisie")
    def test3(self): 
        self.assertNotEqual(englishToFrench("None"), '')

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
    def test2(self): 
        self.assertNotEqual(frenchToEnglish(0), 0)
    def test3(self):
        self.assertNotEqual(frenchToEnglish("None"), '')

unittest.main()
