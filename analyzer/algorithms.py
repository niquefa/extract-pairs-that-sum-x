import logging
from analyzer import analyzer_utils
from analyzer import constants


def naive_n_square(number_list, x):
    n = len(number_list)
    answer = []
    for i in range(n):
        for j in range(i + 1, n):
            if x == number_list[i] + number_list[j]:
                answer.append((number_list[i], number_list[j]))
    return answer
