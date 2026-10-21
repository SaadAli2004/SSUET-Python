# # Task 1

# name = "M. Saad Ali"
# age = 22
# city = "Karachi"

# print(f"My name is {name}, I'm {age} years old and I live in {city}")


# # Task 2
# x = int(input("Enter number 1: "))
# y = int(input("Enter number 2: "))

# def add(num1,num2):
#     return(num1 + num2)
# def subtract(num1,num2):
#     return(num1 - num2)
# def multiply(num1,num2):
#     return(num1 * num2)
# def divide(num1,num2):
#        if num2 != 0:
#             return num1/num2
#        else:
#             return "Undefined: Cannot be divided by 0"

# print("Addition: ",add(x,y)) 
# print("Subtraction: ", subtract(x,y))          
# print("Multiplication: ", multiply(x,y))          
# print("Division: ", divide(x,y)) 
  
    

# # Task 3

# x = int(input("Enter your marks for Maths: "))
# y = int(input("Enter your marks for Physics: "))
# z = int(input("Enter your marks for English: "))

# total= x+y+z

# def average(sub1,sub2,sub3):
#     calc = (sub1 + sub2 + sub3)/3

#     return round(calc)

# print("Total Marks: ", total )
# print("Average Marks: ", average(x,y,z))

# # Task 4
# originalPrice = int(input("Enter the original price of item: "))
# discountPercent = int(input("Enter the discount percentage: "))
# discountAmount= int((originalPrice*discountPercent)/100)

# def discount(price):
#     discountedPrice = price - discountAmount
#     return discountedPrice

# print("Original Price: ",originalPrice)
# print("Discount Percent: ", discountPercent, "%")
# print("Discount Amount: ", discountAmount)
# print("Price after discount: ", discount(originalPrice))

# # Task 4
# originalPrice = int(input("Enter the original price of item: "))
# discountPercent = int(input("Enter the discount percentage: "))

# def discount(price, discount):
#     discountedPrice = price - ((price*discount)/100)
#     return(discountedPrice)


# print("Original Price: ", originalPrice)
# print(f"Discount Percentage: {discountPercent}%")
# print("Discount Amount: ", round(originalPrice*(discountPercent/100)))
# print("Price after discount: ", round(discount(originalPrice, discountPercent)))



# # Task 5
# x = 10
# print("Original value: ", x)
# x += 5
# print("Step 1: 10 + 5 =", x)
# x -= 2
# print("Step 2: 15 - 2 =", x)
# x *= 3
# print("Step 3: 13 x 3 =", x)
# x /= 5
# print("Step 4: 39 / 5 =", x )
# print("Result: ", x)


