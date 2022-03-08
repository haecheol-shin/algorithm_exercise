# 먼저 리스트로 입력받고
# 길이만큼 for문-> 수식의 맨끝에서부터 시작
# 거꾸로 계산하는게 더 편할듯함
# 마이너스가 나오면 나온 부분까지 해서 슬라이스 리스트에 저장
# 그 리스트를 eval함수로 계산
# 변수에다 더해주고 슬라이스 리스트는 다시 초기화

expression = list(input()) # input mathmatical expression

sum = 0
slice_expression = []
for i in range(-1, -len(expression), -1):
    if ('-'==expression[i]):
        slice_expression = expression[i:]
        sum += int(''.join(eval("slice_expression"))) #여기서 어거지 형변환 잘 안되는중

print(sum)