from lib import numSys
from lib import numSysToTen

for i in range(8,1000):
	if numSysToTen(123, i) == numSysToTen(93,i+2):
		print(i)
# Ответ: 9