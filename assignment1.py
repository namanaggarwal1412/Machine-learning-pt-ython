# question 1

# Explanation (Mutability and Performance)
# Lists are mutable (can be changed after creation) and typically slower due to the overhead of supporting operations like resizing and adding/removing elements.
# Tuples are immutable (cannot be changed after creation) and are generally faster due to their fixed size.

# Choose a list when you need to modify or rearrange data.
# Choose a tuple when the data is fixed and needs protection from modification.


# Question 2
#Python Type Conversion

# Implicit Conversion (e.g., int to float)
num_int = 5
num_float = num_int + 2.5  # Converts int to float automatically
print(num_float)  # Output: 7.5

# Explicit Conversion (e.g., str to int)
string_num = "123"
int_num = int(string_num)
print(int_num + 10)  # Output: 133

# Question 3
#Using the += operator

num = 20
num += 10
print(num)  # Output: 30
 

 # Question 4
 #Leap Year Checker

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# Question 5
#Grade Calculator

marks = int(input("Enter your marks: "))

if 90 <= marks <= 100:
    grade = 'A'
elif 80 <= marks <= 89:
    grade = 'B'
elif 70 <= marks <= 79:
    grade = 'C'
elif 60 <= marks <= 69:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is: {grade}")