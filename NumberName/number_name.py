def onesPlace(digit, _):
    names = {
        "": "",
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
    }

    return names[digit]


def tensPlace(digit, nextDigit):
    if digit == "1":
        digit += nextDigit
        nextDigit = ""
        names = {
            "10": "ten",
            "11": "eleven",
            "12": "twelve",
            "13": "thirteen",
            "14": "fourteen",
            "15": "fifteen",
            "16": "sixteen",
            "17": "seventeen",
            "18": "eighteen",
            "19": "nineteen",
        }
    else:
        names = {
            "": "",
            "0": "",
            "2": "twenty",
            "3": "thirty",
            "4": "fourty",
            "5": "fifty",
            "6": "sixty",
            "7": "seventy",
            "8": "eighty",
            "9": "ninety",
        }

    return names[digit], nextDigit


def main():
    MAX_LENGTH = 2
    running = True
    functions = [
        tensPlace,
        onesPlace,
    ]

    while running:
        try:
            number = int(
                input("enter an integer (up to {} digits long)".format(MAX_LENGTH))
            )
        except ValueError:
            print("Not a valid number")
        else:
            numStr = str(number).rjust(MAX_LENGTH, "")
            digits = [*str(number)]
            digits.zfill(MAX_LENGTH)
            digits.append("")
            if len(digits) > MAX_LENGTH:
                print("Number is too long")
            name = ""
            for index, digit in enumerate(digits):
                if digit != "":
                    name += functions[index](digit, digits[index + 1])


if __name__ == "__main__":
    main()
