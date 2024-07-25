square_values = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]


def is_magic_square(square_values):
    total_dict = {str(x): [] for x in range(len(square_values))}
    total_dict.update({"diagonal_1": [], "diagonal_2": []})

    for row_index, row in enumerate(square_values):
        for elem_index, elem in enumerate(row):
            total_dict[str(elem_index)].append(elem)
            if row_index == elem_index:
                total_dict["diagonal_1"].append(elem)

        for elem_index, elem in enumerate(reversed(row)):
            if row_index == elem_index:
                total_dict["diagonal_2"].append(elem)
    result = {sum(x) for x in square_values}

    for key, value in total_dict.items():
        result.add(sum(value))

    return len(result) == 1


print(is_magic_square(square_values))
