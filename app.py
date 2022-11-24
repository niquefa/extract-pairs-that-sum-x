import sys
from analyzer import algorithms
from analyzer import analyzer_utils

if __name__ == "__main__":

    analyzer_utils.validate_app_arguments(sys.argv)
    number_list, x = analyzer_utils.parse_arguments(sys.argv)
    analyzer_utils.validate_input(number_list, x)

    algorithms.naive_n_square(number_list, x)
