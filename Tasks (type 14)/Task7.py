from lib import numSysToTen
from lib import numSys


for x in range(10):
	temp = numSysToTen(int(f'8{x}121'),13)-numSysToTen(int(f'7{x}575'),13)
	
	if temp % 19 == 0:
		print(x)
		print(temp/19)
# Ответ: min x = 0, 