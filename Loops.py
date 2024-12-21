# Execute code repeatedly

# for loop

list_of_Fruits = ["Mango", "Apple", "Pineapple", "Lemon"]


for item in list_of_Fruits:
    print(item)

#while loop

def flat(x,y):
    return x/y

results=flat(25,12)
res=float(results)
print(res)

a=20
b=24

#if conditions are used in relating code statements, we use them normally in functions to execute the best decision 
#we can obtain. The else if this time is not used but we use the short form of elif.
def ifelse():
    if (a == b):
        print("Christmas")
    elif (a < b):
        print("Village")
    elif(a>b):
        print("Upbroad")

ifelse()

# To use exponents, we just need to bring in **.
def value(x):
    return x**3

valuing=value(9)
print(valuing)

#Note that exponents can also be used to get square roots, let's have an example while using 0.5

def square(w):
    return(w**0.5)

we=square(25)
print(25)

#let's have an example of 81
def nine(v):
    return(v**0.5)

vein= nine(81)
print(vein)

# discount.py

# Prompt the user for the original price
original_price = float(input("Enter the original price: "))

# Prompt the user for the discount percentage
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the discounted price
discounted_price = round((1 - discount_percentage / 100) * original_price, 2)

# Print the result
print(f"The discounted price is: {discounted_price}")

