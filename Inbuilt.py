#In pytho, we have inbuilt modules or libraries used.
import datetime
import camelcase

#This camelcase module converts texts into camelcase styles which is the way of writing texts without spaces.
x=datetime.datetime.now()
print(x)


x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)



c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))


# Create a camelcase object
c = camelcase.CamelCase()

# Convert a string to CamelCase
text = "hello world from python"
camel_case_text = c.hump(text)

print(camel_case_text)  # Output: "helloWorldFromPython"
