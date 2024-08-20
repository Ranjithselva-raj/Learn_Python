#formulae for calculating EMI is: P * R * pow(1+R, N) / (pow(1+R, N) - 1)

def emi(p, r, n):
    """
    Calculate the Equated Monthly Installment (EMI) for a loan.

    Args:
        p (float): Principal loan amount.
        r (float): Annual interest rate.
        n (int): Number of months.

    Returns:
        float: The EMI amount.
    """
    # Convert annual rate to monthly rate
    r = r / (12 * 100)
    # Calculate the EMI
    emi = (p * r * pow(1 + r, n)) / (pow(1 + r, n) - 1)
    #emi = p*r*((1+r)**n)/((1+r)**n-1
    # Round the EMI with 2 decimal places
    return round(emi, 2) 
p = int(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate: "))
n = int(input("Enter the number of months: "))
print(emi(p, r, n))