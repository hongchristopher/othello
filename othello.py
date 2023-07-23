class Player:
    """Class used to represent each player. Has methods for initialization and has attributes for player name, piece
    color, and taken tiles. Has necessary get and set methods.
    """
    def __init__(self, name, piece_color):
        self._player_name = name
        self._piece_color = piece_color
        self._taken_tiles = []

    def get_taken_tiles(self):
        return self._taken_tiles

    def set_taken_tiles(self, updated_tiles):
        self._taken_tiles = updated_tiles

    def add_taken_tiles(self, tile):
        self._taken_tiles.append(tile)

    def get_name(self):
        return self._player_name

class Othello:
    """Othello class to be used to play Othello. Utilizes player objects. Has methods make_board, print_board,
    create_player, update_pieces, return_available_positions, return_winner, make_move, and play_game. Moves are made
    with the play_game method with arguments for player color and desired position.
    """
    def __init__(self):
        self._board = self.make_board()
        self._player_black = None
        self._player_white = None

    def make_board(self):
        """Method used to create the board that Othello will be played on. Outputs a 2d list. Called upon
        initialization. Takes no parameters, returns an empty board.
        """
        board = []
        star_list = []
        for index in range(0, 10):
            star_list.append("*")

        period_list = ["*"]
        for index in range(0, 8):
            period_list.append(".")
        period_list.append("*")

        middle_row_1 = ["*", ".", ".", ".", "O", "X", ".", ".", ".", "*"]
        middle_row_2 = ["*", ".", ".", ".", "X", "O", ".", ".", ".", "*"]

        board.append(list(star_list))
        for index in range(0, 3):
            board.append(list(period_list))
        board.append(middle_row_1)
        board.append(middle_row_2)
        for index in range(0, 3):
            board.append(list(period_list))
        board.append(list(star_list))
        return board

    def create_player(self, player_name, color):
        """Creates player objects 1 and 2 that will act as the 2 players that will play Othello. Interacts with the
        play_game method. Takes no parameters, returns a list of two player objects.
        """
        if color == "black":
            self._player_black = Player(player_name, color)
            self._player_black.add_taken_tiles("(4, 5)")
            self._player_black.add_taken_tiles("(5, 4)")
        if color == "white":
            self._player_white = Player(player_name, color)
            self._player_white.add_taken_tiles("(4, 4)")
            self._player_white.add_taken_tiles("(5, 5)")

    def print_board(self):
        """Prints the current board with player positions. To be called at the start of the game, after the make_move
        method is called, and after the game ends. Takes no parameters, returns nothing.
        """
        for row in self._board:
            print(row)

    def add_parentheses(self, string):
        """Takes an argument for a string, adds parentheses to both ends."""
        return "(" + string + ")"

    def return_available_positions(self, color):
        """Method that returns a list of possible positions for the player of given a color. Takes an argument for
        player color, returns a list of available positions. Utilizes player objects to determine currently taken
        tiles.
        """
        available_positions = []
        if color == "black":
            tiles = self._player_black.get_taken_tiles()
            opponent_piece = "O"
        if color == "white":
            tiles = self._player_white.get_taken_tiles()
            opponent_piece = "X"

        for tile in tiles:
            # self._board[int(tile[0])][int(tile[1])]      returns "x", manipulating the first index for vertical
            #                                              movement and the second for horizontal movement
            index = 1
            while self._board[int(tile[1])][int(tile[4]) + index] == opponent_piece:  # checking to the right
                index += 1
                if self._board[int(tile[1])][int(tile[4]) + index] == ".":  # here
                    available_positions.append((int(tile[1]), (int(tile[4])) + index))

            index = 1
            while self._board[int(tile[1])][int(tile[4]) - index] == opponent_piece:  # checking to the left
                index += 1
                if self._board[int(tile[1])][int(tile[4]) - index] == ".":
                    available_positions.append((int(tile[1]),(int(tile[4])) - index))

            index = 1
            while self._board[int(tile[1]) - index][int(tile[4])] == opponent_piece:  # checking upwards
                index += 1
                if self._board[int(tile[1]) - index][int(tile[4])] == ".":
                    available_positions.append((int(tile[1]) - index, int(tile[4])))

            index = 1
            while self._board[int(tile[1]) + index][int(tile[4])] == opponent_piece:  # checking downwards
                index += 1
                if self._board[int(tile[1]) + index][int(tile[4])] == ".":
                    available_positions.append((int(tile[1]) + index, int(tile[4])))

            index = 1
            while self._board[int(tile[1]) - index][int(tile[4]) + index] == opponent_piece:  # checking upper-right
                index += 1
                if self._board[int(tile[1]) - index][int(tile[4]) + index] == ".":
                    available_positions.append((int(tile[1]) - index, int(tile[4]) + index))

            index = 1
            while self._board[int(tile[1]) - index][int(tile[4]) - index] == opponent_piece:  # checking upper-left
                index += 1
                if self._board[int(tile[1]) - index][int(tile[4]) - index] == ".":
                    available_positions.append((int(tile[1]) - index, int(tile[4]) - index))

            index = 1
            while self._board[int(tile[1]) + index][int(tile[4]) + index] == opponent_piece:  # checking lower-right
                index += 1
                if self._board[int(tile[1]) + index][int(tile[4]) + index] == ".":
                    available_positions.append((int(tile[1]) + index, int(tile[4]) + index))

            index = 1
            while self._board[int(tile[1]) + index][int(tile[4]) - index] == opponent_piece:  # checking lower-left
                index += 1
                if self._board[int(tile[1]) + index][int(tile[4]) - index] == ".":
                    available_positions.append((int(tile[1]) + index, int(tile[4]) - index))
            available_positions.sort()
        return available_positions

    def make_move(self, color, piece_position):
        """Takes arguments for player color and desired position. Returns available_positions if available positions is
        [], 'invalid move' if the desired position is not in the available move list, or makes the desired
        move. Interacts with the return_available_positions, and play_game methods.
        """
        piece_position = str(piece_position)
        available_positions = []
        available_positions_int = self.return_available_positions(color)
        for position in available_positions_int:
            available_positions.append(str(position))

        if not available_positions:
            return available_positions

        if piece_position not in available_positions:
            return "invalid move"

        if color == "black":
            piece = "X"
            opponent_piece = "O"
        if color == "white":
            piece = "O"
            opponent_piece = "X"

        if piece_position in available_positions:
            self._board[int(piece_position[1])][int(piece_position[4])] = piece
            tile = piece_position

            index = 1
            while self._board[int(tile[1])][int(tile[4]) + index] == opponent_piece:  # swapping right pieces
                index += 1
                if self._board[int(tile[1])][int(tile[4]) + index] == piece:
                    index_2 = 1
                    while index_2 != index:
                        self._board[int(tile[1])][int(tile[4]) + index_2] = piece
                        index_2 += 1

            index = 1
            while self._board[int(tile[1])][int(tile[4]) - index] == opponent_piece:  # swapping left pieces
                index += 1
                if self._board[int(tile[1])][int(tile[4]) - index] == piece:
                    index_2 = 1
                    while index_2 != index:
                        self._board[int(tile[1])][int(tile[4]) - index_2] = piece
                        index_2 += 1

            index = 1
            while self._board[int(tile[1]) - index][int(tile[4])] == opponent_piece:  # swapping upward pieces
                index += 1
                if self._board[int(tile[1]) - index][int(tile[4])] == piece:
                    index_2 = 1
                    while index_2 != index:
                        self._board[int(tile[1]) - index_2][int(tile[4])] = piece
                        index_2 += 1

            index = 1
            while self._board[int(tile[1]) + index][int(tile[4])] == opponent_piece:  # swapping downward pieces
                index += 1
                if self._board[int(tile[1]) + index][int(tile[4])] == piece:
                    index_2 = 1
                    while index_2 != index:
                        self._board[int(tile[1]) + index_2][int(tile[4])] = piece
                        index_2 += 1

            index = 1
            while self._board[int(tile[1]) - index][int(tile[4]) + index] == opponent_piece:  # swapping upper-right pieces
                index += 1
                if self._board[int(tile[1]) - index][int(tile[4]) + index] == piece:
                    index_2 = 1
                    while index_2 != index:
                        self._board[int(tile[1]) - index_2][int(tile[4]) + index_2] = piece
                        index_2 += 1

            index = 1
            while self._board[int(tile[1]) - index][int(tile[4]) - index] == opponent_piece:  # swapping upper-left pieces
                index += 1
                if self._board[int(tile[1]) - index][int(tile[4]) - index] == piece:
                    index_2 = 1
                    while index_2 != index:
                        self._board[int(tile[1]) - index_2][int(tile[4]) - index_2] = piece
                        index_2 += 1

            index = 1
            while self._board[int(tile[1]) + index][int(tile[4]) + index] == opponent_piece:  # swapping lower-right pieces
                index += 1
                if self._board[int(tile[1]) + index][int(tile[4]) + index] == piece:
                    index_2 = 1
                    while index_2 != index:
                        self._board[int(tile[1]) + index_2][int(tile[4]) + index_2] = piece
                        index_2 += 1

            index = 1
            while self._board[int(tile[1]) + index][int(tile[4]) - index] == opponent_piece:  # swapping lower-left pieces
                index += 1
                if self._board[int(tile[1]) + index][int(tile[4]) - index] == piece:
                    index_2 = 1
                    while index_2 != index:
                        self._board[int(tile[1]) + index_2][int(tile[4]) - index_2] = piece
                        index_2 += 1

        self.update_pieces()
        return self._board

    def update_pieces(self):
        """When called updates the amount of pieces both players have. Also determines if the game has ended and,
        if this is the case, prints a message and calls the return_winner method. Takes no arguments and returns
        nothing.
        """
        pieces_black = []
        pieces_white = []
        row_counter = 0
        game_end_counter = 64
        for row in self._board:
            tile_counter = 0
            for tile in row:
                if self._board[row_counter][tile_counter] == 'X':
                    pieces_black.append(self.add_parentheses(str(row_counter) + ', ' + str(tile_counter)))
                if self._board[row_counter][tile_counter] == 'O':
                    pieces_white.append(self.add_parentheses(str(row_counter) + ', ' + str(tile_counter)))
                if self._board[row_counter][tile_counter] == '.':
                    game_end_counter -= 1
                tile_counter += 1
            row_counter += 1
        self._player_black.set_taken_tiles(pieces_black)
        self._player_white.set_taken_tiles(pieces_white)
        if game_end_counter == 0:
            print(
                "Game is ended white piece : " + self._player_white.get_taken_tiles() + " black piece:" + self._player_black.get_taken_tiles())
            print(self.return_winner())

    def return_winner(self):
        """Determines the winner of the game and returns a message for the users. Used in the update_pieces method.
        Takes no arguments and returns the desired message.
        """
        tiles_white = self._player_white.get_taken_tiles()
        tiles_black = self._player_black.get_taken_tiles()
        if tiles_white > tiles_black:
            return "Winner is white player: " + self._player_white.get_name
        if tiles_black > tiles_white:
            return "Winner is black player: " + self._player_black.get_name
        if tiles_black == tiles_white:
            return "It's a tie"

    def play_game(self, player_color, piece_position):
        """Used to play the game. Takes arguments for player color and piece position to, if legal, make the necessary
        move and, if not legal, return an appropriate message.
        """
        piece_position = str(piece_position)
        val = self.make_move(player_color, piece_position)
        if val == "invalid move":
            print("Here are the valid moves:")
            print(self.return_available_positions(player_color))
            return "Invalid move"
        if not val:
            print(self.return_available_positions(player_color))
            return self.return_available_positions(player_color)
        else:
            return val
        