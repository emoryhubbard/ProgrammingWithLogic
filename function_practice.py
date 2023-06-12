def display_regular(msg):
    print(msg)

def display_uppercase(msg):
    upper = msg.upper()
    print (upper)

def display_lowercase(msg):
    lower = msg.lower()
    print(lower)

def nothing():
    pass

msg = input("What is your message? ")

display_regular(msg)
display_uppercase(msg)
display_lowercase(msg)

print(nothing())