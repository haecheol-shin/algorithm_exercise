# 먼저 리스트로 입력받고
# 길이만큼 for문-> 수식의 맨끝에서부터 시작
# 거꾸로 계산하는게 더 편할듯함
# 마이너스가 나오면 나온 부분까지 해서 슬라이스 리스트에 저장
# 그 리스트를 eval함수로 계산
# 변수에다 더해주고 슬라이스 리스트는 다시 초기화
# 마지막으로 원 수식에 남은 수까지 다 해서 결과값

### 09-09 예외발생

expression = list(input()) # input mathmatical expression

sum = 0 # 마이너스 덩어리를 더해줄 변수
slice_expression = [] # 마이너스 덩어리
slicing_number = 55 # 원 수식에서 마이너스 덩어리를 슬라이싱 할때 필요한 인덱스 번호를 저장하는 변수

for i in range(-1, -len(expression), -1):
    if ('-'==expression[i]):
        slice_expression = expression[i+1:] # 마이너스 기호 앞까지만 저장
        slicing_number = i 
        sum += -eval(''.join(eval("slice_expression"))) # 억지 형변환, 마이너스 기호를 붙여줌

del expression[slicing_number:] # 원 수식에서 마이너스 덩어리 삭제

print(sum+eval(''.join(eval("expression"))))