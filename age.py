driving = input ('請問你有沒有開過車?')
if driving != '有' and driving !='沒有' :
	print('只能輸入 有/沒有')
	raise SystemExit

age = input('請問你的年齡?')
age = int(age)
if driving == '有' :
	if age >= 18 :
		print('你通過測驗了')
	else :
	    print('奇怪 你怎麼有開過車')
elif driving == '沒有':
    if age >= 18 :
        print('你可以去考駕照了')
    else :
        print('很好,再過幾年你就可以考了')    	    
else:
	print('只能輸入 有/沒有')