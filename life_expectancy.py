

# THIS COULD BE IMPLEMENTED MUCH MORE PERFORMANCE-FRIENDLY BY MAKING A LIST
# filled with only one of each country name based on input data. I'd like to
# revisit this sometime after taking algorithms and complexity theory. As is
# it runs through about 20,000 countries everytime since there are so many
# duplicates (This is only a problem for my "longest country" code).

with open("life-expectancy.csv", "r") as life_file:
    lines = []

    for line in life_file:
        clean_line = line.strip()
        clean_line = line.split(",")
        lines.append(clean_line)

    lines.pop(0) # removes the first line, which contains heading data

     # Lowest can't be set too high or highest too low if we use the
     # file data itself. This allows the program to work properly even
     # if there are errors in the file such as negative values. The
     # first line was chosen for this but any line could be chosen.
    COUNTRY_INDEX = 0
    YEAR_INDEX = 2
    LIFE_INDEX = 3
    

    first_line = lines[0]
    lowest = highest = float(first_line[LIFE_INDEX])
    lowest_country = highest_country = first_line[COUNTRY_INDEX]
    lowest_year = hightest_year = first_line[YEAR_INDEX]


    for line in lines:
        age = float(line[LIFE_INDEX])
        country = line[COUNTRY_INDEX]
        year = line[YEAR_INDEX]

        if age > highest:
            highest = age
            highest_country = country
            highest_year = year
        elif age < lowest:
            lowest = age
            lowest_country = country
            lowest_year = year

    user_year = input("Enter the year of interest: ")
    total = 0
    length = 0

    for line in lines:
        if line[YEAR_INDEX] == user_year:
            highest = lowest = float(line[LIFE_INDEX])
            highest_country = lowest_country = line[COUNTRY_INDEX]
            break

    for line in lines:
            age = float(line[LIFE_INDEX])
            year = line[YEAR_INDEX]
            country = line[COUNTRY_INDEX]

            if year == user_year:
                total += age
                length += 1

                if age > highest:
                    highest = age
                    highest_country = line[COUNTRY_INDEX]
                elif age < lowest:
                    lowest = age
                    lowest_country = line[COUNTRY_INDEX]

    avg = total / length

    print()
    print(f"The overall max life expectancy is: {highest} from {highest_country} in {highest_year}")
    print(f"The overall min life expectancy is: {lowest} from {lowest_country} in {lowest_year}")
    print()
    print(f"For the year {user_year}:")
    print(f"The average life expectancy across all countries was {avg:.2f}")
    print(f"The max life expectancy was in {highest_country} with {highest}")
    print(f"The min life expectancy was in {lowest_country} with {lowest}")
    print()
    print("The 3 longest country names (may take up to a minute to load): ")
    
    longest = ""
    longest_index = 0
    countries = []

    while len(countries) < 3:
        for line in lines:
            country = line[COUNTRY_INDEX]
            i = lines.index(line)
            
            if len(country) > len(longest) and not country in countries:
                longest = country
                longest_index = i

        countries.append(longest)
        longest = ""

for country in countries:
        print(country)
