from graphics import *
import Global_variables
import Greedy_ai

p = [[0 for _ in range(15)] for __ in range(15)]
q = [[0 for _ in range(15)] for __ in range(15)]
win = ''


def start_one_game():
	global win
	win = GraphWin("GAME", 480, 600)
	draw_game_board()
	turn_num = 0
	while True:
		turn_num = make_one_move(turn_num)
		if turn_num == -1:
			break
		if win_check() == 'black':
			Text(Point(240, 500), 'Black wins').draw(win)
			break
		if win_check() == 'white':
			Text(Point(240, 500), 'White wins').draw(win)
			break
	win.getMouse()


def draw_game_board():
	global win
	for i in range(15):
		for j in range(15):
			p[i][j] = Point(i * 30 + 30, j * 30 + 30)
			p[i][j].draw(win)
	for r in range(15):
		Line(p[r][0], p[r][14]).draw(win)
		Line(p[0][r], p[14][r]).draw(win)
	center = Circle(p[7][7], 3)
	center.draw(win)
	center.setFill('black')


def make_one_move(turn_num):
	global win
	if turn_num % 2 == 0:
		position = Greedy_ai.get_best_position(True) if turn_num != 0 \
			else [7, 7]
		if not position:
			Text(Point(240, 500), 'draw...').draw(win)
			return -1
		i = position[0]
		j = position[1]
		Global_variables.black[i][j] = 1
		q[i][j] = Circle(p[i][j], 10)
		q[i][j].draw(win)
		q[i][j].setFill('black')
	else:
		position = Greedy_ai.get_best_position(False)
		if not position:
			Text(Point(240, 500), 'draw...').draw(win)
			return -1
		i = position[0]
		j = position[1]
		Global_variables.white[i][j] = 1
		q[i][j] = Circle(p[i][j], 10)
		q[i][j].draw(win)
		q[i][j].setFill('white')
	turn_num += 1
	Global_variables.flag[i][j] = 1
	return turn_num


def win_check():
	for i in range(15):
		for j in range(11):
			if Global_variables.black[i][j:j+5] == [1, 1, 1, 1, 1]:
				return 'black'
			elif Global_variables.white[i][j:j+5] == [1, 1, 1, 1, 1]:
				return 'white'
	for i in range(15):
		for j in range(11):
			if Global_variables.black[j][i] and Global_variables.black[j+1][i] and Global_variables.black[j+2][i] and Global_variables.black[j+3][i] and Global_variables.black[j+4][i]:
				return 'black'
			elif Global_variables.white[j][i] and Global_variables.white[j+1][i] and Global_variables.white[j+2][i] and Global_variables.white[j+3][i] and Global_variables.white[j+4][i]:
				return 'white'
	for i in range(11):
		for j in range(11):
			if Global_variables.black[i][j] and Global_variables.black[i+1][j+1] and Global_variables.black[i+2][j+2] and Global_variables.black[i+3][j+3] and Global_variables.black[i+4][j+4]:
				return 'black'
			elif Global_variables.white[i][j] and Global_variables.white[i+1][j+1] and Global_variables.white[i+2][j+2] and Global_variables.white[i+3][j+3] and Global_variables.white[i+4][j+4]:
				return 'white'
	for i in range(4, 15):
		for j in range(11):
			if Global_variables.black[i][j] and Global_variables.black[i-1][j+1] and Global_variables.black[i-2][j+2] and Global_variables.black[i-3][j+3] and Global_variables.black[i-4][j+4]:
				return 'black'
			elif Global_variables.white[i][j] and Global_variables.white[i-1][j+1] and Global_variables.white[i-2][j+2] and Global_variables.white[i-3][j+3] and Global_variables.white[i-4][j+4]:
				return 'white'
