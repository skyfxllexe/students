def numSystem(number, numSys):
	result = ""
	while number > 0:
		result += str(number % numSys)
		number //= numSys
	return result[::-1]  # возврат строки


number = 8**20 + ((8**22-8**17))*(8**13+8**16)
# число = number
new_number = numSystem(number, 8)
# перевод в 8-СС
new_number = new_number.replace('7', '0')
# заменяем 7 на 0 во всей строке
# далее, по-хорошему, просят удалить то,
# что стоит на 0, 1 и 2 индексе, затем посчитать
# сумму. Но это равносильно замене на 0
new_number = new_number[3:-1]
summa = 0
for elem in new_number:
	summa += int(elem)  # приводим elem к типу int
print(summa)
# ответ: 7