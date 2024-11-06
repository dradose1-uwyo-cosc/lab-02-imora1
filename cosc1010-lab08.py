#Isabell Mora
#Lab Section-11
#11-5-24
#Sources, help given to/received from

def leap_year(year):
    """Checking if a year is a leap year."""
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

def first_day_of_year(year):
    """Calculate the day of the weel"""
    y = year - 1
    return (36 + y + (y // 4) - (y // 100) + (y // 400)) % 7

def valid_date(month, day, year):
    """Checking if date is valid"""
    month_days = {
        1: 31, 2: 29 if leap_year(year) else 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    return 1 <= month <= 12 and 1 <= day <= month_days.get(month, 0)

def day_of_week_for_date(month, day, year):
    """Calculate the day of the week for a given date."""
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    if not valid_date(month, day, year):
        return "Please enter valid date"
    
    jan_first_day = first_day_of_year(year)
    
    days_in_month = {
        1: 31, 2: 29 if leap_year(year) else 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    days_since_jan_first = sum(days_in_month[m] for m in range(1, month)) + (day - 1)
    
    weekday = (jan_first_day + days_since_jan_first) % 7
    return days_of_week[weekday]

def p_date(date_str):
    if len(date_str) != 10 or date_str[2] != '/' or date_str[5] != '/':
        return None
    month_str, day_str, year_str = date_str[:2], date_str[3:5], date_str[6:]
    if not (month_str.isdigit() and day_str.isdigit() and year_str.isdigit()):
        return None
    return int(month_str), int(day_str), int(year_str)

def main():
    while True:
        date_str = input("Enter a date in MM/DD/YYYY format (or type 'exit' to quit): ")
        if date_str.lower() == "exit":
            break

        parsed_date = p_date(date_str)
        if parsed_date is None:
            print("Invalid input. Please enter the date in MM/DD/YYYY format.")
            continue

        month, day, year = parsed_date

        day_of_week = day_of_week_for_date(month, day, year)
        print(f"{date_str} {day_of_week}")
main()




        
