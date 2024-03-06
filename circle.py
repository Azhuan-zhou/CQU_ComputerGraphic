import numpy as np
import matplotlib.pyplot as plt

plt.switch_backend('TKAgg')


def circlePoints(x0, y0, x, y, color, s=1):
    axis = np.array([
        [x, y, x, y, -x, -y, -x, -y],
        [y, x, -y, -x, -y, -x, y, x],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ])
    offset = np.array([
        [1, 0, x0],
        [0, 1, y0],
        [0, 0, 1]
    ])
    new_axis = np.matmul(offset, axis)
    plt.scatter(new_axis[0, 0], new_axis[1, 0], c=color, s=s)
    plt.scatter(new_axis[0, 1], new_axis[1, 1], c=color, s=s)
    plt.scatter(new_axis[0, 2], new_axis[1, 2], c=color, s=s)
    plt.scatter(new_axis[0, 3], new_axis[1, 3], c=color, s=s)
    plt.scatter(new_axis[0, 4], new_axis[1, 4], c=color, s=s)
    plt.scatter(new_axis[0, 5], new_axis[1, 5], c=color, s=s)
    plt.scatter(new_axis[0, 6], new_axis[1, 6], c=color, s=s)
    plt.scatter(new_axis[0, 7], new_axis[1, 7], c=color, s=s)
    plt.pause(0.00001)


def center(r, x0, y0):
    """
    中点画圆算法
    :param r: 圆的半径
    :return: None
    """
    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal')
    plt.xlim(-r + x0 - 1, r + x0 + 1)
    plt.ylim(-r + y0 - 1, r + y0 + 1)
    d = 1 - r  #
    x = 0
    y = r
    plt.title('Center: R={}, ({},{})'.format(r, x0, y0))
    plt.scatter(x0, y0, c='blue', s=5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    circlePoints(x0, y0, x, y, 'red')
    while x <= y:
        if d < 0:
            d = d + 3 + 2 * x
            x = x + 1
        else:
            d = d + 5 + 2 * (x - y)
            x = x + 1
            y = y - 1
        circlePoints(x0, y0, x, y, 'red')

    plt.show()
    plt.close()


def drewPixel(x0, y0, x, y, color, s=1):
    axis = np.array([
        [x, x, -x, -x],
        [y, -y, -y, y],
        [1, 1, 1, 1]
    ])
    offset = np.array([
        [1, 0, x0],
        [0, 1, y0],
        [0, 0, 1]
    ])
    new_axis = np.matmul(offset, axis)
    plt.scatter(new_axis[0, 0], new_axis[1, 0], c=color, s=s)
    plt.scatter(new_axis[0, 1], new_axis[1, 1], c=color, s=s)
    plt.scatter(new_axis[0, 2], new_axis[1, 2], c=color, s=s)
    plt.scatter(new_axis[0, 3], new_axis[1, 3], c=color, s=s)
    plt.pause(0.001)  # Introduce a pause to see the point


def centerBresenham(r, x0, y0):
    # 参数初始化
    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal')
    plt.xlim(-r + x0 - 1, r + x0 + 1)
    plt.ylim(-r + y0 - 1, r + y0 + 1)
    plt.title('Bresenham: R={}, ({},{})'.format(r, x0, y0))
    plt.scatter(x0, y0, c='blue', s=5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    d = 2 * (1 - r)
    y = r
    x = 0
    drewPixel(x0, y0, x, y, 'red')
    while y >= 0:
        # D点在圆内，从H,D中选择下一个点
        if d <= 0:
            H_D = 2 * (d + y) - 1
            # H_D小于零，选择H点（左边）
            if H_D <= 0:
                d = d + 2 * x + 3
                x = x + 1
            # H_D大于零，选择D点（左下角）
            else:
                d = d + 2 * (x - y + 3)
                x = x + 1
                y = y - 1
        else:
            D_V = 2 * (d - x) - 1
            # D_V小于零，选择D点
            if D_V <= 0:
                d = d + 2 * (x - y + 3)
                x = x + 1
                y = y - 1
            # D_V小于零，选择D点
            else:
                d = d - 2 * y + 3
                y = y - 1
        drewPixel(x0, y0, x, y, 'red')
    plt.show()
    plt.close()


if __name__ == '__main__':
    # center(100, 10, 10)
    centerBresenham(60, 20, 10)
