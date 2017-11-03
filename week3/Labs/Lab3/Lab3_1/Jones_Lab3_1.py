# Last Name
# CSC 110, section 05
# 10/11/2016
# This program will calculate the tip for user

# Lab 3

print("Hello! Welcome to the Tip Calculator!")
#input section
money_pay = float(input("Please enter the money you have to pay in dollar: "))
if money_pay < 0:
    print("Error, you have entered and invalid Bill amount")
else:
    percentage_tip = float(input("Please enter the percentage you have to tip: "))
    if percentage_tip < 0 or percentage_tip > 100:
        print("Error, you have entered an invalid Tip Percentage")
    else:
        #statement section  
        money_tip = money_pay * percentage_tip / 100
        total_money_pay = money_pay + money_tip

        #output section
        print("Money not include tip have to pay: $"+format(money_pay,'.2f')+'\n'
        "Percentage have to tip: "+format(percentage_tip,'.0f')+'%\n'
        "Money tip: $"+format(money_tip,'.2f')+'\n'
        "Total amount money including tip you have to pay: $"+format(total_money_pay,'.2f'))
    
