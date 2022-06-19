#문자열 사용법
len - 공백포함 문자길이

#빈 문자열
1.'' or ""
2.str()

#이스케이프 문자
\n : 줄바꿈
\b : 백스페이스(한글자 삭제)
\f : 커서를 다음줄로 이동
\r : 커서를 앞으로 이동
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자

#raw string
raw string을 사용하면 escape문이 동작되지 않고, 있는 그대로 출력된다.
#멀티라인 사용
역슬래시\를 이용

#문자열 연산
* : 반복
+ : 합쳐서 출력
in : 단어가 존재하는지
not in : 단어가 존재하지 않는지

#문자열 함수
Capitalize : 첫글자를 대문자로 변경
endswith : 정의된 문자열의 끝의 문자열과 같은지 다른지를 증명
replace : 특정 단어를 새로운 단어로 바꿈
sorted : 단어를 한글자씩 배열
split : 특정 단어를 기준으로 띄어쓰기 배열

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
문자 -> 아스키 코드 : ord
아스키 코드 -> 코드 : chr