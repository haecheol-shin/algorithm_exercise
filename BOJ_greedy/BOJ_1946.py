# 일단 데이터 입력받는거는 성공

test_case = int(input()) # 테스트 케이스의 개수
case_people = []
people_rank = []

for i in range(test_case):
    case_people.append(int(input()))
    for j in range(case_people[i]):
        people_rank.append(list(map(int, input().split())))

print(people_rank)
