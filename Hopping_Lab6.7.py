#Rachel Hopping
#Complete
#Take input from a user for how many numbers
#Generate a series of random numbers between 1-500 and save to a file

import random
import math

def main():
    #Get input from user
    try:
        total_numbers = int(input('Enter the number of random numbers in this file: '))

    except ValueError:
        print('The input must be an integer. Try again.')
        total_numbers = int(input('Enter the number of random numbers in this file: '))
    except:
        print('There was an error. Please try again.')
        total_numbers = int(input('Enter the number of random numbers in this file: '))

    #Open a new file
    with open('random_numbers.txt', 'w') as this_file:

        #Add the random numbers to the file
        for each in range(0, total_numbers):
            new_num = math.ceil(random.random() * 500)
            this_file.write(f'{new_num}\n')
        
main()
