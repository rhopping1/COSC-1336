#Rachel Hopping
#Complete
#Calculate the distance in meters based on the object's falling distance
#Create two functions, main and falling_distance

import distance

def main():
    print('Time\tFalling Distance\n')
    for n in range(30):
        print('-', end='')
    print('\n')

    for nums in range(1, 11):
        this_distance = distance.falling_distance(nums)
        print(f'{nums}\t{this_distance:.2f}')

main()
