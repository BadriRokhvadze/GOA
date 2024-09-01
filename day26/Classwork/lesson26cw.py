def num_filter(num):
    even_nums = [i for i in num if i % 2 == 0]
    return even_nums


lst = [1,2,3,4,5,6,7,8,9,10]
print(num_filter(lst))