def calculate_year(age, current_year = 2025):
    return current_year - age

def leap_year(year):
    leapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    return leapYear
