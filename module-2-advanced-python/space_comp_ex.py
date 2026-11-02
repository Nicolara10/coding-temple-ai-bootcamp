# Function A
def reverse_string(s):
    return s[::-1]
#O(n) s[::-1] builds a brand new reversed string the same length as the original, so memory grows with the string.
# Function B
def count_letters(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts
#O(k), where k is the number of unique characters, which is at most O(n). The dictionary gets one entry per different character, so “aaaa” needs 1 entry but “abcd” needs 4. (If your instructor wants one answer, O(n) is the safe worst case.)
# Function C
def matrix_identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
#O(n²). It builds an n × n grid, so n = 1,000 means 1,000,000 numbers stored.
# Function D
def running_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)
#It only ever keeps one variable, total, no matter how long the list is. This is the opposite of Function A: it reads a lot but stores almost nothing.

def find_duplicates_set(filename):
    seen = set()
    duplicates = set()

    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            email = row["email"]
            if email in seen:
                duplicates.add(email)
            else:
                seen.add(email)

    return duplicates

def find_duplicates_sorted(filename):
    emails = []

    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            emails.append(row["email"])

    emails.sort()  # duplicates now sit right next to each other

    duplicates = []
    for i in range(1, len(emails)):
        if emails[i] == emails[i - 1]:
            # Only record it once, even if it appears 3+ times
            if len(duplicates) == 0 or duplicates[-1] != emails[i]:
                duplicates.append(emails[i])

    return duplicates