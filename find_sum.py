def find_sum(**kwargs):
    print(kwargs.values())
    return sum(kwargs.values())
    
print(find_sum(name=9))