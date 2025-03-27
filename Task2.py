try: 
a = int(input("Enter number: "))
if 1<= a <= 100:
   print("Your number is between 1 and 100 ")
else :
   print("Your number is not corecct")
except ValueError:
    print("Invalid input! Please enter a number.")
