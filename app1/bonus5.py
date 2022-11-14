waiting_list = ['sen', 'ben', 'john']
waiting_list.sort(reverse=True)
for i, j in enumerate(waiting_list, start=1):
    print(f'{i}. {j.capitalize()}')