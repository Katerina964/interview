# Given arrival and departure times of all trains that reach a railway station. 
# Find the minimum number of platforms required for the railway station so that no train is kept waiting.
# Consider that all the trains arrive on the same day and leave on the same day.
#  Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. 
# At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms.
import copy

# n = 6
# arr = ["0900", "0940", "0950", "1100", "1500", "1800"] 
# dep = ["0910", "1200", "1120", "1130", "1900", "2000"]
# arr = ["0900"] 
# dep = ["1000"]

n = 3
arr = ["1000", "0935", "1100"] 
dep = ["1200", "1240", "1130"]

# n = 3
# arr = ["0900", "1235", "1100"] 
# dep = ["1000", "1240", "1200"]

def station_count(arr: list, dep: list, n: int):
    arr_hours = [int(x[:2]) if x[0] != "0" else int(x[1]) for x in arr]
    arr_min = [int(x[2:]) if x[2] != "0" else int(x[3]) for x in arr]

    dep_hours = [int(x[:2]) if x[0] != "0" else int(x[1]) for x in dep]
    dep_min = [int(x[2:]) if x[2] != "0" else int(x[3]) for x in dep]

    duration_list = []
    for each in zip(arr_hours, dep_hours, arr_min, dep_min):
        duration_set = set()
        if each[0] == each[1]:
           for i in range(each[2], each[3]+1):            
            minutes = str(i) if i >= 10 else "0" + str(i)
            duration_set.add(str(each[0]) + minutes)
        else:
            for i in range(each[2], 60):               
                minutes = str(i) if i >= 10 else "0" + str(i)
                duration_set.add(str(each[0]) + minutes)
            for h in range(each[0] + 1, each[1]):
                for m in range(0, 60):
                   minutes = str(m) if m >= 10 else "0" + str(m)
                   duration_set.add(str(h) + minutes)
            for i in range(0, each[3] + 1):
                minutes = str(i) if i >= 10 else "0" + str(i)
                duration_set.add(str(each[1]) + minutes)

        duration_list.append(duration_set)

    count_list = []   
    for each in duration_list:
        count = 0
        for train in duration_list:
            if not train.intersection(each):
                count += 1
                if  count == (len(duration_list) - 1):           
                    count_list.append(each)

    station_number = 1 if len(count_list) == n else n - len(count_list)
    return station_number





        

print(station_count(arr, dep, n))   

        

    