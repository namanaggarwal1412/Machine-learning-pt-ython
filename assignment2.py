# 1. Pascal's Triangle

def pascals_triangle(rows):
    for i in range(rows):
        row = [1]  # First element is always 1
        for j in range(1, i + 1):
            row.append(row[j - 1] * (i - j + 1) // j)  # Formula for Pascal's Triangle
        print(" ".join(map(str, row)))

print("Pascal's Triangle (5 rows):")
pascals_triangle(5)


# 2. The continue Statement
# continue skips the remaining code in the current iteration and moves to the next iteration.

numbers = [10, 15, 18, 22, 24, 30, 35]
print("\nNumbers divisible by 3:")
for num in numbers:
    if num % 3 != 0:
        continue  # Skip numbers that are not divisible by 3
    print(num)


# 3. List Comprehension for Pythagorean Triplets

pythagorean_triplets = [(a, b, c) for a in range(1, 51) 
                        for b in range(a, 51) 
                        for c in range(b, 51) 
                        if a**2 + b**2 == c**2]

print("\nPythagorean Triplets (a, b, c) where a, b, c ≤ 50:")
print(pythagorean_triplets)


# 4. Maximum Consecutive Sum

def max_consecutive_sum(nums, k):
    if len(nums) < k or k <= 0:
        return None  # Edge case: k is larger than list size or invalid
    max_sum = sum(nums[:k])  # Initial sum of first k elements
    current_sum = max_sum
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]  # Sliding window technique
        max_sum = max(max_sum, current_sum)
    return max_sum

print("\nMax consecutive sum:", max_consecutive_sum([1, 2, 3, 4, 5, 6, 7, 8], 3))


# 5. Modifying List in a Function

def modify_list(lst):
    lst.append("New Item")

my_list = [1, 2, 3]
modify_list(my_list)
print("\nModified List:", my_list)  # Demonstrates how the list is changed globally


# 6. Fibonacci Sequence up to n terms

def fibonacci(n):
    if n <= 0:
        return []  # Edge case: No terms
    elif n == 1:
        return [0]  # Edge case: Only one term
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

n_terms = int(input("\nEnter number of Fibonacci terms: "))
print("Fibonacci sequence:", fibonacci(n_terms))
