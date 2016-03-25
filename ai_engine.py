from operator import itemgetter


class Player:
    X = 'X'
    O = 'O'


class AIEngine(object):

    def __init__(self, board, player=Player.O):
        self.board, self.player = board, player

    def has_won(self, board, player):
        rows = [board[0:3], board[3:6], board[6:9]]
        cols = zip(board[0:3], board[3:6], board[6:9])
        diagonals = [board[0:9:4], board[2:7:2]]

        row_win = any(all(a == player for a in c) for c in rows)
        col_win = any(all(a == player for a in c) for c in cols)
        diag_win = any(all(a == player for a in c) for c in diagonals)

        return row_win or col_win or diag_win

    def best_move(self):
        moves = []
        for cell in self.__empty_cells(self.board):
            b = list(self.board)
            b[cell] = self.player

            moves.append(
                (cell, self.__minimax(b, self.__opponent(self.player)))
            )

        # Return cell representing best move
        return max(moves, key=itemgetter(1))[0]

    def __minimax(self, board, player):
        empty_cells = self.__empty_cells(board)
        score = self.__get_score(board)

        if score == 0:
            # Check for draw
            if len(empty_cells) == 0:
                return score
        else:
            return score

        scores = []
        for cell in empty_cells:
            b = list(board)
            b[cell] = player

            scores.append(self.__minimax(b, self.__opponent(player)))

        if player == self.player:
            return max(scores)
        else:
            return min(scores)

    def __empty_cells(self, board):
        return [i for i, c in enumerate(board)
                if c not in [Player.X, Player.O]]

    def __opponent(self, player):
        if player == Player.X:
            return Player.O
        else:
            return Player.X

    def __has_two_in_line(self, board, player):
        rows = [board[0:3], board[3:6], board[6:9]]
        cols = zip(board[0:3], board[3:6], board[6:9])
        diagonals = [board[0:9:4], board[2:7:2]]
        combinations = rows + cols + diagonals

        for c1, c2, c3 in combinations:
            one_empty_cell = (c1 == '' or c2 == '' or c3 == '')
            two_equal_cells = (c1 == player and c2 == player) or \
                              (c2 == player and c3 == player) or \
                              (c1 == player and c3 == player)

            if one_empty_cell and two_equal_cells:
                return True

        return False

    def __get_score(self, board):
        opp = self.__opponent(self.player)
        win = self.has_won(board, self.player)
        has_two_in_line = self.__has_two_in_line(board, self.player)
        opp_win = self.has_won(board, opp)
        opp_has_two_in_line = self.__has_two_in_line(board, opp)

        score = 0
        if win:
            score += 100
        if has_two_in_line:
            score += 10
        if opp_win:
            score -= 100
        if opp_has_two_in_line:
            score -= 10

        return score
