import csv
import copy


def circle_y_coordinate_up(x, r):
    """通过圆的坐标X，计算圆的曲线的上半部分的坐标Y，圆心坐标在(0,0)
        args:
            x - 圆曲线的坐标X(int)
            r - 圆的半径(int)
        return:
            圆的曲线的上半部分的坐标Y(int)
    """
    y_coordinate = (r**2 - (x-r)**2)**0.5 + r
    return int(round(y_coordinate))


def circle_y_coordinate_down(x, r):
    """通过圆的坐标X，计算圆的曲线的下半部分的坐标Y，圆心坐标在(0,0)
            args:
                x - 圆曲线的坐标X(int)
                r - 圆的半径(int)
            return:
                圆的曲线的上半部分的坐标Y(int)
    """
    y_coordinate = r - (r**2 - (x-r)**2)**0.5
    return int(round(y_coordinate))


def circle_line_coordinate(a, b, r):
    """通过圆的半径，圆心坐标在(a,b)，求出圆的曲线的坐标X，坐标Y的值
            args:
                a - 圆心坐标X(int)
                b - 圆心坐标Y(int)
                r - 圆的半径(int)
            return:
                圆的曲线的坐标X，坐标Y的值列表[[x1,y1],[x2,y2]...[xn,yn]]
    """
    circle_coordinate_up_list = []
    step = 1
    for i in range(0, 2*r, step):
        x = i + a - r
        y = circle_y_coordinate_up(i, r) + b - r
        circle_coordinate_up_list.append([x, y])
    circle_coordinate_up_list.append([2*r + a - r, circle_y_coordinate_up(2*r, r) + b - r])

    # 补全yn与yn-1之间的空隙值，使得y坐标的解在整数上是连续的。完成圆的曲线的上半部分
    circle_coordinate_up_result = []
    for i in range(0, len(circle_coordinate_up_list)-1):
        x = circle_coordinate_up_list[i][0]
        y = circle_coordinate_up_list[i][1]
        x_next = circle_coordinate_up_list[i+1][0]
        y_next = circle_coordinate_up_list[i+1][1]
        circle_coordinate_up_result.append([x, y])
        if y_next > y + 1:
            for j in range(y+1, y_next):
                circle_coordinate_up_result.append([x, j])
        elif y_next < y - 1:
            for j in range(y-1, y_next, -1):
                circle_coordinate_up_result.append([x_next, j])
    circle_coordinate_up_result.append(circle_coordinate_up_list[len(circle_coordinate_up_list)-1])

    # 补全圆曲线的下半部分
    result_list = copy.deepcopy(circle_coordinate_up_result)
    for i in circle_coordinate_up_result:
        result_list.append([i[0], 2 * b - i[1]])

    return result_list


if __name__ == '__main__':
    cl = circle_line_coordinate(0, 0, 100)
    path = './circle_line.csv'

    with open(path, 'w', newline="") as f:
        csv_write = csv.writer(f)
        for item in cl:
            data_row = item
            csv_write.writerow(data_row)
