import math
'''
Импортируем библиотеку math, для использования числа pi = 3.141592653589793...
'''

def area(r):
    '''
	 Принимает число r(радиус круга).
	 Возвращает площадь круга (радиус в квадрате, умноженный на число pi)
	 Параметры:
		 r(int/float)
	 Доп параметры:
		 pi:(float)
	 Возвращаемое значение:
		 pi*r*r(float) - площадь круга
    '''
    return math.pi * r * r
'''
Пример вышеприведенной функции:
r = 10 (int)
area(r) = 314.1592653589793 (float)
'''


def perimeter(r):
    '''
	 Принимает число r(радиус круга).
	 Возвращает периметр круга (дважды радиус, умноженный на число pi)
	 Параметры:
		 r(int/float)
	 Доп параметры:
		 pi:(float)
	 Возвращаемое значение:
		 2*pi*r(float) - периметр круга
    '''
    return 2 * math.pi * r
'''
Пример вышеприведенной функции:
r = 10 (int)
perimeter(r) = 62.83185307179586 (float)
'''

