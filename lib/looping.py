#!/usr/bin/env python3
import math

def happy_new_year():
    Counter = 10
    while Counter > 0:
        print(Counter)
        Counter = Counter - 1
    
    print('Happy New Year!')

def square_integers(int_list):
    squared_list = []
    for integer in int_list:
        squared_list.append(integer ** 2)
    return squared_list


def fizzbuzz():
    count = 1
    while count < 101:
        if count % 3 == 0 and count % 5 == 0:
            print('FizzBuzz')
        elif count % 3 == 0:
            print('Fizz')
        elif count % 5 == 0:
            print('Buzz')
        else:
            print(count)
        count += 1