#Rachel Hopping
#Complete
#Ask the user to enter the number of views and engagement rate in the last 30 days.
#Calculate which if any ads should display based on views and engagement
#Calculate the revenue based on ads shown

SKIPPABLE_RATE = 0.01
NON_SKIPPABLE_RATE = 0.15
BOTH_ADS_RATE = 0.16

views = int(input('Enter the number of views in the last 30 days: '))
engagement_rate = int(input('Enter the engagement rate percentage as a whole number. For example, 10% is entered as 10. '))

# views less that 1000
if views < 1000:
    ads = 0
    print('Monetization Strategy: Display no ads at this time')

#engagement rate less than 2%
elif engagement_rate < 2:
    ads = 0
    print('Monetization Strategy: Display no ads at this time')

#views between 1000 and 5000
elif views < 5000:
    ads = SKIPPABLE_RATE
    print('Monetization Strategy: Display skippable ads')

else:
    ads = BOTH_ADS_RATE
    print('Monetization Strategy: Display skippable and non-skippable ads')

revenue = views * ads

print(f'Total Potential Revenue: ${revenue:,.2f}')
