#we going to create a simple interest calculator
#formula is SI =  p*t*r/100 # p principal, t time, r rate of interest
 
p = int(input("Enter the principal amount: "))
t = float(input("Enter the time: "))
r = float(input("Enter the rate of interest: "))

si = p*t*r/100
print(f"Simple interest is: {si}")