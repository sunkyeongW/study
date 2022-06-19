#문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """hi"""
str4 ='''hello'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

#빈 문자열
str1_t1 = '' or ""
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

#이스케이프 문자 사용
print("I'm Boy")
print("I\'m Boy")
print('a\tb')
print('a\nb')
print('ad\\bd')
print('adf\000bdf')
print('adfs\bbdfsd')
print('adf\fbdf')
print('adf\rbdf')

#Raw String
raw_s1 = r'D:\python\test'
print(raw_s1)

#멀티라인 출력
multi_str =\
"""
문자열
멀티라인 입력
테스트
"""
print(multi_str)

#문자열 연산
str_o1 = "python"
str_o2 = "apple!"
str_o3 = "banana"
str_o4 = "wa!te!r"

print(str_o1 * 3)
print('y' in str_o1)
print('y' not in str_o2)

#문자열 함수
#upper, isalnum, startswith 등등

print("Capitalize:", str_o1.capitalize())
print("endswith?:", str_o2.endswith("!"))
print("replace:", str_o3.replace('ban', 'nam' ))
print("sorted: ", sorted(str_o2))
print("split: ", str_o4.split('!'))
print()
#반복(시퀀스)
im_str = "good boy!"
#__iter__
#출력
for i in im_str:
    print(i)

#슬라이싱
str_sl = "Nice Goodboy"
print(len(str_sl))
print(str_sl[0:3]) #0 1 2
print(str_sl[5:]) # [5:12]
print(str_sl[:len(str_sl)]) # [:12]
print(str_sl[0:9:2]) #스킵하면서 가져오기
print(str_sl[-5:]) #뒤의 단어부터 빼기
print(str_sl[::3]) #스킵하면서 가져오기

#아스키 코드
a = 'z'

print(ord(a))
print(chr(122))
