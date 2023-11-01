def calculate_total(numbers, exclude_negative=False):
    total = 0
    for number in numbers:
        if exclude_negative and number < 0:
            continue
        total += number
    return total

user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

exclude_negative_input = input("Exclude negative numbers (yes or no)? ").strip().lower()

if exclude_negative_input == 'yes':
    exclude_negative = True
else:
    exclude_negative = False

result = calculate_total(numbers, exclude_negative)

print("Sum of elements:", result)

