import Evaluate_function
import Global_variables
import random

best_pos = []
search_range = []


def get_best_position(is_black):
	global search_range, best_pos
	search_range = improve_branching()
	best_pos = greedy_process(is_black)
	return best_pos


def improve_branching():
	cover_range = [[0 for _ in range(15)] for __ in range(15)]
	for i in range(15):
		for j in range(15):
			if Global_variables.flag[i][j] == 1:
				for k in range(3):
					cover_range[max(0, i - 1)][min(14, j - 1 + k)] = 1
					cover_range[max(0, i)][min(14, j - 1 + k)] = 1
					cover_range[min(14, i + 1)][min(14, j - 1 + k)] = 1
	for i in range(15):
		for j in range(15):
			if Global_variables.flag[i][j] == 1:
				cover_range[i][j] = 0
	return cover_range


def greedy_process(is_black):
	global search_range
	black_max_score = 0
	white_max_score = 0
	w_best_pos = []
	b_best_pos = []
	if is_black:
		for i in range(15):
			for j in range(15):
				if Global_variables.flag[i][j] == 0 and search_range[i][j] == 1:
					Global_variables.flag[i][j] = 1
					search_range[i][j] = 0
					Global_variables.white[i][j] = 1
					white_score = Evaluate_function.evaluate_board_score('white', i, j)
					Global_variables.white[i][j] = 0
					Global_variables.black[i][j] = 1
					black_score = Evaluate_function.evaluate_board_score('black', i, j)
					Global_variables.black[i][j] = 0
					Global_variables.flag[i][j] = 0
					if black_score > black_max_score:
						black_max_score = black_score
						b_best_pos = [(i, j)]
					elif black_score == black_max_score:
						b_best_pos.append((i, j))
					if white_score > white_max_score:
						white_max_score = white_score
						w_best_pos = [(i, j)]
					elif white_score == white_max_score:
						w_best_pos.append((i, j))

		if white_max_score > black_max_score:
			return random.choice(w_best_pos) if w_best_pos else ""
		else:
			return random.choice(b_best_pos) if b_best_pos else ""

	else:
		for i in range(15):
			for j in range(15):
				if Global_variables.flag[i][j] == 0 and search_range[i][
					j] == 1:
					Global_variables.flag[i][j] = 1
					search_range[i][j] = 0
					Global_variables.black[i][j] = 1
					white_score = Evaluate_function.evaluate_board_score(
						'black', i, j)
					Global_variables.black[i][j] = 0
					Global_variables.white[i][j] = 1
					black_score = Evaluate_function.evaluate_board_score(
						'white', i, j)
					Global_variables.white[i][j] = 0
					Global_variables.flag[i][j] = 0
					if black_score > black_max_score:
						black_max_score = black_score
						b_best_pos = [(i, j)]
					elif black_score == black_max_score:
						b_best_pos.append((i, j))
					if white_score > white_max_score:
						white_max_score = white_score
						w_best_pos = [(i, j)]
					elif white_score == white_max_score:
						w_best_pos.append((i, j))

		if white_max_score < black_max_score:
			return random.choice(b_best_pos) if b_best_pos else ""
		else:
			return random.choice(w_best_pos) if w_best_pos else ""
