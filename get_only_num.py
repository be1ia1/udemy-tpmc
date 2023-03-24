def get_only_num(somelist):
    return [i if type(i) is not str else 0 for i in somelist]


print(get_only_num([1,2,34,'fdf']))