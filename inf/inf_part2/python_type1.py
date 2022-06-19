#숫자형

#파이썬 지원 자료형
""""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
turple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

#데이터 타입

str1 = "python"
bool = True , #False
str2 = "star"
float_v = 10.0
int_v = 7
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0
}
turple = (1, 2, 3)
set = {4, 5, 6}


print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(list))
print(type(dict))
print(type(dict))
print(type(turple))
print(type(set))
print()
#숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x)
pow(x, y) or x ** y -> 2 ** 3
"""
print(pow(2, 3))
print(2 ** 3)
print(abs(4))
print()
#정수 선언
i = 17
i2 = -26
big_int = 32442423424224242434224

print(i)
print(i2)
print(big_int)
print()

#실수 선언
f = 0.8989
f2 = 3.43
f3 = -3.445
f4 = 3 / 9
print(f)
print(f2)
print(f3)
print(f4)
print()

#형 변환 실습
a = 3
b = 5.0
c = 4.6
d = 25.76
print(type(a), type(b), type(c), type(d))
print(float(b))
print(int(c))
print(int(d))
print(int(True))
print(float(False))
print(complex(3))

#수치연산 함수
print(abs(-56))
x, y = divmod(100, 9)
print(x, y)
print(pow(5,3), 5 ** 3)

#외부 모듈
import math
print(math.pi)
print(math.ceil(5.1)) # 이상의 수 중에서 가장 작은 정수