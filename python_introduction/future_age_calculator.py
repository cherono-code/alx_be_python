#ask user for their age
age = (int(input(("How old are you? "))))

#calculate age in 2050
current_year = 2023
target_year = 2050

#difference between current year and target year
years_difference = int(target_year - current_year)

#finding out future age of 2050
future_age = age + years_difference
print(f"In 2050, you will be {future_age} years old.")