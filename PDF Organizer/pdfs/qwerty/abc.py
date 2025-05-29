print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip_percentage = float(input("How much tip would you like to give? 10, 12 or 15 - "))
num_people = int(input("How many people to split the bill amongst? "))
total_tip = bill * (tip_percentage / 100)
total_amount = bill + total_tip
amount_per_person = round(total_amount / num_people, 2)
print(f"Each person should pay {amount_per_person}")

print(f"Each person should pay {amount_per_person}")