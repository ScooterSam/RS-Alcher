import numpy
import pyautogui
import bezier


def hanging_line(point1, point2):
    import numpy as np
    #
    # a = (point2[1] - point1[1]) / (np.cosh(point2[0]) - np.cosh(point1[0]))
    # b = point1[1] - a * np.cosh(point1[0])
    # x = np.linspace(point1[0], point2[0], 100)
    # y = a * np.cosh(x) + b
    #
    # return (x, y)
    nodes1 = np.asfortranarray(point1, point2)
    curve1 = bezier.curve(nodes1, degree=2)
    print(curve1)


interval = 1

while interval < 20:
    try:
        x, y = hanging_line([10, 10], [500, 500])
        #print(int(x[interval]), int(y[interval]))
       # pyautogui.moveTo(int(x[interval]), int(y[interval]), duration=0.1)
        interval += 1;
    except IndexError:
        print('No index for that number')

