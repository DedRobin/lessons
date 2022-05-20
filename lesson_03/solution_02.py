# Variables
first_contribution = 2130
bonus = 120
percent = 0.1
years = 5

current_contribution = first_contribution

# Find the current contribution for each year
for year in range(years):
    general_bonus = current_contribution * percent + bonus
    current_contribution += general_bonus

print(current_contribution)
