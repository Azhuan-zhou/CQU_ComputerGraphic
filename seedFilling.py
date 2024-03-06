import matplotlib.pyplot as plt
plt.switch_backend('TKAgg')


def generateRegion():
    line1 = [(0, i) for i in range(0, 4)]
    line2 = [(i, 3) for i in range(1, 3)]
    line3 = [(2, i) for i in range(4, 5)]
    line4 = [(3, i) for i in range(4, 7)]
    line5 = [(i, 6) for i in range(4, 8)]
    line6 = [(7, i) for i in range(5, 2, -1)]
    line7 = [(i, 3) for i in range(6, 3, -1)]
    line8 = [(4, i) for i in range(2, 0, -1)]
    line9 = [(i, 0) for i in range(4, 0, -1)]
    Rectangle = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + line9
    return Rectangle


region = generateRegion()
fill_already = []


def getPixelColor(x, y):
    if (x, y) in region:
        return 'red'  # 边界颜色
    elif (x, y) in fill_already:
        return 'blue'  # 填充颜色
    else:
        return 0


def boundaryFill4(x, y, fillColor, boundaryColor, ax):
    color = getPixelColor(x, y)
    if color is boundaryColor:
        return
    if color is fillColor:
        return
    else:
        fill_already.append((x, y))
        ax.scatter(x, y, c=fillColor)
        plt.pause(0.01)
        boundaryFill4(x + 1, y, fillColor, boundaryColor, ax)
        boundaryFill4(x - 1, y, fillColor, boundaryColor, ax)
        boundaryFill4(x, y + 1, fillColor, boundaryColor, ax)
        boundaryFill4(x, y - 1, fillColor, boundaryColor, ax)


def boundaryFill4_stack(x, y, fillColor, boundaryColor, ax):
    stack = [(x, y)]  # 创建一个栈
    while stack:
        x0, y0 = stack.pop()  # 获取栈顶元素
        color = getPixelColor(x0, y0)
        if color == 0:  # 如果该点不是边界点，或者不是已经填充的点
            fill_already.append((x0, y0))
            ax.scatter(x0, y0, c=fillColor)
            plt.pause(0.01)
            stack.append((x0 + 1, y0))
            stack.append((x0 - 1, y0))
            stack.append((x0, y0 + 1))
            stack.append((x0, y0 - 1))


def boundaryFill8_stack(x, y, fillColor, boundaryColor, ax):
    stack = [(x, y)]  # 创建一个栈
    while stack:
        x0, y0 = stack.pop()  # 获取栈顶元素
        color = getPixelColor(x0, y0)
        if color == 0:  # 如果该点不是边界点，或者不是已经填充的点
            fill_already.append((x0, y0))  # 将满足条件的点放入已经填充点的列表中
            ax.scatter(x0, y0, c=fillColor)
            plt.pause(0.01)
            stack.append((x0 + 1, y0))
            stack.append((x0 - 1, y0))
            stack.append((x0, y0 + 1))
            stack.append((x0, y0 - 1))
            stack.append((x0 + 1, y0 + 1))
            stack.append((x0 + 1, y0 - 1))
            stack.append((x0 - 1, y0 + 1))
            stack.append((x0 - 1, y0 - 1))


def boundaryFill8(x, y, fillColor, boundaryColor, ax):
    color = getPixelColor(x, y)
    if color is boundaryColor:
        return
    if color is fillColor:
        return
    else:
        fill_already.append((x, y))
        ax.scatter(x, y, c=fillColor)
        plt.pause(0.01)
        boundaryFill8(x + 1, y, fillColor, boundaryColor, ax)
        boundaryFill8(x - 1, y, fillColor, boundaryColor, ax)
        boundaryFill8(x, y + 1, fillColor, boundaryColor, ax)
        boundaryFill8(x, y - 1, fillColor, boundaryColor, ax)
        boundaryFill8(x + 1, y + 1, fillColor, boundaryColor, ax)
        boundaryFill8(x + 1, y - 1, fillColor, boundaryColor, ax)
        boundaryFill8(x - 1, y + 1, fillColor, boundaryColor, ax)
        boundaryFill8(x - 1, y - 1, fillColor, boundaryColor, ax)
        plt.pause(0.01)


def main(x, y, fillColor, boundaryColor):
    _, ax = plt.subplots()
    plt.title('boundaryFill: ({},{})'.format(x, y))
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.gca().set_aspect('equal')
    re = generateRegion()
    # 画出边界
    for x0, y0 in re:
        ax.scatter(x0, y0, c=boundaryColor)
    boundaryFill8_stack(x, y, fillColor, boundaryColor, ax)
    plt.show()


if __name__ == '__main__':
    main(1, 2, 'blue', 'red')
