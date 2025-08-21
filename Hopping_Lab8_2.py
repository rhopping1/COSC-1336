#Rachel Hopping
#Complete
#Ask for input from user for a date in mm/dd/yyyy
#Print the date as Month DD, YYYY

MONTHS = ['January',
 'February',
 'March',
 'April',
 'May',
 'June',
 'July',
 'August',
 'September',
 'October',
 'November',
 'December'
 ]

def main():
    #Get date from user
    get_date = str(input('Enter the date in the format mm/dd/yyyy: '))
    
    #Split date
    split_date = get_date.split('/')
    
    #Subtract 1 from index
    get_month = int(split_date[0])- 1
    get_day = split_date[1]
    get_year = split_date[2]

    #Print date as Month DD, YYYY
    print(f'{MONTHS[get_month]} {get_day}, {get_year}')


main()
