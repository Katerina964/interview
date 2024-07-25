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

# square_values = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]


# def is_magic(square_values):
#     len_square = len(square_values)
#     result_top = sum(square_values[0])
#     result_bot = sum(square_values[-1])

#     if result_top == result_bot:
#         result_left = []
#         result_right = []
#         result_diagonal_first = []
#         result_diagonal_second = []

#         for count, row in enumerate(square_values[:]):
#             for value in range(len_square):
#                 if value == len_square - 1:
#                     result_left.append(row[-1])
#                 if value == 0:
#                     result_right.append(row[0])

#                 if value == count:
#                     result_diagonal_first.append(row[value])

#             for value in reversed(range(len_square)):
#                 if value == count:
#                     result_diagonal_second.append(row[value])
#             print(result_diagonal_second)
#             print(result_diagonal_first)
#     else:
#         return False

#     if (
#         result_bot
#         == sum(result_left)
#         == sum(result_right)
#         == sum(result_diagonal_first)
#         == sum(result_diagonal_second)
#     ):
#         return True
#     else:
#         return False


# print(is_magic(square_values))
