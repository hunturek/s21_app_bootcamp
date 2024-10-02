from collections import Counter
import itertools

coop = True
cheat = False

draw = 2
lose = -1
win = 1
brake = 0


class Game(object):
    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()
        
    def rules(self):
        print("1. Каждый играет с каждым\n \
            2. В начале каждой игры двоим играющим выдаётся по 10 конфет\n \
            3. ")

    def play(self, player1, player2):
        player1.distrust = False
        player2.distrust = False
        for match_num in range(self.matches):
            res1 = player1.play(match_num)
            res2 = player2.play(match_num)
            if res1 and res2:
                player1.draw_game()
                player2.draw_game()
                # print("draw game")
            elif res1 and not res2:
                player1.lose_game()
                player2.win_game()
                # print(player2, "win game")
            elif not res1 and res2:
                player1.win_game()
                player2.lose_game()
                # print(player1, "win game")
            elif not res1 and not res2:
                player1.brake_game()
                player2.brake_game()
                # print("brake game")
        return None
        
    def tournament(self, *players):
        for p1, p2 in itertools.combinations(players, 2):
            self.play(p1, p2)
            print(p1, p1.get_candy_count(), p2, p2.get_candy_count())
        return None

    def top3(self):
        return None


class Player(object):

    def __init__(self):
        self.candyes = 0
        self.last_play = None
        self.last_res = None
        self.distrust = False

    def get_candy_count(self):
        return self.candyes

    def win_game(self):
        self.candyes = self.candyes + 3
        self.last_res = win
        return None

    def lose_game(self):
        self.last_res = lose
        return None

    def draw_game(self):
        self.candyes = self.candyes + 2
        self.last_res = draw
        return None

    def brake_game(self):
        self.last_res = brake
        return None

    # метод, высчитывающий прошлое действие противника
    def __think_about_it__(self):
        if self.last_play == coop and self.last_res == draw:
            return coop
        elif self.last_play == coop and self.last_res == lose:
            return cheat
        elif self.last_play == cheat and self.last_res == win:
            return coop
        else:
            return cheat


class Cheater(Player):

    def play(self, match_num):
        self.last_play = cheat
        return cheat


class Cooperator(Player):

    def play(self, match_num):
        self.last_play = coop
        return coop


class Copycat(Player):

    def play(self, match_num):
        if match_num == 0:
            self.last_play = coop
            return coop
        else:
            self.last_play = self.__think_about_it__()
        return self.__think_about_it__()


class Grudger(Player):

    def play(self, match_num):
        if match_num == 0:
            self.last_play = coop
            return coop
        else:
            if not self.distrust and self.__think_about_it__() == cheat:
                self.distrust = True
            elif self.distrust:
                self.last_play = cheat
                return cheat
            else:
                self.last_play = coop
                return coop


class Detective(Player):

    def play(self, match_num):
        if match_num in [0, 2, 3]:
            if match_num != 0 and self.__think_about_it__() == cheat:
                self.distrust = True
            self.last_play = coop
            return coop
        elif match_num == 1:
            self.last_play = cheat
            return cheat
        else:
            if self.distrust:
                self.last_play = self.__think_about_it__()
                return self.__think_about_it__()
        return cheat
        
class Sample(Player):

    def play(self, match_num):
        if match_num == 0:
            self.last_play = coop
            return coop
        else:
            if self.distrust == -1 and self.__think_about_it__() == cheat:
                print("distrust")
                self.distrust = 1
            elif self.distrust == False and self.__think_about_it__() == cheat:
                print("think")
                self.distrust = -1
                return coop
            elif self.distrust == 1:
                self.last_play = cheat
                return cheat
            else:
                self.last_play = coop
                return coop