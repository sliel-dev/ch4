cart = {'사과' : 3, '바나나' : 5, '딸기' : 2}

apple = cart('사과')
banana = cart('바나나')
stro = cart('딸기')
total = apple + banana + stro
print(total)

scores = {'수학' : 95, '영어' : 88, '국어' : 100}

math_sco = scores('수학')
eng_sco = scores('영어')
nat_sco = scores('국어')
total = (math_sco + eng_sco + nat_sco) / 3
print(total)

menu = {'아메리카노' : 2000, '라떼' : 3000, '케이크' : 4500}

ame = menu('아메리카노')
latte = menu('라떼')
cake = menu('케이크')
total = (ame * 2) + latte
print(total)