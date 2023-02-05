# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import math
grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]];
print(len(grid))
print(grid[0][0])


def checkXMatrix(grid):
    """
    :type grid: List[List[int]]
    :rtype: bool
    """
    Size = len(grid)
    i = j = 0
    sum = 0
    multiply = 1
    while i < Size:
        while j < Size:
            multiply *=grid[j][j]
            j = j + 1
            i =i +1
            if i != j:
                sum += grid[i][j]
    if multiply != 0 and sum == 0:
        return 'true'
    else:
        return 'false'


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print(checkXMatrix(grid))

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
