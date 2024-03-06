import numpy as np
import matplotlib.pyplot as plt

plt.switch_backend('TKAgg')


# dd
def DDA(x1, y1, x2, y2):
    plt.figure(figsize=(6, 6))
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    # 0<abs(k)<1的情况
    if np.abs(y2 - y1) <= np.abs(x2 - x1):
        step = np.abs(x2 - x1)
    else:
        step = np.abs(y2 - y1)
    x = x1
    y = y1
    step_x = (x2 - x1) / step
    step_y = (y2 - y1) / step
    # 如果 k = 0 或者 k 为无穷，不进入循环
    if step_y == 0:  # k = 0
        x_ = np.arange(x1, x2 + step_x, int(step_x))
        y_ = np.zeros_like(x_)
        y_[:] = y1
        plt.scatter(x_, y_, c='red', s=1)
    if step_x == 0:  # k = -inf
        y_ = np.arange(y1, y2 + step_y, int(step_y))
        x_ = np.zeros_like(y_)
        x_[:] = x1
        plt.scatter(x_, y_, c='red', s=1)
    plt.scatter(int(x + 0.5), int(y + 0.5), c='red', s=1)
    while True:
        if x == x2 or y == y2:
            break
        x = x + step_x
        y = y + step_y
        plt.scatter(int(x + 0.5), int(y + 0.5), c='red', s=1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('DDA:({},{})->({},{})'.format(x1, y1, x2, y2))
    plt.grid(True)
    plt.show()


# 中点画线算法
def center(x1, y1, x2, y2):
    plt.figure(figsize=(6, 6))
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    dx = np.abs(x2 - x1)
    dy = np.abs(y2 - y1)
    sx = 1 if x2 > x1 else -1  # x增加的方向
    sy = 1 if y2 > y1 else -1  # y增加的方向
    a = y1 - y2
    b = x2 - x1
    d = 2 * sx * a + sy * b if dx >= dy else 2 * sy * b + sx * a
    x, y = x1, y1

    if dy == 0:  # k =0
        x_ = np.arange(x1, x2 + sx, int(sx))
        y_ = np.zeros_like(x_)
        y_[:] = y1
        plt.scatter(x_, y_, c='red', s=1)
    if dx == 0:  # k = -inf
        y_ = np.arange(y1, y2 + sy, int(sy))
        x_ = np.zeros_like(y_)
        x_[:] = x1
        plt.scatter(x_, y_, c='red', s=1)
    plt.scatter(x, y, c='red', s=1)
    while x != x2 and y != y2:

        if dx >= dy:  # 斜率绝对值小于1
            x += sx
            if sx * sy * d <= 0:  # 中点在直线下方, 取（x+sx,y+sy）
                d += 2 * (sx * a + sy * b)
                y += sy
            else:  # 中点在直线上方, 取（x+sx,y）
                d += 2 * sx * a
            plt.scatter(x, y, c='red',s=1)
        else:  # 斜率绝对值大于1
            y += sy
            if sx * sy * d <= 0:  # 中点在直线左方, 取（x,y+sy）
                d += 2 * sy * b
            else:  # 中点在直线右方, 取（x+sx,y+sy）
                d += 2 * (sx * a + sy * b)
                x += sx
            plt.scatter(x, y, c='red', s=1)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Center:({},{})->({},{})'.format(x1, y1, x2, y2))
    plt.grid(True)
    plt.show()


def Bresenham(x1, y1, x2, y2):
    plt.figure(figsize=(6, 6))
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    x = x1
    y = y1
    dx = np.abs(x2 - x1)
    dy = np.abs(y2 - y1)
    sx = 1 if x2 > x1 else -1  # x增加的方向
    sy = 1 if y2 > y1 else -1  # y增加的方向

    if dy == 0:  # k =0
        x_ = np.arange(x1, x2 + sx, int(sx))
        y_ = np.zeros_like(x_)
        y_[:] = y1
        plt.scatter(x_, y_, c='red', s=1)
    if dx == 0:  # k = -inf
        y_ = np.arange(y1, y2 + sy, int(sy))
        x_ = np.zeros_like(y_)
        x_[:] = x1
        plt.scatter(x_, y_, c='red', s=1)

    flag = False  # 是否互换了dx dy

    if dy > dx:  # k的绝对值大于1
        dx, dy = dy, dx
        flag = True
    e = -dx
    plt.scatter(x, y, c='red', s=1)
    while x != x2 and y != y2:
        e = e + 2 * dy
        if e >= 0:
            if not flag:  # 如果没有交换
                y += sy
            else:  # 如果交换了
                x += sx
            e = e - 2 * dx
        if not flag:  # # 如果没有交换
            x += sx
        else:
            y += sy
        plt.scatter(x, y, c='red', s=1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Bresenham:({},{})->({},{})'.format(x1, y1, x2, y2))
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    DDA(50, 0, 50, 80)
    DDA(0, 50, 80, 50)
    DDA(20, 20, 80, 50)
    DDA(20, 80, 80, 50)
    DDA(20, 20, 80, 100)
    DDA(20, 80, 80, 0)
    center(50, 0, 50, 80)
    center(0, 50, 80, 50)
    center(20, 20, 80, 50)
    center(20, 80, 80, 50)
    center(20, 20, 80, 100)
    center(20, 80, 80, 0)
    Bresenham(50, 0, 50, 80)
    Bresenham(0, 50, 80, 50)
    Bresenham(20, 20, 80, 50)
    Bresenham(20, 80, 80, 50)
    Bresenham(20, 20, 80, 100)
    Bresenham(20, 80, 80, 0)
