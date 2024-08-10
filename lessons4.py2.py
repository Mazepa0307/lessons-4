lst = [1,2,0,5,6,]
if not lst:
    result = 0
else:
    result = sum(lst[i] for i in range(0, len(lst), 2)) * lst[-1]
print(result)