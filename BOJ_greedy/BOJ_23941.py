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