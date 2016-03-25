#!/usr/bin/env python

from ai_engine import Player, AIEngine
import cmd


def display(board):
    """Displays a Tic Tac Toe board"""
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


class GameConsole(cmd.Cmd):

    board = ["", "", "", "", "", "", "", "", ""]

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '=> '

    def do_play(self, line):
        """
        Make a move.

        Usage: play <cell>

        The cell positions are as follows:

         0 | 1 | 2
        -----------
         3 | 4 | 5
        -----------
         6 | 7 | 8
        """
        self.board[int(line)] = Player.X

        engine = AIEngine(self.board)
        if engine.has_won(self.board, Player.X):
            display(self.board)
            print "You win!"
            self.do_EOF(line)

        comp_move = engine.best_move()
        self.board[comp_move] = Player.O

        if engine.has_won(self.board, Player.O):
            display(self.board)
            print "AI wins. Muhuhahaha!"
            print
            self.do_EOF(line)

        display(self.board)

    def emptyline(self):
        return True

    def do_EOF(self, line):
        raise SystemExit

    def precmd(self, line):
        print
        return cmd.Cmd.precmd(self, line)

    def postcmd(self, stop, line):
        print

    def postloop(self):
        print


if __name__ == '__main__':
    GameConsole().cmdloop("Minimalistic Tic Tac Toe")
