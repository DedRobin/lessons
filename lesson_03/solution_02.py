contribution = 2130

bonus = 120

percent = 0.1

years = 5

answer = contribution

for year in range(1, years):
	answer += contribution * percent + bonus

print(answer)

