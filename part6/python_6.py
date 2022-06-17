import math
import statistics
from xmlrpc.server import DocCGIXMLRPCRequestHandler


print('정수형 변수')
pizza = 22900
coke = 1500
print("pizza = 22900")
print("coke = 1500")
print("pizza + coke",pizza + coke)
print("coupon 30%",(pizza + coke) * 0.7)
print('''
''')
print('문자열 변수')
star = 'dog'
goodboy = 'cutie'
print("star = dog")
print("goodboy = cutie")

print(star + goodboy)
print('''
''')
print('리스트 변수')
f_age = [59,59,34,30,26,17]
f_age.append(100)
print('fameily age',f_age)
print('리스트의 다섯번째',f_age[5])
print(f_age)

