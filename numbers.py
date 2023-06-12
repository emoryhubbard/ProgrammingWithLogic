numbers = []
number = -1

print("Enter a list of numbers, type 0 when finished.")

while number != 0:
    number = int(input("Enter number: "))
    if number != 0:
        numbers.append(number)
sum = 0

for number in numbers:
    sum += number

print(f"The sum is: {sum}")

length = len(numbers)
average = sum / length

print(f"The average is: {average}")

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
print(f"The largest number is: {largest}")

