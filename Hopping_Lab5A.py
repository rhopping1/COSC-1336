#Rachel Hopping
#Complete
#Write two functions, main and determine_stars
#main will get 5 inputs between 1-10 using a loop then calculate average score
#determine_stars will get average and display number of stars based on chart

def main():
    score = 0
    for count in range(5):
        rank = int(input('Enter your critic rating between 0-10: '))
        # Make sure rank is not less than 0 or greater than 10.
        while rank < 0 or rank > 10:
            print('The score cannot be negative or higher than 10. Try again.')
            rank = int(input('Enter your critic rating between 0-10: '))
        score += rank
    
    average_score = score / 5
    print(f'Your restaurant rating is {average_score:.2f}')
    #Run function to show stars based on average score
    determine_stars(average_score)

def determine_stars(average):
    if average >= 9:
        #Display 5 stars
        for n in range(5):
            print('*', end='')
    elif average >= 8:
        #Display 4 stars
        for n in range(4):
            print('*', end='')
    elif average >= 7:
        #Display 3 stars
        for n in range(3):
            print('*', end='')
    elif average >= 6:
        #Display 2 stars
        for n in range(2):
            print('*', end='')
    elif average > 5:
        #Display 1 star
        print('*', end='')
    else:
        print('No stars')

main()
