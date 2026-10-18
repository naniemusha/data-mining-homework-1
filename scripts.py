# ==============================================================================
# DATA MINING - HOMEWORK 1: PYTHON & ALGORITHMS SOLUTIONS
# ==============================================================================

# ==============================================================================
# PROBLEM 1: PYTHON DOMAINS
# ==============================================================================

# --- 1. INTRODUCTION ---
# Say "Hello, World!" With Python
print("Hello, World!")

# Python If-Else
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0 or (n % 2 == 0 and 6 <= n <= 20):
        print("Weird")
    else:
        print("Not Weird")

# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

# Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

# Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i ** 2)

# Write a function
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Print Function
if __name__ == '__main__':
    n = int(input())
    print("".join(map(str, range(1, n + 1))))


# --- 2. BASIC DATA TYPES ---
# List Comprehensions
if __name__ == '__main__':
    x, y, z, n = int(input()), int(input()), int(input()), int(input())
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])

# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])

# Nested Lists
if __name__ == '__main__':
    records = [[input(), float(input())] for _ in range(int(input()))]
    score_set = sorted(list(set(score for name, score in records)))
    second_lowest = score_set[1]
    print("\n".join(sorted([name for name, score in records if score == second_lowest])))

# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        student_marks[name] = list(map(float, line))
    query_name = input()
    scores = student_marks[query_name]
    print(f"{sum(scores)/len(scores):.2f}")


# --- 3. STRINGS ---
def swap_case(s):
    return s.swapcase()

def split_and_join(line):
    return "-".join(line.split(" "))

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count
# Capitalize!
def solve(s):
    for x in s.split():
        s = s.replace(x, x.capitalize())
    return s


# --- 4. SETS ---
def average(array):
    distinct_set = set(array)
    return sum(distinct_set) / len(distinct_set)


# --- 5. COLLECTIONS ---
from collections import Counter

if __name__ == '__main__':
    X = int(input())
    shoe_sizes = Counter(map(int, input().split()))
    N = int(input())
    earnings = 0
    for _ in range(N):
        size, price = map(int, input().split())
        if shoe_sizes[size] > 0:
            shoe_sizes[size] -= 1
            earnings += price
    print(earnings)


# --- 6. DATE AND TIME ---
import calendar
from datetime import datetime
if __name__ == '__main__':
    m, d, y = map(int, input().split())
    print(calendar.day_name[calendar.weekday(y, m, d)].upper())
# Time Delta
def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    return str(int(abs((dt1 - dt2).total_seconds())))

# --- 7. EXCEPTIONS ---
for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)


# --- 8. BUILT-INS ---
# Zipped!
if __name__ == '__main__':
    n, x = map(int, input().split())
    sheet = [list(map(float, input().split())) for _ in range(x)]
    for scores in zip(*sheet):
        print(sum(scores) / len(scores))

# Athlete Sort
if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())
    arr.sort(key=lambda x: x[k])
    for row in arr:
        print(*row)

# ginorts
import sys
if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    if s:
        print(*(sorted(s, key=lambda x: (x.isdigit() and int(x) % 2 == 0, x.isdigit(), x.isupper(), x.islower(), x))), sep='')


# --- 9. PYTHON FUNCTIONALS ---
cube = lambda x: x ** 3

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    res = [0, 1]
    for i in range(2, n):
        res.append(res[-1] + res[-2])
    return res


# ==============================================================================
# PROBLEM 2: ALGORITHMS
# ==============================================================================

# 1. Birthday Cake Candles
def birthdayCakeCandles(candles):
    max_val = max(candles)
    return candles.count(max_val)

# 2. Number Line Jumps (Kangaroo)
def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return "NO"
    if (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    return "NO"

# 3. Viral Advertising
def viralAdvertising(n):
    shared = 5
    cumulative = 0
    for _ in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative

# 4. Recursive Digit Sum
def superDigit(n, k):
    def get_sum(num_str):
        if len(num_str) == 1:
            return int(num_str)
        return get_sum(str(sum(int(char) for char in num_str)))
    
    initial_sum = sum(int(char) for char in n) * k
    return get_sum(str(initial_sum))

# 5. Insertion Sort - Part 1
def insertionSort1(n, arr):
    target = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > target:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    arr[i + 1] = target
    print(*arr)

# 6. Insertion Sort - Part 2
def insertionSort2(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(*arr)
