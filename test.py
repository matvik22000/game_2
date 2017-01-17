def intersect(s1_x, s2_x, s1_y, s2_y, s1_size_x, s1_size_y, s2_size_x, s2_size_y):
    if ((s1_x > s2_x - s1_size_x) and (s1_x < s2_x + s2_size_x)) and (s1_y > s2_y - s1_size_y) and (s1_y < s2_y + s2_size_y):
        return True
    else:
        return False
a = intersect(20 ,20, 10, 10, 100, 100, 100, 100)
print a