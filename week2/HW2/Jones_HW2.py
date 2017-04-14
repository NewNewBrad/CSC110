#Brad Jones
#CSC110 - Section 6
#4/13/2017

# Home Renovation Cost Calculator

###############Example for testing####################

#INPUT
#Enter a length of house in feet: 		50
#Enter a width of house in feet: 		30
#Enter a height of house in feet: 		10
#Enter a cost of profile in $: 			128.75
#Enter a cost of siding nails in $: 		15.96
#Enter a cost of side strips in $: 		11
#Enter a cost of a bundle of shingles in $: 	24.75
#Enter a cost of roofing nails in $: 		2.98
#
#OUTPUT
#The house has length = 50, width = 30, height = 10
#SIDING
#******************************************
#Total area of walls is 			1600
#Total profile is 				80
#Boxes of siding nails are 		40
#Weather side strips are 		54
#The cost of materials for siding	$11532.40
#******************************************
#ROOF
#******************************************
#Bundles of shingles are 		93
#Boxes of roofing nails are 		92.38
#******************************************
#TOTAL
#*******************************************
#The cost of materials for the roof	$2394.13
#Total cost of home renovation	 	$13926.53

#######################################################

#USER INPUT
house_length = int(input("Enter a length of house in feet: "))
house_width = int(input("Enter a width of house in feet: "))
house_height = int(input("Enter a height of house in feet: "))
profile_cost = input("Enter a cost of profile in $: ")
sidingNail_cost = input("Enter a cost of siding nails in $: ")
sideStrip_cost = input("Enter a cost of side strips in $: ")
shingle_cost = input("Enter a cost of a bundle of shingles in $: ")
roofNail_cost = input("Enter a cost of roofing nails in $: ")


#PROCESSING
import math

#SIDING MATH
house_area = float((2 * (house_length * house_height)) + (2 * (house_height * house_width)))
siding_area = float(house_area - (house_area * (20/100)))
siding_profile = float((9 * 32) / 12)
total_profile = float(siding_area / siding_profile)
siding_nails = float((1/2) * total_profile)
siding_strips = float(2 / (3 * total_profile))

#ROOF MATH
#roof_height = float(( house_width - ((1/2) * house_width)))
#roof_tri = float((house_width * roof_height) / 2 )
roof_box = float(house_width + 5 * house_length)
#roof_area = float((2 * roof_tri) + (2 * roof_box))
roof_bundle = float(33.3)
roof_nails = float(3 / roof_bundle)

#COST MATH





#PROGRAM OUTPUT
#TEST OUTPUT:
print(house_length, house_width, house_height, profile_cost, sidingNail_cost, sideStrip_cost,
      shingle_cost, roofNail_cost)


#print("The house has length = ", length, ", width = ", width, "height = ", height)
print("\n")
print("SIDING: ")
print("************************************************************")
print("Total area of walls is: ", house_area)
print("Total profile is : ",)
print("Boxes of siding nails needed: ",)
print("Weather side strips needed: ",)
print("TOTAL MATERIAL COST FOR SIDING: ",)
print("************************************************************")
print("\n")
print("ROOF: ")
print("************************************************************")
print("Bundles of shingles required: ",)
print("Boxes of roofing nails required: ",)
print("TOTAL MATERIAL COST FOR ROOF: ",)
print("************************************************************")

print("\n")
print("TOTAL: ")
print("************************************************************")
print("************************************************************")
