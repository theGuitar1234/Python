from turanpy.config import DEFAULTS

def f(x):
    return x**2

def bajillion_integral(f, a, b):

	dx = (b - a) / DEFAULTS.bajillion
	n = DEFAULTS.bajillion

	area = 0.0
	for i in range(n):
		x = a + i * dx         
		area += f(x) * dx
	return area

def trapezoid_integral(f, a, b): 

	dx = (b - a) / DEFAULTS.bajillion
	n = DEFAULTS.bajillion

	area = 0.0
	for i in range(n):
		x0 = a + i * dx
		x1 = x0 + dx
		area += (f(x0) + f(x1)) * 0.5 * dx
	return area

if __name__ == "__main__":
	pass