from lib import numSysToTen
from lib import numSys


for i in range(9,21):
	t = numSys(i,2)
	t = t[-3]+t[-2]+t[-1]
	if t == '110':
		print(i)
# Ответ: 14