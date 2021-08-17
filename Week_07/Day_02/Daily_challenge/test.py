# Daily Challenge - Solve the matrix
matrix = [
		['7', 'i', '3'],
		['T', 's', 'i'],
		['h', '%', 'x'],
		['i', ' ', '#'],
		['s', 'M', ' '],
		['$', 'a', ' '],
		['#', 't', '%'],
		['^', 'r', '!'],
]

result = ''
num_of_column = len(matrix[0])
num_of_rows = len(matrix)
for i in range(num_of_column):
	for j in range(num_of_rows):
		# scan the column
		if matrix[j][i].isalpha():
			result += matrix[j][i]
		elif result and result[-1] != ' ':  # result is not an empty string and the last item is not a space
			result += ' '

print(result)