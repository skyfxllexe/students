'''
Это мини-библиотека функций, чтобы решать задания на СС
Чтобы постоянно не прописывать эти функции мне, я ее сделал
Тут можно ознакомиться с функциями
Первая переводит число number из системы счисления numSys в десятичную
Вторая переводит число number в систему счисления numSys
Третья считает сумму цифр строки
Использовать в других приложениях: закинуть в ОДНУ ПАПКУ
со всеми остальными задачами lib.py (этот файл)
и внутри кода будет работать строчка from lib import <func_name>

'''

def numSysToTen(number, numSys):
	summa = 0
	numberString = str(number)[::-1]
	for elem in range(len(numberString)):
		summa += int(numberString[elem]) * numSys**elem
	return summa


def numSys(number, numSys):
	result = ""
	while number > 0:
		result += str(number % numSys)
		number //= numSys
	return result[::-1]


def summaStroki(string):
	summa = 0
	for elem in range(len(string)):
		summa += int(string[elem])
	return summa
