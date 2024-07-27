o = [1,2,3,4,5,6,7]
o1 = ['a','b','c','d','e','f','g']
o2 = []
o3 = 0
o4 = 0

for i in range(7):
    o3 = o3 + 1
    o4 = o4 + 1
    o2.insert(o4,o[o3])
    o2.insert(o4,o1[o3])
    #vergavige