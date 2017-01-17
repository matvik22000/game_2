def intersect_classes(class_1, class_2):
    x1 = class_1.x
    x2 = class_2.x
    y1 = class_1.y
    y2 = class_2.y
    x1_size = class_1.x_size
    x2_size = class_2.x_size
    y1_size = class_1.y_size
    y2_size = class_2.y_size
    result = intersect(x1, x2, y1, y2, x1_size, x2_size, y1_size, y2_size)
    return result


def intersect(s1_x, s2_x, s1_y, s2_y, s1_size_x, s1_size_y, s2_size_x, s2_size_y):
    if ((s1_x > s2_x - s1_size_x) and (s1_x < s2_x + s2_size_x)) and (s1_y > s2_y - s1_size_y) and (
        s1_y < s2_y + s2_size_y):
        return True
    else:
        return False
def intersect_class(class_1, x2, y2, x_size2, y_size2):
    x1 = class_1.x
    y1 = class_1.y
    x1_size = class_1.x_size
    y1_size = class_1.y_size
    result = intersect(x1, x2, y1, y2, x1_size, x_size2, y1_size, y_size2)
    return result