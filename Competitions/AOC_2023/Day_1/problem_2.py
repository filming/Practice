text_to_digit_map = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}

def get_input():
    calibration_lines = []

    with open("input/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                calibration_lines.append(line)
    
    return calibration_lines

def find_calibration_value(calibration_string):
    # convert input string into a string only containing digits
    calibration_digits = ""

    curr_index = 0
    while curr_index < len(calibration_string):
        if calibration_string[curr_index] in ('o', 't', 'f', 's', 'e', 'n'):

            if calibration_string[curr_index] == 'o':
                if calibration_string[curr_index: curr_index+3] in text_to_digit_map: # possibly creating a substr of "one"
                    calibration_digits += '1'
                    curr_index += 2

                else:
                    curr_index += 1

            elif calibration_string[curr_index] == 't':
                if calibration_string[curr_index: curr_index+3] in text_to_digit_map: # possibly creating a substr of "two"
                    calibration_digits += '2'
                    curr_index += 2

                elif calibration_string[curr_index: curr_index+5] in text_to_digit_map: # possibly creating a substr of "three"
                    calibration_digits += '3'
                    curr_index += 4

                else:
                    curr_index += 1

            elif calibration_string[curr_index] == 'f':
                substr = calibration_string[curr_index: curr_index+4] # possibly creating a substr of "four" or "five"

                if substr in text_to_digit_map:
                    if substr == "four":
                        calibration_digits += '4'
                    else:
                        calibration_digits += '5'
                    
                    curr_index += 3

                else:
                    curr_index += 1

            elif calibration_string[curr_index] == 's':
                if calibration_string[curr_index: curr_index+3] in text_to_digit_map: # possibly creating a substr of "six"
                    calibration_digits += '6'
                    curr_index += 2

                elif calibration_string[curr_index: curr_index+5] in text_to_digit_map: # possibly creating a substr of "seven"
                    calibration_digits += '7'
                    curr_index += 4

                else:
                    curr_index += 1

            elif calibration_string[curr_index] == 'e':
                if calibration_string[curr_index: curr_index+5] in text_to_digit_map: # possibly creating a substr of "eight"
                    calibration_digits += '8'
                    curr_index += 4

                else:
                    curr_index += 1

            else:
                if calibration_string[curr_index: curr_index+4] in text_to_digit_map: # possibly creating a substr of "nine"
                    calibration_digits += '9'
                    curr_index += 3

                else:
                    curr_index += 1

        elif calibration_string[curr_index].isnumeric():
            calibration_digits += calibration_string[curr_index]
            curr_index += 1

        else:
            curr_index += 1
    
    # return the first and last digit of the newly transcribed string
    first_digit, last_digit = calibration_digits[0], calibration_digits[len(calibration_digits) - 1]

    return int(first_digit + last_digit)

def main():
    calibration_lines = get_input()

    sum_of_calibration_values = 0

    for curr_line in calibration_lines:
        sum_of_calibration_values += find_calibration_value(curr_line)

    print (f"Sum of all calibration values is: {sum_of_calibration_values}")

if __name__ == "__main__":
    main()
