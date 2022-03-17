n = input() # 수를 입력받음 (일부러 str으로 받음)
n_list = list(n) # 리스트로 변환
n_list = list(map(int, n_list)) # 각 항목을 int형으로 변환 (map을 쓰면 list가 아닌 iterator object가 되기 때문에 다시 리스트로 형변환)
n_list.sort(reverse=True) # 내림차순 정렬

sum = 0 # 각 자리수의 총합
n_max = '' # 30의 배수가 되는 최댓값 (list를 다시 str으로 바꿔줘야 하기 때문에 str으로 선언)

for i in range(len(n_list)): # 각 자리수를 다 더함
    sum += int(n_list[i])

if (n_list[len(n_list)-1] == 0 and sum%3==0): # 30의 배수가 되는 조건
    n_max = int(''.join(str(s) for s in n_list)) # list를 str로 바꿔준 후 int형으로 형변환
    print(n_max)

else: # 30의 배수가 아닐경우
    print(-1)