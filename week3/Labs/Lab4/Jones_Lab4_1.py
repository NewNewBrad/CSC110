#Brad Jones
#CSC110 - Section 6
#4/20/2017
#Bulk discount calculator


#Input
print('Software packages are $99. Discounts given to bulk orders.')
apps = int(input('Enter the number of packages to order to calculate discount: '))
subtotal = apps * 99


#Processing
#10% off for 10-19 packages
if apps > 9 and apps < 20:
    reward = str('10%')
    discount = subtotal * (10/100)
    finaltotal = (subtotal - discount)
    

#20% off for 20-49 packages
if apps >= 20 and apps < 50:
    reward = str('20%')
    discount = subtotal * (20/100)
    finaltotal = subtotal - discount


#30% off for 50 or more packages
if apps >= 50 :
    reward = str('30%')
    discount = subtotal * (30/100))
    finaltotal = subtotal - discount


#Output
print('Your purchase of ', apps, ' software packages totals: ', subtotal)
print('You qualify to recieve ', reward, 'off!')
print('Your final total is: ', finaltotal)
print('You saved: ', discount, 'dollars.')
