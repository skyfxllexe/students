from lib import numSys
from lib import summaStroki
# использование библиотеки
# для того чтобы везде не писать одно и то же
# алгоритм приложен в корневой папке lib

for x in range(1, 1000):
	number = 64**11 - 4**10 + 96 - x
	if summaStroki(numSys(number, 4)) == 71:
		print(x)
# Ответ: 16
