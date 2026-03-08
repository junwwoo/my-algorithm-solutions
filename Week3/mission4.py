from collections import defaultdict
# 컬렉션 모듈을 이용하여 매번 key가 존재하는지 검사할 필요가 없어짐

s = "banana"

# 원래의 방법(처음 나온 문자에 대해 1을 더할 수가 없음)
result_dict1 = {}
for target in s:
  if target not in result_dict1:
    result_dict1[target] = 0
  result_dict1[target]+=1
print(dict(result_dict1))


# 컬렉션 모듈 활용 방법 (기본값을 0으로 초기화해 줌)
result_dict2 = defaultdict(int)
for target in s:
  result_dict2[target] +=1
print(dict(result_dict2))

# 추가 Counter 클래스 활용 방법
from collections import Counter
print(dict(Counter(s)))