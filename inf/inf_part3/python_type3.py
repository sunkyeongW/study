#선언
a = []
b = list()
c = [70, 40, 30, 20]
d = [100, 3000, 'apple', 'banana']
e = [100, 3000, ['apple', 'banana']]
f = [23.53, 'foobar', 3, 5, False, 3.43453]
print(len(c))
print()
#인덱싱
print('d -', type(d), d)
print('d -', d[1])
print('e -', e[-1][-1])
print('e -', list(e[-1][-1]))
print()
#슬라이싱
print('d -', d[0:2])
print('d -', d[0:])
print('e -', e[-1][:2] )
print()
#리스트 연산
print('c + d', c + d)
print(c * 3)
print('Test' + str(c[0]))
print()
#값 비교
print(c == c[:3] + c[3:])
print()
#identify(id)
temp = c
print(temp,c)
print()
#리스트 수정,삭제
print('리스트 수정,삭제')
c = [70, 40, 30, 20]
c[2:3] = ['a','b','c']
print(c)

del c[2]
print(c)
print()
#리스트 함수
a = [2, 5, 6, 4, 1]
print(a)
a.append(10)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
a.insert(2, 7)
print(a)
a.reverse()
print(a)
#del
a.remove(10)
print(a)
print('a - ', a.pop())
print(a)
print('a - ' ,a.count(4))
ex = [8, 9]
a.extend(ex)
print('a - ', a)

#삭제: remove, pop, del
