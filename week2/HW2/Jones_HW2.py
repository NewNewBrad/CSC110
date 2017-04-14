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
profile_cost = int(input("Enter a cost of profile in $: "))
siding_nails_cost = int(input("Enter a cost of siding nails in $: "))
siding_strips_cost = int(input("Enter a cost of side strips in $: "))
bundle_cost = int(input("Enter a cost of a bundle of shingles in $: "))
roof_nails_cost = int(input("Enter a cost of roofing nails in $: "))


#PROCESSING
import math

#SIDING MATH
house_area = float((2 * (house_length * house_height)) + (2 * (house_height * house_width)))
doorWindow_mod = house_area * 0.2
siding_area = house_area - doorWindow_mod
ONE_PROFILE = (1/20)
total_profile = house_area * ONE_PROFILE
siding_nails = float((1 / 2) * total_profile)
siding_strips = float((2 / 3)* total_profile)

#ROOF MATH
#The roof has 4 faces. 2 rectangle faces and 2 triangle faces
#Triangle height determined using Pythagorean Thorem
#1/2Width^2*Height^2=width^2
#height^2= width^2 - 1/2width^2
#sqrt both sides: height = width - 1/2width
roof_height = float(house_width - ((1/2) * house_width))

#Area of a triangle is (base(our width)*triangle height)/2)
roof_tri = float(((house_width + 5) * roof_height) / 2 )

#Area of a rectangle plus the 5ft overhang on length and width
roof_box = float(house_width + 5 * house_length + 5)

#Area of the Roof is area of 2 triangle faces + 2 Box faces
roof_area = float((2 * roof_tri) + (2 * roof_box))
ONE_BUNDLE = 33.3
total_bundle = roof_area / ONE_BUNDLE
roof_nails = float((1 / 3) * total_bundle)

#COST MATH
total_profile_cost = total_profile * profile_cost
total_siding_nails_cost = siding_nails * siding_nails_cost
total_siding_strips_cost = siding_strips * siding_strips_cost
total_bundle_cost = total_bundle * bundle_cost
total_roof_nails_cost = roof_nails * roof_nails_cost
total_siding_cost = total_profile_cost + total_siding_nails_cost + total_siding_strips_cost
total_roof_cost = total_bundle_cost + total_roof_nails_cost
total_material_cost = total_siding_cost + total_roof_cost





#PROGRAM OUTPUT

#TEST OUTPUT:
print(house_length, house_width, house_height, profile_cost, siding_nails_cost, siding_strips_cost,
      bundle_cost, roof_nails_cost, roof_height, roof_tri, roof_box, roof_area)


#print("The house has length = ", length, ", width = ", width, "height = ", height)
print("\n")
print("SIDING: ")
print("************************************************************")
print("Total area of walls is: ", format(house_area, '.0f'))
print("Total profile is : ", math.ceil(total_profile))
print("Boxes of siding nails needed: ", math.ceil(siding_nails))
print("Weather side strips needed: ", math.ceil(siding_strips))
print("TOTAL MATERIAL COST FOR SIDING: ",)
print("************************************************************")
print("\n")
print("ROOF: ")
print("************************************************************")
print("Bundles of shingles required: ", math.ceil(total_bundle))
print("Boxes of roofing nails required: ", math.ceil(roof_nails))
print("TOTAL MATERIAL COST FOR ROOF: ",)
print("************************************************************")

print("\n")
print("TOTAL: ")
print("************************************************************")
print("************************************************************")
