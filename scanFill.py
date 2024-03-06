import matplotlib.pyplot as plt
from seedFilling import generateRegion as boundary
plt.switch_backend('TKAgg')


def generateRegion():
    line2 = [(i, 1) for i in range(1, 4)]
    line3 = [(i, 2) for i in range(1, 4)]
    line4 = [(i, 3) for i in range(3, 4)]
    line5 = [(i, 4) for i in range(3, 7)]
    line6 = [(i, 5) for i in range(4, 7)]
    region =  line2 + line3 + line4 + line5 + line6
    return region


region = generateRegion()


def getPixelColor(x, y):
    if (x, y) in region:
        return 'red'  # oldcolor
    else:
        return 'blue'


def scanLineFill(x, y, oldColor, newColor, ax):
    stack = [(x, y)]  # 初始点入栈
    while stack:  # 存在种子点
        a = stack.pop()  # 获取种子点(右填充)
        x1, y1 = a[0], a[1]
        while getPixelColor(x1, y1) == oldColor:  # 向右填充
            ax.scatter(x1, y1, c=newColor)
            region.remove((x1, y1))
            plt.pause(0.01)
            x1 += 1
        xr = x1 - 1  # 右边界点
        x1 = a[0] - 1
        while getPixelColor(x1, y1) == oldColor:  # 向左填充
            ax.scatter(x1, y1, c=newColor)
            region.remove((x1, y1))
            plt.pause(0.01)
            x1 -= 1
        xl = x1 + 1  # 左边界点

        # 处理上一条扫描线
        x_upper, y_upper = xl, y1 + 1
        while x_upper <= xr:
            fill = False
            while getPixelColor(x_upper, y_upper) == oldColor:  # 如果是边界上的点，则找到其右边界的点
                fill = True
                x_upper += 1
            if fill:
                stack.append((x_upper - 1, y_upper))  # 将
                fill = False
            while getPixelColor(x_upper, y_upper) != oldColor and x_upper <= xr:
                x_upper += 1  # 重新找到位于填充区域的点

        # 处理下一条扫描线
        x_lower, y_lower = xl, y1 - 1
        while x_lower <= xr:
            fill = False
            while getPixelColor(x_lower, y_lower) == oldColor:  # 如果是边界上的点，则找到其右边界的点
                fill = True
                x_lower += 1
            if fill:
                stack.append((x_lower - 1, y_lower))
                fill = False
            while getPixelColor(x_lower, y_lower) != oldColor and x_lower <= xr:
                x_lower += 1  # 重新找到位于填充区域的点


def main(x, y, oldColor, newColor):
    _, ax = plt.subplots()
    plt.title('boundaryFill: ({},{})'.format(x, y))
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.gca().set_aspect('equal')
    re = generateRegion()
    b = boundary()
    # 画出边界
    for x0, y0 in b:
        ax.scatter(x0, y0, c=oldColor)
    scanLineFill(x, y, oldColor, newColor, ax)
    plt.show()


if __name__ == '__main__':
    main(1, 2, 'red', 'blue')
