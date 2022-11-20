try:
    tvalue = int(input('Enter total value: '))
    value = int(input('Enter value: '))
    percent = value * 100 / tvalue
    print(f'That is {percent}%')
except ValueError:
    exit('You need to enter a number. Run program again.')
except ZeroDivisionError:
    exit('Your total value cannot be zero.')