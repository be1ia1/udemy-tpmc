import random

lower_bound = int(input('Enter the lower bound: '))
upper_bound = int(input('Enter the upper bound: '))


for i in range(21):
    print(random.randrange(lower_bound,upper_bound+1))