#Rachel Hopping
#Complete
#Write a function that creates a list of 10 integers and a number n
#Write second function that returns all numbers from the original list greater than n
#Display the original list, n, and all the numbers that are greater than n

def main():
    search_list = []

    #Create the list
    for i in range(10):
        add_to_list = int(input('Enter an integer: '))
        search_list.append(add_to_list)

    #Get the n
    number = int(input('Enter the integer to compare the list to: '))    

    #Get the list of numbers larger than n
    greater_than_list = display_larger(search_list, number)

    #Display the list and n and larger than list
    print(f'The original list of integers: {search_list}')
    print(f'Number: {number}')
    print(f'The list of integers larger than {number}: {greater_than_list}')
    

def display_larger(list, n):
    #list comprehension
    return [num for num in list if num > n]
    

main()
