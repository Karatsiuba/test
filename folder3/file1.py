import calendar

def average_days_in_month():
    total_days = sum(calendar.mdays[1:])  # Sum of days in all months
    avg_days = total_days / 12  # Average days in a month
    return avg_days

if __name__ == "__main__":
    print(f"Average number of days in a month: {average_days_in_month():.2f}")