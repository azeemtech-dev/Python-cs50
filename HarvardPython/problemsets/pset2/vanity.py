def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return (is_correct_length(s) and 
            starts_with_two_letters(s) and 
            no_invalid_characters(s) and 
            valid_number_usage(s))

def is_correct_length(s):
    return 2 <= len(s) <= 6

def starts_with_two_letters(s):
    return s[:2].isalpha()

def no_invalid_characters(s):
    return all(c.isalnum() for c in s)

def valid_number_usage(s):
    num_started = False
    for i, c in enumerate(s):
        if c.isdigit():
            if i == 0:
                return False  # Number at the start
            if not num_started:
                if c == '0':
                    return False  # First number is '0'
                num_started = True
        elif num_started:
            return False  # Letter after number
    return True

if __name__ == "__main__":
    main()
