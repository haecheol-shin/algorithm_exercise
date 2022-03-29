# 일단 데이터 입력받는거는 성공

test_case = int(input()) # 테스트 케이스의 개수
case_people = []
people_rank = []
rank_sum = []


for i in range(test_case):
    case_people.append(int(input()))
    for j in range(case_people[i]):
        people_rank.append(list(map(int, input().split())))
        rank_sum[j] = people_rank[j][0] + people_rank[j][1] # 각 사람들의 성적 합


# 그룹에서 성적이 가장 좋은사람의 순위를 뽑아냄
# 둘 중 더 낮은 성적을 뽑아냄
# 만약 5명 중 4등을 했다? -> 3명까지 무조건 확정
# 1등이 여러 명이라면? -> 3명 + @

for i in range(test_case):


print(people_rank)
