seq = 'ABCDE'
for i,element in enumerate(seq):
    print(i,element)
    i = i+1

print(list(enumerate(seq)))

#哈希表+排序
# defaultdict(list),会构建一个默认value为list的字典
'''
#from collections import defaultdict
result = defaultdict(list)
data = [("p", 1), ("p", 2), ("p", 3),
        ("h", 1), ("h", 2), ("h", 3)]
 
for (key, value) in data:
    result[key].append(value)
print(result)#defaultdict(<class 'list'>, {'p': [1, 2, 3], 'h': [1, 2, 3]})
'''



