stats_file = 'files/stats.txt'
with open(stats_file) as fo:
    stats = fo.readlines()
    start = stats[0].split(',')
    counter = int(start[0])
    head_counter = int(start[1])
    heads = float(start[2])
while True:
    counter += 1 
    uchoice = input('Enter "head" or "tail": ')
    chunk = 100 / counter
    print(chunk)
    if uchoice == 'head':
        head_counter += 1
    heads = chunk * head_counter
    with open(stats_file, 'a') as foa:
        foa.writelines([f'\n{counter},{head_counter},{heads}'])
