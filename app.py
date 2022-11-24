import sys
from analyzer import algorithms
from analyzer import analyzer_utils

if __name__ == "__main__":

    try:
        analyzer_utils.validate_app_arguments(sys.argv)
        number_list, x = analyzer_utils.parse_arguments(sys.argv)
        analyzer_utils.validate_input(number_list, x)
        answer = algorithms.set_based_solution(number_list, x)
        # answer.sort() #TODO Check if this is necessary
        for pair in answer:
            print(f"{pair[0]},  {pair[1]}")
    except Exception as error:
        print("Something went wrong! try again")
