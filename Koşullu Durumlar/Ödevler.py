# %% BMI -

height = float(input("Enter your height(Example:1.77):"))
weight = float(input("Enter your weight:"))

BMI = weight / (height * height)

if BMI < 18.5:
    print("You are thin")
elif 18.5 <= BMI < 25:
    print("You are in normal weight")
elif 25 <= BMI <= 30:
    print("You are overweight")
else:
    print("You are obese")

# %%  Take 3 number from user and find the highest

a = int(input("Enter first number: "))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a > b and a > c:
    print("The highest number is: ", a)
elif b > a and b > c:
    print("The highest number is: ", b)
else:
    print("The highest number is: ", c)

# %%
