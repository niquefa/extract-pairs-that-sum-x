import logging
from analyzer import analyzer_utils
from analyzer import constants

"""
    Naive O(n^2) solution, just try all possible pairs
"""


def naive_n_square(number_list, x):
    n = len(number_list)
    answer = []
    for i in range(n):
        for j in range(i + 1, n):
            if x == number_list[i] + number_list[j]:
                answer.append((number_list[i], number_list[j]))
    return answer


"""
    Set based solution with O(n) complexity in best case, O(n^2) worst case. The commplexity depends on the 
    set contains function behaivior wich is O(1) in the average case but O(n) in the worst case
    https://wiki.python.org/moin/TimeComplexity
"""


def set_based_solution(number_list, x):
    answer = set()
    list_as_set = set(number_list)
    for number in number_list:
        complement = x - number
        if number != complement and complement in list_as_set:
            answer.add(tuple(sorted((number, complement))))
    return list(answer)


"""
    Helper unction O(n log n) to check if a number is in a sorted list
"""


def check_contains_with_binary_search(number_list, number_to_search):
    low = 0
    high = len(number_list) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if number_list[mid] < number_to_search:
            low = mid + 1
        elif number_list[mid] > number_to_search:
            high = mid - 1
        else:
            return True
    return False


"""
    Sort and binary search based solution with O(n log n) complexity. The complexity is dominated by the sorting and the 
    linear loop with the binary search inside.
"""


def sort_and_binary_search_based_solution(number_list, x):
    number_list.sort()
    answer = set()
    for number in number_list:
        complement = x - number
        if number != complement and check_contains_with_binary_search(number_list, complement):
            answer.add(tuple(sorted((number, complement))))
    return list(answer)


"""
    O(max(n,m)) where m = max_element_in_number_list - min_element_in_number_list
    This algorithm will not work if the value of m is too big, or at least the trade off would not be worth it.
"""


def limited_magnitude_in_numbers_based_solution(number_list, x):
    max_n = number_list[0]
    min_n = number_list[0]
    for number in number_list:
        max_n = number if number > max_n else max_n
        min_n = number if number < min_n else min_n

    in_list = [False] * (max_n - min_n + 1)
    for number in number_list:
        index = number - min_n
        in_list[index] = True

    used = [False] * (max_n - min_n + 1)
    answer = []
    for number in number_list:
        complement = x - number
        complement_index = complement - min_n
        number_index = number - min_n
        if (
            number != complement
            and complement_index < len(in_list)
            and complement_index >= 0
            and in_list[complement_index]
            and not used[complement_index]
            and not used[number_index]
        ):
            answer.append(tuple(sorted((number, complement))))
            used[complement_index] = True
            used[number_index] = True

    return answer
