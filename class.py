class Myclass:
    y=5
    


p1=Myclass()
print(p1.y)

# Step 1: Define the Calculator class
class Calculator:
    # Method to add two integers
    # represents an object of the class
    def add_numbers(self, num1, num2):
        return num1 + num2

# Step 2: Create an object of the Calculator class
calc = Calculator()

# Step 3: Call the add_numbers method using the object
result = calc.add_numbers(5, 10)  # Adding 5 and 10

# Print the result
print("The sum is:", result)

class perfect:

    def here(self, x,y):
        return x*y

van=perfect()
res=van.here(5,8)
print(res)


class Math:

    def gift(self, rent, hype):
        return rent-hype

M=Math()

resu=M.gift(15,8)
print(resu)