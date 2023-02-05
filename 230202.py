"""
在一个有向图中，节点分别标记为 0, 1, ..., n-1。图中每条边为红色或者蓝色，且存在自环或平行边。

red_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的红色有向边。类似地，blue_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的蓝色有向边。

返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 answer[x] = -1。

 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/shortest-path-with-alternating-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

#学习图的表示方法:散列表，无顺序
from collections import deque
graph = {}
graph["you"]=["Alice","Bob","Clarie"]
graph["Alice"]=[]
graph["Bob"]=["you"]
graph["Clarie"] = ["you","mogom"]


search_queue = deque()
search_queue += graph["you"]

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person+"is a mango person")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")

n = 3
red_edges = [[0,1],[1,2]]
blue_edges = []

class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        g = []
        for i,j in redEdges:
            g[0][i].append(j)
        for i,j in blueEdges:
            g[1][i].append(j)
        ans = [-1]*n
        vis = set()
        q = deque([(0,0),(0,1)])
        d = 0
        while q:
            for _ in range(len(q)):
                i,c = q.popleft()
                if ans[i] == -1:
                    ans[i] = d
                vis.add((i,c))
                c = 1
                for j in g[c][i]:
                    if (j,c) not in vis:
                        q.append((j,c))
            d += 1
        return ans

#Solution().shortestAlternatingPaths(n,red_edges,blue_edges)



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                sum = nums[i] + nums[j]
                if sum == target:
                    ans = [i, j]
                    return ans