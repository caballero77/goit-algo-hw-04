import timeit
import random
from merge_sort import merge_sort
from insertion_sort import insertion_sort


def is_sorted(array):
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))


def test_sort(sort, array):
    assert not is_sorted(array)
    time = timeit.timeit(lambda: sort(array), number=100)
    assert is_sorted(array)
    return time


def test_sorting(list_size):
    random_list = [random.randint(-1000, 1000) for _ in range(list_size)]
    print(f"Testing with array of size {size}")
    print("Merge Sort:", test_sort(merge_sort, random_list.copy()))
    print("Insertion Sort:", test_sort(insertion_sort, random_list.copy()))
    print("Python Sort:", test_sort(lambda l: l.sort(), random_list.copy()))


for size in [10, 100, 1000, 10000]:
    test_sorting(size)

# Results
# As expected the default python sort is facter than both merge and insertion sort
# Insertion sort is faster than merge sort for smaller arrays, but merge sort is faster for larger arrays
# Python sort is the fastest for all array sizes
