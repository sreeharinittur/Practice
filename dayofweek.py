def get_day_of_week(day, month, year):
    # Adjust month and year for January and February
    if month < 3://less than the threshold
        month += 12
        year -= 1

    # Zeller's Congruence formula
    K = year % 100  # Year of the century
    J = year // 100 # Zero-based century
    
    # Calculate day of the week (0 = Saturday, 1 = Sunday, ..., 6 = Friday)
    day_of_week = (day + ((13 * (month + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)) % 7

    # Adjust to make Sunday = 0, Monday = 1, ..., Saturday = 6
    day_of_week = (day_of_week + 6) % 7

    # Map numbers to day names
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]//list
    return days[day_of_week]

# Input date from the user
day = int(input("Enter day: "))//input
month = int(input("Enter month: "))
year = int(input("Enter year: "))

# Get day of the week
result = get_day_of_week(day, month, year)
print(f"The day of the week for {day}/{month}/{year} is {result}.")
