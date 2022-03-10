n = int(input()) # 지불한 돈

exchange = 1000 - n # 거스름돈

result = 0 # 결과 값

result += exchange // 500 # 500엔 개수

exchange = exchange % 500 # 500엔 개수 뺀 나머지

result += exchange // 100 # 100엔 개수

exchange = exchange % 100 # 100엔 개수 뺀 나머지

result += exchange // 50 # 50엔 개수

exchange = exchange % 50 # 50엔 개수 뺀 나머지

result += exchange // 10 # 10엔 개수

exchange = exchange % 10 # 10엔 개수 뺀 나머지

result += exchange // 5 # 5엔 개수

exchange = exchange % 5 # 5엔 개수 뺀 나머지

print(result+exchange)