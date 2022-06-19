#선언
a = ()
b = (1,)
c = (13,34,234,24)
d = (56, 65, 'ace', 'base')
e = (2, 3, ('dfg', 'case'))
print(type(a), type(b))
print()
#인덱싱
print('d -', d[1])
print('d -', d[1] + d[0])

#슬라이싱
print('d -', d[1:4])
print('e -', e[2][1:])
print()
#튜플 함수
a = (5, 2, 3, 1, 4)
print('a -', a)
print('a -', a.index(1)) #위치
print('a -', a.count(1)) #특정 원소 갯수
print()
#팩킹 & 언팩킹
#팩킹
t = ('foo', 'bar', 'zoo', 'rfr')

#언팩킹
(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)