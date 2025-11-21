#
def calc(a, b, op):
	"""Perform basic arithmetic on two numbers."""
	try:
		return {'+': a + b, '-': a - b, '*': a * b, '/': a / b}[op]
	except KeyError:
		raise ValueError('Operator must be one of: + - * /')
	except ZeroDivisionError:
		return 'Error: division by zero'


if __name__ == '__main__':
	a = float(input('First number: '))
	b = float(input('Second number: '))
	op = input('Operator (+ - * /): ').strip()
	try:
		print('Result:', calc(a, b, op))
	except ValueError as e:
		print(e)
