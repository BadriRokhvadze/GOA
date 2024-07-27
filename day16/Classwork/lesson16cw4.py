list = [1,8,3,2,6,9,4,7]
list1 = []

o = min(list)
oo = max(list)

list.remove(o)
list.remove(oo)


list1.append(o)
list1.append(oo)

print(list,list1)