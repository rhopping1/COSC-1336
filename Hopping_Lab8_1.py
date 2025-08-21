#Rachel Hopping
#Complete
#Read text.txt file and count uppercase, lowercase, digits, and whitespaces
#Display the counts of each


def main():
    #Get counts of upper, lower, digits, and whitespaces
    count_upper = 0
    count_lower = 0
    count_digit = 0
    count_white = 0

    #Open text file
    with open('text.txt', 'r') as this_file:
        line = this_file.readline()
        
        while line != '':
            for char in line:
                if char.isupper():
                    count_upper += 1
                elif char.islower():
                    count_lower += 1
                elif char.isdigit():
                    count_digit += 1
                elif char.isspace():
                    count_white += 1
            line = this_file.readline()
        
    

    #Display counts
    print(f'Uppercase letters: {count_upper}')
    print(f'Lowercase letters: {count_lower}')
    print(f'Digits: {count_digit}')
    print(f'Spaces: {count_white}')
    
main()
