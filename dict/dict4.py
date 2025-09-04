import copy

# dic = {'name' : '둘리', 'age' : 20}
# copy = dic.copy()

# copy['age'] = 25
# print(dic)
# print(copy)

dic = {'name' : '둘리', 'age' : 20, 'hobby' : ['축구', '야구']}
copy = copy.deepcopy(dic)

copy['hobby'][0] = '테니스'
print(dic)
print(copy)
