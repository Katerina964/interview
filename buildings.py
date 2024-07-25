class Building:
    def __init__(self, left, right, height):
        self.left = left
        self.right = right
        self.height = height


def calculateSkylineArea(buildings):
    total_list = []

    for each in buildings:
        list_values = []

        for point in range(each.left, each.right + 1):           
            list_values.append(point)

        area = (each.right - each.left) * each.height
        list_values.insert(0, area)
        total_list.append(list_values)

    point_values = set(total_list[0][1:])
    areas = total_list[0][0]

    for each in total_list[1:]:
        each_set = set(each[1:])
        if not each_set.intersection(point_values):
            areas += each[0]
            point_values.update(each_set)

    return areas


buildings = [Building(2, 4, 1), Building(3, 4, 5), Building(5, 7, 1)]


print(calculateSkylineArea(buildings))
