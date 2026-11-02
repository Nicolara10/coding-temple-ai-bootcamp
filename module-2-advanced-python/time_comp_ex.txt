import time
import random
# Function A
def get_first(data):
    return data[0]
#o(1) Grabbing data[0] is one step whether the list has 5 items or 5 million, because Python jumps straight to that position.

# Function B
def count_matches(data, target):
    count = 0
    for item in data:
        if item == target:
            count += 1
    return count
#O(n), linear time. The loop visits every item once, so doubling the list doubles the work.

# Function C
def all_pairs(data):
    pairs = []
    for i in range(len(data)):
        for j in range(len(data)):
            pairs.append((data[i], data[j]))
    return pairs
#O(n²), quadratic time. For each of the n items, the inner loop runs n times, so you get n × n steps. A list of 1,000 makes 1,000,000 pairs.

# Function D
def mystery(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count
#O(log n), logarithmic time. Each pass cuts n in half, so even n = 1,000,000 only takes about 20 loops. This is the trickiest one: there’s a loop, but it doesn’t run n times.
# Function E
def process(data):
    total = sum(data)           # Line 1
    sorted_data = sorted(data)  # Line 2
    first = data[0]             # Line 3
    return total, sorted_data, first
#O(n log n). Line 1 is O(n), Line 2 is O(n log n) because sorting is the expensive part, and Line 3 is O(1). When steps run one after another, you keep only the biggest term, so the whole function is O(n log n).

def num_of_pairs_slow(data, target):
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == target:
                count += 1
    return count
def count_pairs_fast(numbers, target):
    count = 0
    seen = {}

    for num in numbers:
        needed = target - num

        if needed in seen:
            count += seen[needed]

        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1

    return count
# ------------------------------------------------------------
# Correctness check: both functions should agree
# ------------------------------------------------------------
assert num_of_pairs_slow([1, 2, 3, 4], 5) == 2
assert count_pairs_fast([1, 2, 3, 4], 5) == 2
assert num_of_pairs_slow([2, 2, 2], 4) == 3
assert count_pairs_fast([2, 2, 2], 4) == 3


# ------------------------------------------------------------
# Benchmark
# ------------------------------------------------------------
random.seed(42)  # makes the random lists the same every run
target = 100
sizes = [1000, 5000, 10000]

print("Benchmark: counting pairs that sum to", target)
print("-" * 60)

for size in sizes:
    data = [random.randint(1, 100) for _ in range(size)]

    start = time.perf_counter()
    slow_result = num_of_pairs_slow(data, target)
    slow_time = time.perf_counter() - start

    start = time.perf_counter()
    fast_result = count_pairs_fast(data, target)
    fast_time = time.perf_counter() - start

    print(f"n = {size}")
    print(f"  O(n^2) version: {slow_time:.4f} seconds  (pairs found: {slow_result})")
    print(f"  O(n)   version: {fast_time:.4f} seconds  (pairs found: {fast_result})")
    print(f"  Results match: {slow_result == fast_result}")
    print()