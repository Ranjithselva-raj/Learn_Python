#Fahrenheit(F) = temperature in degree celsius(C) * 9/5 + 32

celsius_temp =[25,30,35,40,45,50]

fahrenheit_temp = list(map(lambda c: (c*9/5)+32, celsius_temp))

print(fahrenheit_temp)




