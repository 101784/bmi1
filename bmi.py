height = input('請輸入身高(cm): ')
weight = input('請輸入體重(kg): ')
height = float(height)
weight = float(weight)
height = height/100
bmi = weight / height**2
if bmi < 18.5 :
	print('你的bmi值為 :', bmi , '體重過輕歐')
elif bmi >= 18.5 and bmi < 24:
	print('你的bmi值為 :', bmi ,'正常範圍')
elif 24 >= bmi < 27:
	print('你的bmi值為 :', bmi ,'過重囉')
elif 27 >= bmi < 30:
	print('你的bmi值為 :', bmi ,'輕度肥胖')
elif 30 >= bmi < 35:
	print('你的bmi值為 :', bmi ,'中度肥胖')
else :
	print('你的bmi值為 :', bmi ,'超出範圍拉兄弟')