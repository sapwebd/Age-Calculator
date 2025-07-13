

from datetime import datetime, date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - (
        (today.month, today.day) < (birthdate.month, birthdate.day)
    )
    return age

def main():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
        age = calculate_age(birthdate)
        print(f"Your age is: {age} years.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    main()


