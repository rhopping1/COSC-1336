#Rachel Hopping
#Complete
#Display the number of millimeters the ocean will rise over 25 years at 1.8 millimeters per year

RATE = 1.8
YEARS = 26
rise = 0

print('Year \t Rise (in millimeters)')
for n in range(30):
    print('-', end='')
print('\n')

for year in range(1, YEARS):
    rise = year * RATE
    print(f'{year} \t {rise:.2f}')
