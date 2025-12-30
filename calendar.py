def main():
    month = input("Enter month name: ").strip().title()
    year = int(input("Enter year: "))

    print(f"\nCalendar for {month} {year}")

    days = get_days(month, year)

    if days == 0:
        print("Invalid month")
    else:
        print_days(days)


def get_days(month, year):
    match month:
        case "January" | "March" | "May" | "July" | "August" | "October" | "December":
            return 31
        case "April" | "June" | "September" | "November":
            return 30
        case "February":
            if year % 4 == 0:
                return 29
            else:
                return 28
        case _:
            return 0


def print_days(days):
    for day in range(1, days + 1):
        print(day)


main()