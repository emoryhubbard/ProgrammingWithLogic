names = []
balances = []
response = 0
QUIT = "quit"
print("Enter the names and balances of bank accounts (type: quit when done)")

while response != QUIT:
    response = input("What is the name of this account? ")
    if response != QUIT:
        names.append(response)
        response = input("What is the balance? ")
        if response != QUIT:
            balances.append(float(response))

print("\nAccount Information: ")
total = 0

for i in range(len(names)):
    print(f"{names[i]} - ${balances[i]:.2f}")
    total += balances[i]

print(f"\nTotal: ${total:.2f}")

average = total / len(names)
print(f"Average: ${average:.2f}")
