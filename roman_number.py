def roman_to_integer(roman):
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    roman = roman.upper()
    if not roman:
        raise ValueError("Roman numeral cannot be empty.")


    
    for char in roman:
        if char not in values:
            raise ValueError("Invalid Roman numeral character.")

    
    if "VV" in roman or "LL" in roman or "DD" in roman:
        raise ValueError("V, L, and D cannot be repeated.")


   
    if "IIII" in roman or "XXXX" in roman or "CCCC" in roman or "MMMM" in roman:
        raise ValueError("A Roman numeral cannot repeat more than 3 times.")

    
    valid_subtractions = {
        "IV", "IX",
        "XL", "XC",
        "CD", "CM"
    }

    
    for i in range(len(roman) - 1):
        current = roman[i]
        next_char = roman[i + 1]

        if values[current] < values[next_char]:
            pair = current + next_char

            if pair not in valid_subtractions:
                raise ValueError(
                    f"Invalid subtraction: {pair}"
                )


    total = 0

    1) = 14
    for i in range(len(roman)):
        
        if (
            i + 1 < len(roman)
            and values[roman[i]] < values[roman[i + 1]]
        ):
            total -= values[roman[i]]
        else:
            total += values[roman[i]]

    if total < 1 or total > 3999:
        raise ValueError("Roman numeral must represent a number from 1 to 3999.")

   
    if integer_to_roman(total) != roman:
        raise ValueError("Invalid Roman numeral format.")

    return total


def integer_to_roman(number):
   
    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    result = ""

   
    for value, symbol in values:
        while number >= value:
            result += symbol
            number -= value

    return result


if __name__ == "__main__":
    
    while True:
        roman = input("Enter a Roman numeral: ")

        try:
            result = roman_to_integer(roman)
            print("Integer:", result)

        except ValueError as error:
            print("Invalid input:", error)
            continue

        while True:
            again = input("Do you want to continue? (yes/no): ").lower()

            if again == "yes" or again == "y":
                break

            elif again == "no" or again == "n":
                print("Goodbye!")
                exit()

            else:
                print("Please enter yes or no.")
