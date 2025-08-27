# Q1: Variables And data Types

user_name = "Syeda kiswa";
age = 15;
is_student = True;

print("My name is ",  user_name, " and I am ",  age, "years is old" , "student:",  is_student);
print(type(user_name));
print(type(age));
print(type(is_student));

# Q2: Arithmetic operators

x = 20;
y = 6;

print(x + y); # Addition
print(x - y); # Subtraction
print(x * y); # Mutliplication
print(x / y);  # Division
print(x // y); # Floor Divsion
print(x % y);  # Modulus
print(x ** y); # Exponention

# Q3: Assignment Operators

num = 10;
num += 5;
num *= 2;
num -= 4;

print(num)

# Q4: Comparison Operators

a = 15;
b = 12;

print(a > b) # --> true
print(a < b) # --> false
print(a == b) # --> false
print(a != b) # --> true
print(a >= b) # --> true
print(a <= b) # --> false

# Q5: Logical Operators

p = True;
q = False;

p and q # --> false
p or q # --> true
not p # --> false
not q # --> true

# Q6: Real-Life Example

total_enough = 600
notebook_price = 80;
book = 7


total_cost = notebook_price * book;
print(total_cost)

if total_enough >= total_cost:
    print("Yes, you have enough money to buy 7 notebooks.")

else:
   print("No, you don’t have enough money.")
   

# Q7: Bonus (Optional)


sum_number1 = 40;
sum_number2 = 30;

total_sumnumber = sum_number1 + sum_number2;

print("The sum num 1: ", sum_number1)
print("The sum num 2: ", sum_number2)
print("Total sum number:", total_sumnumber)

if sum_number1 > sum_number2:
  print("The first number is greater than second number");

else:
  print("The first number is not greater than second number");