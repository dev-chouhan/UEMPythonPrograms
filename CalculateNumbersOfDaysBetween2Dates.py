from datetime import date
future_date = date(2022, 3, 1)
past_date = date(2022, 1, 1)
daysBetween = future_date - past_date
print(daysBetween.days)
