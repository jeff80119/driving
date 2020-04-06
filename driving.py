country = input('請問你是哪國人: ')
age = input('輸入你的年齡: ')
if str.isdigit(age):
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
else:
	print('年齡輸入錯誤')