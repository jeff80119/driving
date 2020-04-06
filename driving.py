country = input('請問你是哪國人: ')
age = input('輸入你的年齡: ')
if int(age):
	age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你不可以考駕照')
if country == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你不可以考駕照')
else:
	print('你的國家未知')