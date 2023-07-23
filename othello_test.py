import unittest

from othello import Player, Othello

class TestOthello(unittest.TestCase):
    def test_player_attributes(self):
        player = Player("Alice", "black")
        self.assertEqual(player.get_name(), "Alice")
        self.assertEqual(player._piece_color, "black")
        self.assertEqual(player.get_taken_tiles(), [])

        player.add_taken_tiles("(3, 4)") 
        player.add_taken_tiles("(5, 6)")
        self.assertEqual(player.get_taken_tiles(), ["(3, 4)", "(5, 6)"])

    def test_othello_game(self):
        game = Othello()

        game.create_player("Alice", "black")
        game.create_player("Bob", "white")

        # Testing the starting board state
        self.assertEqual(game._board[4][4], "O")
        self.assertEqual(game._board[4][5], "X")
        self.assertEqual(game._board[5][4], "X")
        self.assertEqual(game._board[5][5], "O")

        # Test invalid move
        self.assertEqual(game.play_game("black", "(4, 4)"), "Invalid move")

        # Test a valid move
        game.play_game("black", "(3, 4)")
        self.assertEqual(game._board[3][4], "X")

if __name__ == "__main__":
    unittest.main()