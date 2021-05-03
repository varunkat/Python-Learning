

import collections
items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

#Output: [[1,87],[2,88]]
res = []
dic = collections.defaultdict(list)
for id, score in items:
    dic[id].append(score)
print(dic)

for id, score in dic.items():
    score.sort(reverse = True)
    res.append([id, sum(score[:5]) // 5])

print(res)
