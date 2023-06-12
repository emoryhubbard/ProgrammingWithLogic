people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

y_name, y_age = people[0].split(" ")

for person in people:
    name, age = person.split(" ")

    if float(age) < float(y_age):
        y_age = age
        y_name = name

print(f"Youngest: {y_name}, {y_age}")