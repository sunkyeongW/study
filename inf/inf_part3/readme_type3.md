#리스트 자료형(순서, 중복, 수정, 삭제)
순서는 0번부터 시작
다양한 데이터타입 동시에 배열 가능
리스트 안에 리스트 입력 가능

#인덱스
ex)
e = [100, 3000, ['apple', 'banana']]
print(e[-1][-1]) : e라는 리스트(-1번째 순서는 ['apple', 'banana'] )
안에 [-1]이기 때문에 'banana'가 입력.

#리스트 연산
* 숫자만큼 정렬(단, 순서는 유지)
문자 + 숫자는 같은 타입으로 변경.

#id
temp 임시로 저장할 변수

#리스트 수정, 삭제
슬라이스 범위를 지정했을시엔 원소
리스트로 입력시엔 리스트로 입력

#리스트 함수
append() : 리스트 끝에 추가
sort() : 오른차순으로 정렬
reverse() : 역순으로 정렬
insert() : 위치에 삽입
remove() : 불필요한 걸 리스트에서 삭제
pop() : 마지막 원소를 단독으로 빼놓고 나머지 원소를 리스트로 정리
queue() : 먼저 들어온 원소를 단독으로 빼놓고 나머지 원소를 리스트로 정리
count() : 값의 갯수를 확인
extend() : 원소를 연장