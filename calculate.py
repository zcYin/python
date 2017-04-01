import math
def calculate(a,b,c):
	g = b*b - 4 * a * c
	if g < 0:
		print('无解')
	else:
		x = (-b + math.sqrt(g))/(2 * a)
		y = (-b - math.sqrt(g))/(2 * a)
		print(x,y)

calculate(1,0,1)