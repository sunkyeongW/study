#집합(set) 특징
#집합(set) 자료형(순서x, 중복x, 추가o, 삭제o)

#선언
a =set()
{} 키가없이 리스트만 나열하면 set임

#튜플 변환
t = tuple()
#리스트 변환
l = list()

#집합 자료형 활용
& 교집합
| 합집합
- 차집합

#중복원소
print('s1 & s2', s1.isdisjoint(s2))
false- 교집합 존재
true- 존재x

#부분 집합
.issubset
.issuperset - 진부분집합

#추가& 제거
.add

.remove
.discard
집합을 제거할때는 discard를 이용하면 예외를 발생하지 않음
.clear : 전부 삭제