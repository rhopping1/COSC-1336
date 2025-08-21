#Rachel Hopping
#Complete
#Create the courses dictionary with key-value pairs
#Get input from user to pick which course to display all details


courses = { 'CS101' : [3004, 'Haynes', '8:00 a.m.'],
            'CS102' : [4501, 'Alvarado', '9:00 a.m.'],
            'CS103' : [6755, 'Rich', '10:00 a.m.'],
            'NT110' : [1244, 'Burke', '11:00 a.m.'],
            'CM241' : [1411, 'Lee', '1:00 p.m.']}

def main():
    number = input('Enter the course number: ')
    
    while number != '':
        while number not in courses:
            print(f'{number} is not a valid course number in the list.')
            number = input('Enter the course number: ')

        room = courses[number][0]
        instructor = courses[number][1]
        time = courses[number][2]

        #Display room, instructor, and time
        print(f'Room Number: {room}')
        print(f'Instructor: {instructor}')
        print(f'Meeting Time: {time}')

        number = input('Enter another course number or press enter to stop: ')

main()
