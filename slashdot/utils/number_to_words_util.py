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
