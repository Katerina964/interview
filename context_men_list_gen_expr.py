some_data =[]
path = "https://"

with open(path, 'w') as f_obj:
    f_obj.write(some_data)

f_obj = open(path, 'w')
f_obj.write(some_data)
f_obj.close()


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
for x in fruits:
  if "a" in x:
    newlist.append(x)

generator = (num ** 2 for num in range(10)) 
for num in generator:
    print(num)    




