my_list = [[1, 4], [3, 1], [5, 2], [2, 9]]

sorted_list = sorted(my_list, key=lambda x: x[1])

print("Sorted list based on second element:")
print(sorted_list)
