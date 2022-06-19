#선언
a = set()
b = set([1, 2, 3, 4])
c = set([3, 5, 6, 7])
d = set([3, 5, 'pen', 'plate'])
e = {'foo', 'bar', 'zoo', 'qer'}
f = {45, 'zio', (1, 2, 3), 3.453}

print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)
print(type(f), f)
print()
#튜플 변환
t = tuple(b)
print(type(t), t)
#리스트 변환
l = list(f)
print(type(f), f)
print()
#집합 자료형 활용
s1 = set([4, 5, 6])
s2 = set({4, 5, 6, 7, 8, 9})
print('교집합')
print('s1 & s2', s1 & s2)
print('s1 & s2', s1.intersection(s2))
print('합집합')
print('s1 | s2', s1 | s2)
print('s1 | s2', s1.union(s2))
print('차집합')
print('s1 - s2', s1 - s2)
print('s1 - s2', s1.difference(s2))
print()
#중복 원소 확인
print('s1 & s2', s1.isdisjoint(s2))

#부분 원소 확인
s1 = set([4, 5, 6, 7, 8, 9])
s2 = set({7, 8, 9})
print(s1.issubset(s2))
print(s1.issuperset(s2))
print()
#추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
#제거
s1.remove(2)
print(s1)
s1.discard(3)
print(s1)