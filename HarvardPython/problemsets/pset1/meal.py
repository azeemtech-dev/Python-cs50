def convert(time_str):
    hours, minutes = time_str.split(":")
    hours = int(hours)
    minutes = int(minutes)
    hours_decimal = hours + (minutes / 60)
    return hours_decimal

def main():
    time_input = input("Enter the time (24-hour format, e.g., 07:30): ")

    try:
        time_in_hours = convert(time_input)
        
        if 7.0 <= time_in_hours < 12.0:
            print("It's breakfast time!")
        elif 12.0 <= time_in_hours < 15.0:
            print("It's lunch time!")
        elif 18.0 <= time_in_hours < 22.0:
            print("It's dinner time!")
        # No output if not within any meal time range
        
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM format.")

if __name__ == "__main__":
    main()
