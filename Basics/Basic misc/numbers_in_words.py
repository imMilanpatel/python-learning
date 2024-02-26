def number_to_indian_words(num):
    words = [
        "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    ]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def convert_less_than_thousand(number):
        if number < 20:
            return words[number]
        elif number < 100:
            return tens[number // 10] + (" " + words[number % 10] if number % 10 != 0 else "")
        else:
            return words[number // 100] + " Hundred" + (" and " + convert_less_than_thousand(number % 100) if number % 100 != 0 else "")

    if num == 0:
        return "Zero"

    result = ""

    crore = num // 10000000
    num %= 10000000

    if crore > 0:
        result += convert_less_than_thousand(crore) + " Crore"

    lakh = num // 100000
    num %= 100000

    if lakh > 0:
        result += " " + convert_less_than_thousand(lakh) + " Lakh"

    thousand = num // 1000
    num %= 1000

    if thousand > 0:
        result += " " + convert_less_than_thousand(thousand) + " Thousand"

    remaining = convert_less_than_thousand(num)
    if remaining:
        result += " " + remaining

    return result.strip()

# Example
input_number = int(input("Enter the number: "))
output_words = number_to_indian_words(input_number)
print(f"{input_number:,} is written as {output_words}")