#Rachel Hopping
#Complete
#Read the random number file from the earlier lab
#Display the numbers, the sum, the average, and the count of numbers


def main():
    try:
        with open('random_numbers.txt', 'r') as this_file:
            sum = 0
            count = 0
            line = this_file.readline()
            while line != '':
                number = int(line.rstrip('\n'))

                #Display the random numbers
                print(number) 

                #Calculate sum, average, and count
                sum += number
                count += 1
                line = this_file.readline()

            average = sum / count
            
        #Display the sum
        print(f'The sum of the random numbers is: {sum}')

        #Display the average
        print(f'The average of the random numbers is: {average:.2f}')

        #Display the count
        print(f'There are {count} numbers in the file.')

    except IOError:
        print(f'The file is not found.')
    except ValueError:
        print('The numbers in the list are not all integers.')
    except:
        print('There\'s an error with this program.')

main()

