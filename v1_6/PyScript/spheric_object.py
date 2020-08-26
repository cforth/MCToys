import circle_surface
import csv


def spheric_object_coordinate(a, b, z, r):
    spheric_object_coordinate_list = []
    for r_index in range(0, r+1):
        cl = circle_surface.circle_surface_coordinate(a, b, int(round((r**2 - r_index**2)**0.5)))
        for cl_i in cl:
            spheric_object_coordinate_list.append(cl_i + [z+r_index])

    for r_index in range(r, -1, -1):
        cl = circle_surface.circle_surface_coordinate(a, b, int(round((r**2 - r_index**2)**0.5)))
        for cl_i in cl:
            spheric_object_coordinate_list.append(cl_i + [z-r_index])

    return spheric_object_coordinate_list


if __name__ == '__main__':
    cl = spheric_object_coordinate(0, 0, 0, 40)
    path = './spheric_object.csv'

    with open(path, 'w', newline="") as f:
        csv_write = csv.writer(f)
        for item in cl:
            data_row = item
            csv_write.writerow(data_row)
