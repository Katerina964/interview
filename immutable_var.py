color_list = ["blue", "white"]
print(id(color_list))   # the same
color_list.append("yellow")
color_list += ["pink"]
print(id(color_list)) # the same


color_tuple = ("blue", "white")
print(id(color_tuple)) # different
color_tuple += "yellow",
print(id(color_tuple)) # different
