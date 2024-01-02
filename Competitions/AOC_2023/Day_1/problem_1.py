def get_input():
    calibration_lines = []

    with open("input/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                calibration_lines.append(line)
    
    return calibration_lines

def find_calibration_value(calibration_string):
    first_digit, last_digit = None, None

    for curr_char in calibration_string:
        if curr_char.isnumeric():
            
            if first_digit == None:
                first_digit = curr_char

            last_digit = curr_char
    
    return int(first_digit + last_digit)


def main():
    calibration_lines = get_input()

    sum_of_calibration_values = 0

    for curr_line in calibration_lines:
        sum_of_calibration_values += find_calibration_value(curr_line)

    print (f"Sum of all calibration values is: {sum_of_calibration_values}")

if __name__ == "__main__":
    main()