#Variables
age=int()
ski_time=str()
total_cost=int()
#Ask the user for their input to go skiing
age=int(input("Enter your age:  "))
ski_time=str(input("Do you want to night ski? Enter yes or no:  "))
#Process to determine the cost of the ski lift
if age <= 7:
    total_cost = 0
elif age >= 8 and age <= 13:
    total_cost = 35
elif age >= 14 and age <= 17:
    total_cost = 45
elif age >= 18 and age <= 70:
    total_cost = 55
else:
    total_cost = 0

if ski_time == "yes":
    if age >= 8 and age <= 70:
        total_cost = total_cost + 20
    else:
        total_cost = 0
        
#Output of cost of ski lift
print("Your life ticket will cost you:  $", total_cost)
