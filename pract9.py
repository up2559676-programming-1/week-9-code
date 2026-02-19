import calendar

def display_date(day: int, month: int, year: int):
    month_str = calendar.month_name[month]
    print(f"{day} {month_str} {year}")