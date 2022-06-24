import csv
import alphashape

def get_outline(points):
    alpha_shape = alphashape.alphashape(points, 0)
    return str(alpha_shape)

def create_shape(points, label):
    feature = "polygon"
    show_points = "true"
    fill_color = "165 63 91 100"
    shape = [get_outline(points), feature, show_points, label, fill_color]

    return shape

def create_csv(headers, rows, file_name):
    with open(file_name + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(headers)
        for row in rows:
            writer.writerow(row)

'''
    Given a list of points, a list of labels, and a file name, this function creates a CSV
    for JMARS shape layer

    This functions accepts multiple shapes at a time and outputs them all into a single CSV file.
    As a result, the points_list is a 2D list of the following format

    [
        [(0, 0), (0, 1), (1, 1)],
        [(3, 5), (3, 6), (4, 6)],
        [(-2, -4), (-3, -4), (-4, -4)],
    ]

    Each element in the list is a list of tuples that represents latitude and longitude

'''
def multiple_points_to_csv(points_list, labels_list, file_name):
    headers = ["geometry", "Feature:string", "ShowPoints:boolean", "Label:string", "Fill Color:color"]
    
    shapes = []
    for index, points in enumerate(points_list):
        new_shape = create_shape(points, labels_list[index])
        shapes.append(new_shape)
        

    create_csv(headers, shapes, file_name)

if __name__ == "__main__":
    
    #example for testing purpose
    points = [
        (0, 0), (0, 1), (0, 2), (0, 3),
        (1, 3), (1, 2), (1, 1), (1, 0),
        (2, 0), (2, 1), (2, 2), (2, 3),
        (3, 3), (3, 2), (3, 1), (3, 0),
        (3, -1), (2, -1), (1, -1), (0, -1),
        (0, 0)
    ]

    points_list = [points, points, points]
    labels_list = ["shape_1", "shape_2", "shape_3"]
    file_name= "testing"

    multiple_points_to_csv(points_list, labels_list, file_name)
