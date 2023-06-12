def main():
    loan = int(input("How large is the loan? "))
    credit = int(input("How good is your credit history? "))
    income = int(input("How high is your income? "))
    down = int(input("How large is your down payment? "))

    approve = is_approved(loan, credit, income, down)

    if approve:
        print("\nYour loan application has been approved.")
    else:
        print("\nYour loan application has been denied.")

    return

def is_approved(loan, credit, income, down):
    approve = False
    if loan >= 5:
        if credit >= 7 and income >= 7:
            approve = True
        elif (credit >=7 or income >= 7) and down >= 5:
            approve = True
        else:
            approve = False
    elif credit < 4:
        approve = False
    elif income >= 7 or down >= 7:
        approve = True
    elif income >= 4 and down >= 4:
        approve = True
    else:
        approve = False
    
    return approve

if __name__ == "__main__":
    main()
