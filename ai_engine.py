from operator import itemgetter


class Player:
    X = 'X'
    O = 'O'


class Engine(object):

    def __init__(self, board, player=Player.O):
        self.board, self.player = board, player

    def best_move(self):
        return max(self.gen_move(), key=itemgetter(1))[0]

    def gen_move(self):
        moves = []
        for cell in self.empty_cells(self.board):
            b = list(self.board)
            b[cell] = self.player

            moves.append(
                (cell, self.minimax(b, self.opponent(self.player)))
            )

        return moves

    def minimax(self, board, player):
        empty_cells = self.empty_cells(board)
        score = self.get_score(board)

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

            scores.append(self.minimax(b, self.opponent(player)))

        if player == self.player:
            return max(scores)
        else:
            return min(scores)

    def empty_cells(self, board):
        return [i for i, c in enumerate(board)
                if c not in [Player.X, Player.O]]

    def opponent(self, player):
        if player == Player.X:
            return Player.O
        else:
            return Player.X

    def has_won(self, board, player):
        rows = [board[0:3], board[3:6], board[6:9]]
        cols = zip(board[0:3], board[3:6], board[6:9])
        diagonals = [board[0:9:4], board[2:7:2]]

        row_win = any(all(a == player for a in c) for c in rows)
        col_win = any(all(a == player for a in c) for c in cols)
        diag_win = any(all(a == player for a in c) for c in diagonals)

        return row_win or col_win or diag_win

    def has_two_in_line(self, board, player):
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

    def game_over(self, board):
        all_filled = all(c != '' for c in board)
        return self.has_won(board, Player.X) or \
            self.has_won(board, Player.O) or \
            all_filled

    def get_score(self, board):
        opp = self.opponent(self.player)
        win = self.has_won(board, self.player)
        has_two_in_line = self.has_two_in_line(board, self.player)
        opp_win = self.has_won(board, opp)
        opp_has_two_in_line = self.has_two_in_line(board, opp)

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


def display(board):
    rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    width = 3
    for i, row in enumerate(rows):
        s = ''
        for idx, col in enumerate(row):
            value = board[col] if board[col] != '' else ' '
            s += value.center(width)
            if idx != len(row) - 1:
                s += '|'

        print s
        if i != len(rows) - 1:
            print '-' * (width * 3 + 2)