list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}

# 1
for item in list_data:
    print(item * 2)

print("\n")

# 2
for items in embedded_lists:
    print(items)
    for items_within in items:
        print(items_within)

print("\n")

# 3
for data in dict_data:
    print(data)

print("\n")

# 4
for data in dict_data:
    print(dict_data[data].values())

# print("\n")

# 5
print(dict_data.values())
i = 0
for data in dict_data.values():
    i = i + 1
    print(i)
    print(type(data))
    print(data)

# 6
for dict_items in dict_data.values():
    for value in dict_items.values():
        print(value)

print("\n")
print("\n")

# 7
for dict_items in dict_data.values():
    print(dict_items['money'])

print("\n")

# 8
for d in list_data:
    x = d
    if x < 3:
        print("less than 3")
    elif x == 3:
        print("i found 3")
    else:
        print("more than 3")
