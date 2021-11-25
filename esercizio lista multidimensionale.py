# l = []
# l2 = []
# for i in range (0,3):
#     l.append (l2)
# for j in range (0,3):
#     l2.append (0)


# print (l)
l = []
def multidimensional (list_element):
    nums = []
    for i in range (3):
        nums.append([])
        for j in range(3):
            nums [i].append(0)
    return nums
l = multidimensional (l)
print (l)




