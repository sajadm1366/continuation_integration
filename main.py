'''
A simple program
'''

# import libraries
import numpy as np

def add_fucntion(x, y):
    return x + y

def multiply_function(x, y):
    return x ** y

def main():
    print(f'2 plus 3 is: {add_fucntion(2, 3)}')
    print(f'2 multiply 3 is: {multiply_function(2, 3)}')


if __name__ == '__main__':
    main()


