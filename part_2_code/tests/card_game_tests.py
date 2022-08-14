import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card_game = CardGame()
        self.card1 = Card("Hearts",1)
        self.card2 = Card("Spade", 3)
        self.card3 = Card("Hearts", 5)
        self.cards = [self.card1, self.card2, self.card3]
        
    
    def test_check_for_ace(self):
        self.assertTrue(self.card_game.check_for_ace(self.card1))
    
    def test_check_no_ace_is_false(self):
        self.assertFalse(self.card_game.check_for_ace(self.card2))
        
    def test_card3_is_higher_than_card2(self):
        self.assertEqual(self.card3, self.card_game.highest_card(self.card2, self.card3))
    
    def test_card2_is_not_higher_than_card3(self):
        self.assertNotEqual(self.card2, self.card_game.highest_card(self.card2, self.card3))
    
    def test_card_total(self):
        self.assertEqual("You have a total of 9", self.card_game.cards_total(self.cards) )