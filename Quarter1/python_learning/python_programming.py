name = input("Enter your name:")
num1 = int(input("Enter your first favourite number:"))
num2 = int(input("Enter your second favourite number:"))
num3 = int(input("Enter your third favourite number:"))
print("Hello",name,"Let's Explore your favourite number:".lstrip())
if  num1 % 2 == 0:
    print(f"The number",num1,"is even")
else:
    print("The number",num1,"is odd")    
if num2 % 2 == 0:
    print(f"The number",num2,"is even")
else:
    print("The number",num2,"is odd")    
if num3 % 2 == 0:
    print(f"The number",num3,"is even")
else:
    print("The numbe",num3,"is odd")
print("The number",num1,"and its square:",num1 ** 2)
print("The number",num2,"and its square:",num2 ** 2)
print("The number",num3,"and its square:",num3 ** 2)
print("Amazing! The sum of your favourite number is:",num1+num2+num3)
sum = num1 + num2 + num3
if sum/1 == 1 and sum/sum == 1:
    print(f"Wow,", sum, "is not a prime number!")
else:
    print(f"Wow,",sum, "is a prime number!")




