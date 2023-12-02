NUMBER_DICT = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def process_line(line):

    first_digit = None
    last_digit = None
    number_as_chars = ''
    i = 0 
    while i < len(line):
        try:
            int(line[i]) # line to raise exception for characters
            if not first_digit:
                first_digit = last_digit = line[i]
            last_digit = line[i]
        except ValueError:
            number_as_chars = number_as_chars + line[i]
            j = 0
            while j < len(number_as_chars):
                if number_as_chars[j:] in NUMBER_DICT.keys():
                    if not first_digit:
                        first_digit = last_digit = NUMBER_DICT[number_as_chars[j:]]
                    last_digit = NUMBER_DICT[number_as_chars[j:]]
                    number_as_chars = ''
                    i = i-1
                    break
                j = j+1

        i = i + 1
    return first_digit, last_digit

def readlines(filepath):
    with open(filepath, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    return lines

def sum_of_calibration_values(lines):

    calibration_values = []
    for line in lines:
        first_digit, last_digit = process_line(line.strip())
        calibration_values.append(int(f"{first_digit}{last_digit}"))
        
    return sum(calibration_values)

if __name__ == "__main__":
    lines = readlines('part2_input.txt')
    print(sum_of_calibration_values(lines))
