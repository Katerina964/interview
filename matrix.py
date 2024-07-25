m = 5
n = 5
s = [["0"] * m for x in range(n)]

# for each in s:
#     print(*each)

for r in range(len(s)):
    for e in range(len(s[r])):
        if r == e:
            s[r][e] = 2
        if r > e:
            s[r][e] = 1
        if r < e:
            s[r][e] = 3
    print(*s[r])    

rows = 7
coloms = 7

line_index_top = 0
line_start_index = 0
line_stop_index = rows
line_index_bot = coloms

elem = 0
numbers =  rows * coloms

s = [["0"] * rows for x in range(coloms)]

while elem < numbers:
    
    for row in range(line_start_index, line_stop_index):
       elem += 1
       s[line_index_top][row] = elem
    line_index_top += 1   
    
    if elem < numbers:
        for row in s[line_index_top:line_index_bot]:
            elem += 1
            row[line_stop_index - 1] = elem
        line_stop_index -= 1
    
    if elem < numbers:
        for row in reversed(range(line_start_index, line_stop_index)):
            elem += 1
            s[line_index_bot - 1][row] = elem
        line_index_bot -= 1
    
    if elem < numbers:
        for row in reversed(s[line_index_top:line_index_bot]):
            elem += 1
            row[line_start_index] = elem
        line_start_index += 1
       

for i in s:
    print(*i, "    ")  


