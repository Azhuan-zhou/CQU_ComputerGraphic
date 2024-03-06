import numpy as np
import matplotlib.pyplot as plt
from numpy import cos as cos
from numpy import sin as sin
from numpy import pi as pi

plt.switch_backend('TKAgg')


def drewPixel(x0, y0, theta, x, y, color, s=5):
    theta = theta / 180 * pi
    axis = np.array([
        [x, x, -x, -x],
        [y, -y, -y, y],
        [1, 1, 1, 1]
    ])
    offset_1 = np.array(
        [
            [cos(theta), -sin(theta), 0],
            [sin(theta), cos(theta), 0],
            [0, 0, 1]
        ]
    )
    offset_2 = np.array([
        [1, 0, x0],
        [0, 1, y0],
        [0, 0, 1]
    ])
    new_axis = np.matmul(offset_2, np.matmul(offset_1, axis))
    plt.scatter(new_axis[0, 0], new_axis[1, 0], c=color, s=s)
    plt.scatter(new_axis[0, 1], new_axis[1, 1], c=color, s=s)
    plt.scatter(new_axis[0, 2], new_axis[1, 2], c=color, s=s)
    plt.scatter(new_axis[0, 3], new_axis[1, 3], c=color, s=s)
    plt.pause(0.01)


def center(a, b, x0, y0, theta):
    """
    椭圆的中点绘制算法
    """
    plt.figure(figsize=(6, 6))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-30, 30)
    plt.ylim(-30, 30)
    plt.grid(True)
    plt.title('Ellipse: a={}, b={}, ({},{}), theta={}'.format(a, b, x0, y0, theta))
    plt.scatter(x0, y0, c='blue', s=5)
    plt.gca().set_aspect('equal')
    flag = 1  # 是否交换a,b
    x = 0
    y = b
    if b > a:  # 交换
        a, b = b, a
        x, y = 0, b  # (y,x)
        flag = -1
    d_1 = (b ** 2) + (a ** 2) * (0.25 - b)
    # 先绘制椭圆的上半部分
    while True:
        if flag == 1:
            drewPixel(x0, y0, theta, x, y, "red")
        else:
            drewPixel(x0, y0, theta, y, x, "red")
        # 中点在椭圆内,取（x+1,y）
        if d_1 <= 0:
            d_1 = d_1 + (b ** 2) * (2 * x + 3)
            x = x + 1
            if (b ** 2) * (x + 1) > (a ** 2) * (y - 0.5):  # 当下一个中点是切点的时候
                x = x - 1
                break
        # 中点在椭圆外,取（x+1,y-1）
        else:
            d_1 = d_1 + (b ** 2) * (2 * x + 3) + (a ** 2) * (2 - 2 * y)
            x = x + 1
            y = y - 1
            if (b ** 2) * (x + 1) > (a ** 2) * (y - 0.5):
                x = x - 1
                y = y + 1
                break
    # 椭圆的下半部分
    d_2 = (b ** 2) * ((x + 0.5) ** 2) + (a ** 2) * ((y - 1) ** 2) - (a ** 2) * (b ** 2)
    while y > 0:
        if d_2 > 0:
            d_2 = d_2 + a ** 2 * (3 - 2 * y)
            y = y - 1
        else:
            d_2 = d_2 + b ** 2 * (2 * x + 2) + a ** 2 * (3 - 2 * y)
            x = x + 1
            y = y - 1
        if flag == 1:
            drewPixel(x0, y0, theta, x, y, 'red')
        else:
            drewPixel(x0, y0, theta, y, x, 'red')
    plt.show()


if __name__ == '__main__':
    center(24, 16, 2, 2, 30)
