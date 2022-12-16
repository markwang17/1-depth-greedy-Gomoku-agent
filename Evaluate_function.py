import Global_variables
import re


def evaluate_board_score(color, i, j):
	row_string = '2'
	col_string = '2'
	right_dia_string = '2'
	left_dia_string = '2'
	for ii in range(15):
		if Global_variables.black[i][ii] == 1:
			if color == 'black':
				row_string += '1'
			else:
				row_string += '2'
		elif Global_variables.white[i][ii] == 1:
			if color == 'black':
				row_string += '2'
			else:
				row_string += '1'
		else:
			row_string += '0'
	row_string += '2'
	for ii in range(15):
		if Global_variables.black[ii][j] == 1:
			if color == 'black':
				col_string += '1'
			else:
				col_string += '2'
		elif Global_variables.white[ii][j] == 1:
			if color == 'black':
				col_string += '2'
			else:
				col_string += '1'
		else:
			col_string += '0'
	col_string += '2'
	for ii in range(max(0, i-j), min(i+(14 - j) + 1, 15)):
		if Global_variables.black[ii][ii + j - i] == 1:
			if color == 'black':
				right_dia_string += '1'
			else:
				right_dia_string += '2'
		elif Global_variables.white[ii][ii + j - i] == 1:
			if color == 'black':
				right_dia_string += '2'
			else:
				right_dia_string += '1'
		else:
			right_dia_string += '0'
	right_dia_string += '2'
	for ii in range(max(0, i-(14 - j)), min(i + j + 1, 15)):
		if Global_variables.black[ii][j - (ii - i)] == 1:
			if color == 'black':
				left_dia_string += '1'
			else:
				left_dia_string += '2'
		elif Global_variables.white[ii][j - (ii - i)] == 1:
			if color == 'black':
				left_dia_string += '2'
			else:
				left_dia_string += '1'
		else:
			left_dia_string += '0'
	left_dia_string += '2'

	is_col_done, is_row_done, is_dia_left_done, is_dia_right_done = \
		False, False, False, False
	is_double_three, is_double_four = False, False
	score = 0
	for patterns in Global_variables.all_patterns:
		for p in patterns:

			if not is_col_done:
				result = re.search(p, col_string)
				if result:
					is_col_done = True
					cur_score = Global_variables.all_scores[Global_variables.all_patterns.index(patterns)]
					if cur_score >= 100 and is_double_three:
						score += 1000
					elif cur_score >= 10:
						if is_double_four:
							score += 150
					if cur_score >= 100: is_double_three = True
					elif cur_score >= 10: is_double_four = True
					score += cur_score
			if not is_row_done:
				result = re.search(p, row_string)
				if result:
					is_row_done = True
					cur_score = Global_variables.all_scores[Global_variables.all_patterns.index(patterns)]
					if cur_score >= 1000 and is_double_three:
						score += 10000
					elif cur_score >= 100:
						if is_double_four:
							score += 1500
					if cur_score >= 1000:
						is_double_three = True
					elif cur_score >= 100:
						is_double_four = True
					score += cur_score
			if not is_dia_left_done:
				result = re.search(p, left_dia_string)
				if result:
					is_dia_left_done = True
					cur_score = Global_variables.all_scores[Global_variables.all_patterns.index(patterns)]
					if cur_score >= 1000 and is_double_three:
						score += 10000
					elif cur_score >= 100:
						if is_double_four:
							score += 1500
					if cur_score >= 1000:
						is_double_three = True
					elif cur_score >= 100:
						is_double_four = True
					score += cur_score
			if not is_dia_right_done:
				result = re.search(p, right_dia_string)
				if result:
					is_dia_right_done = True
					cur_score = Global_variables.all_scores[Global_variables.all_patterns.index(patterns)]
					if cur_score >= 1000 and is_double_three:
						score += 10000
					elif cur_score >= 100:
						if is_double_four:
							score += 1500
					if cur_score >= 1000:
						is_double_three = True
					elif cur_score >= 100:
						is_double_four = True
					score += cur_score
	return score + Global_variables.board_scores[i][j]
