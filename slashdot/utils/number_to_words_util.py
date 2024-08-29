def number_to_words(n):
    if not 10 <= n <= 99:
        raise ValueError("Input must be a two-digit number between 10 and 99.")

    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 10 <= n < 20:
        return teens[n - 10]
    else:
        ten_part = n // 10
        unit_part = n % 10
        return f"{tens[ten_part]} {units[unit_part]}".strip()


print(number_to_words(45))


def number_to_words(num: float) -> str:
    def convert_integer_to_words(n: int) -> str:
        under_20 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                    'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        above_1000 = {100: 'Hundred', 1000: 'Thousand', 1000000: 'Million', 1000000000: 'Billion'}

        if n < 20:
            return under_20[n]
        elif n < 100:
            return tens[n // 10] + ('' if n % 10 == 0 else ' ' + under_20[n % 10])
        else:
            max_key = max([key for key in above_1000.keys() if key <= n])
            return convert_integer_to_words(n // max_key) + ' ' + above_1000[max_key] + (
                '' if n % max_key == 0 else ' ' + convert_integer_to_words(n % max_key))

    if num < 0:
        return "Minus " + number_to_words(abs(num))

    integer_part, fractional_part = str(num).split(".")

    integer_words = convert_integer_to_words(int(integer_part))
    fractional_words = convert_integer_to_words(int(fractional_part))

    dollar_word = "dollar" if int(integer_part) == 1 else "dollars"
    cent_word = "cent" if int(fractional_part) == 1 else "cents"

    return f"{integer_words} {dollar_word} and {fractional_words} {cent_word}"


print(number_to_words(1.01))    # Output: "One dollar and One cent"
print(number_to_words(0.09))    # Output: "Zero dollars and Nine cents"
print(number_to_words(141.99))  # Output: "One Hundred Forty-One dollars and Ninety-Nine cents"
