lst = [1,2,0,5,6,0]
lst = [x for x in lst if x != 0] + [0] * lst.count(0)
print(lst)
