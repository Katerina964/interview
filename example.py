# people = [x for x in range(1, 10)]
people = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]

def delete_each_occurrency(n, people):    
    counter = 0
    for each in people[:]:
        counter += 1
        print(f"{each}: {counter}")
        if counter % n == 0:
            people.remove(each)

    return people


from copy import copy
people_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
# people_1 = [x for x in range(1, 10)]           
def delete_each_occurrency_1(n, people):
    for each in copy(people_1):
        print(each)
        if each % n == 0:
            people.remove(each)

    return people

print(delete_each_occurrency(3, people))

print(delete_each_occurrency_1(3, people_1))