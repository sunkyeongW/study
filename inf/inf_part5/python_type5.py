#선언
a = {'name': 'Won', 'phone': '01030305939', 'birth': '971109'}
b = {0: 'hello'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'star',
    'City': 'Incheon',
    'Age': 24,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'star'),
    ('City', 'Incheon'),
    ('Age', 26),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name='Won',
    City='Incheon',
    Age=26,
    Grade='A',
    Status=True
)
print('a -', type(a), a)
print('b -', type(b), b)
print('c -', type(c), c)
print('d -', type(d), d)
print('f -', type(f), f)
print()
#출력
print('a -', a['name'])
print('a -', a.get('name1'))
print('b -', b.get(0))
print('f -', f.get('City'))
print()
#딕셔너리 추가
a['address'] = 'seoul'
print('a -', a)
a['rank'] = [1, 2, 3]
print('a -', a)

#반복문
print('키 값')
print('a -', a.keys())
print('b -', b.keys())
print('c -', c.keys())
print('d -', d.keys())
print('e -', e.keys())
print('values')
print('a -', a.values())
print('b -', b.values())
print('c -', c.values())
print('d -', d.values())
print('e -', e.values())
print('items')
print('a -', a.items())
print('b -', b.items())
print('c -', c.items())
print('d -', d.items())
print('e -', e.items())
print()
#pop
print('a - ', a.pop('name'))
print('a - ', a)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print()
#in mathod
print('a - ', 'birth' in a)
print('d - ', 'birth' in d)
print()
#수정
a['test'] = 'test_dict'
print('a - ', a)

a.update(birth='971110')
print('a - ', a)

temp = {'phone': '01030451234'}
a.update(temp)
print('a - ', a)
