import circle_line
import csv


def circle_surface_coordinate(a, b, r):
    """通过圆的半径，圆心坐标在(a,b)，求出圆的表面
            args:
                a - 圆心坐标X(int)
                b - 圆心坐标Y(int)
                r - 圆的半径(int)
            return:
                圆的表面的坐标X，坐标Y的值列表[[x1,y1,x1,yn],[x2,y2,x2,yn-2]...]
    """
    circle_line_coordinate_list = circle_line.circle_line_coordinate(a, b, r)
    circle_surface_coordinate_list = []
    c_length_half = len(circle_line_coordinate_list) // 2
    for i in range(0, c_length_half):
        circle_surface_coordinate_list.append([circle_line_coordinate_list[i][0],
                                               circle_line_coordinate_list[i][1],
                                               circle_line_coordinate_list[i][0],
                                               circle_line_coordinate_list[c_length_half+i][1]])
    return circle_surface_coordinate_list


if __name__ == '__main__':
    cl = circle_surface_coordinate(0, 0, 50)
    path = './circle_surface.csv'

    with open(path, 'w', newline="") as f:
        csv_write = csv.writer(f)
        for item in cl:
            data_row = item
            csv_write.writerow(data_row)
