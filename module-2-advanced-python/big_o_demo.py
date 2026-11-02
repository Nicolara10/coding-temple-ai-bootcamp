
import time
import random


def has_duplicate_slow(data):
    """Compare every element to every other element."""
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                return True
    return False


def has_duplicate_sort(data):

    """Sort the data and check for adjacent duplicates."""
    sorted_data = sorted(data)
    for i in range(len(sorted_data) - 1):
        if sorted_data[i] == sorted_data[i + 1]:
            return True
    return False


def has_duplicate_fast(data):
    """Use a set to track seen items for instant lookup."""
    seen = set()
    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False


def benchmark(func, data):
    """Run a function and return the time it took to run."""
    start = time.time()
    func(data)
    end = time.time()
    return end - start


sizes = [1000, 5000, 10000, 20000, 50000]

for size in sizes:
    data = list(range(size))
    random.shuffle(data)

    t1 = benchmark(has_duplicate_slow, data)
    t2 = benchmark(has_duplicate_fast, data)
    t3 = benchmark(has_duplicate_sort, data)

    print()