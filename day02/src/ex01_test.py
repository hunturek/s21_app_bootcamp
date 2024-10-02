import ex01

player1 = ex01.Cheater()
player2 = ex01.Cooperator()
player3 = ex01.Copycat()
player4 = ex01.Grudger()
player5 = ex01.Detective()
player6 = ex01.Sample()

prisoners_problem = ex01.Game()
prisoners_problem.tournament(player1, player2, player3, player4, player5, player6)

print("Cheater:", player1.get_candy_count())
print("Cooperator:", player2.get_candy_count())
print("Copycat:", player3.get_candy_count())
print("Grudger:", player4.get_candy_count())
print("Detective:", player5.get_candy_count())
print("Sample:", player6.get_candy_count())