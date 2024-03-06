import numpy as np
import matplotlib.pyplot as plt

plt.switch_backend('TKAgg')


# dd
def DDA(x1, y1, x2, y2, ax):
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
        ax.scatter(x_, y_, c='blue', s=1)
    if step_x == 0:  # k = -inf
        y_ = np.arange(y1, y2 + step_y, int(step_y))
        x_ = np.zeros_like(y_)
        x_[:] = x1
        ax.scatter(x_, y_, c='blue', s=1)
    ax.scatter(int(x + 0.5), int(y + 0.5), c='blue', s=1)
    plt.pause(0.01)
    while True:
        if int(x + 0.5) == x2 or int(y + 0.5) == y2:
            break
        x = x + step_x
        y = y + step_y
        ax.scatter(int(x + 0.5), int(y + 0.5), c='blue', s=1)


def drawWindow(XL, XR, YB, YT, ax):
    ax.plot([XL, XL, XR, XR, XL], [YB, YT, YT, YB, YB], c='red')


def LineClip(x1, y1, x2, y2, XL, XR, YB, YT, ax):
    """
    直线裁切
    :param x1: 起始点x
    :param y1: 起始点y
    :param x2: 终点x
    :param y2: 终点y
    :param XL: x左边界
    :param XR: x右边界
    :param YB: y上边界
    :param YT: y下边界
    :return:
    """
    u1, u2 = 0, 1  # 线段裁切的范围在[0,1]
    dx, dy = x2 - x1, y2 - y1
    u = [u1, u2]
    if ClipT(-dx, x1 - XL, u):  # 左边界
        if ClipT(dx, XR - x1, u):  # 右边界
            if ClipT(-dy, y1 - YB, u):  # 上边界
                if ClipT(dy, YT - y1, u):  # 下边界
                    print(x1 + u[0] * dx, y1 + u[0] * dy, x1 + u[1] * dx, y1 + u[1] * dy)
                    DDA(x1 + u[0] * dx, y1 + u[0] * dy, x1 + u[1] * dx, y1 + u[1] * dy, ax)


def ClipT(p, q, u):
    if p < 0:  # 线段由外到内
        r = q / p  # 边界裁切比例
        if r > u[1]:  # 边界裁切的比例大于1
            return False
        if r > u[0]:
            print('u1:', r)
            u[0] = r
    elif p > 0:  # 线段由内到外
        r = q / p
        if r < u[0]:
            return False
        if r < u[1]:
            print('u2:', r)
            u[1] = r
    else:
        return q >= 0
    return True


def main():
    _, ax = plt.subplots()
    XL, XR, YB, YT = 100, 200, 100, 200
    #x1, y1, x2, y2 = 17, 74, 274, 223  # 两端点在裁剪框外
    #x1, y1, x2, y2 = 58, 131, 174, 174  # 一个端点在裁剪框外
    x1, y1, x2, y2 = 135,120,171,190 # 两个端点在裁剪框内
    #x1, y1, x2, y2 = 17, 74, 74, 251  # 两端点在裁剪框外
    ax.scatter(x1, y1, c='black', s=5)
    plt.legend('Start')
    ax.scatter(x2, y2, c='black', s=5)
    plt.legend('end')

    plt.title('Liang-Barsky:({},{})->({},{})'.format(x1, y1, x2, y2))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(0, 300)
    plt.ylim(0, 300)
    plt.grid(True)
    plt.gca().set_aspect('equal')
    drawWindow(XL, XR, YB, YT, ax)
    LineClip(x1, y1, x2, y2, XL, XR, YB, YT, ax)
    plt.show()


if __name__ == '__main__':
    main()
