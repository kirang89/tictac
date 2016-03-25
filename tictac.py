#!/usr/bin/env python


import cmd


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

        engine = Engine(self.board)
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
    # display(board=["", "", "", "", "", "", "", "", ""])
    GameConsole().cmdloop("Minimalistic Tic Tac Toe")
