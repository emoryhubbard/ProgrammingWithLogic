def get_wind_chill(temp, speed):

    chill = 35.74 + 0.6215 * temp - 35.75 * speed ** 0.16 + 0.4275 * temp * speed ** 0.16
 
    return chill

def is_celsius(unit):
    is_celsius = True
    if unit.lower() != "c":
        is_celsius = False

    return is_celsius

def get_fahr(temp):
    fahr = temp * (9/5) + 32
    return fahr



temp = float(input("what is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ")

if is_celsius(unit):
    temp = get_fahr(temp)
else:
    temp = temp

for speed in range(5, 65, 5):
    chill = get_wind_chill(temp, speed)
    print(f"At temperature {temp}F, and wind speed {speed} mph, the windchill is: {chill:.2f}F")

