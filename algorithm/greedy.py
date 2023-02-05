# 贪婪算法
# 集合不能包含重复的元素 set([数列])
# 散列表：

x = 121
#x = str(x)
#print(''.join(reversed(x)))
#print(reversed(x))

if x < 0:
    print(False)
x = str(x)
if ''.join(reversed(x)) == x:
    print(True)
