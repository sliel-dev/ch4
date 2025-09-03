lis = [1, 2, 3]

lis.append(4)
print(lis)

lis.insert(0, 0)
print(lis)

lis[2] = 7
print(lis)

del lis[2] # 인덱스 자리를 삭제
print(lis)

lis.remove(3) # 값을 삭제
print(lis)

last = lis.pop(0)
print(lis, last)

size = len(lis)
print(size)