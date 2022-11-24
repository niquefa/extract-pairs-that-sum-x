import unittest
from analyzer import algorithms
from analyzer import analyzer_utils
from analyzer import data_generator
from analyzer import constants


# TODO Delete prints about sizes of algorithms responses


class AlgorithmsTests(unittest.TestCase):
    def assertEmpty(self, some_list):
        self.assertTrue(len(some_list) == 0)

    def assertNotEmpty(self, some_list):
        self.assertTrue(len(some_list) > 0)

    def test_naive_n_square_empty_list(self):
        self.assertEmpty(algorithms.naive_n_square([], 1))
        pass

    def test_naive_n_square_empty_answer_small_case(self):
        self.assertEmpty(algorithms.naive_n_square([1], 1))
        pass

    def test_naive_n_square_one_pair_answer_small_case_zero(self):
        answer = algorithms.naive_n_square([-1, 1], 0)
        self.assertNotEmpty(answer)
        self.assertTrue(analyzer_utils.list_are_equal(answer, [(1, -1)]))
        pass

    def test_naive_n_square_one_pair_answer_small_case(self):
        answer = algorithms.naive_n_square([1, 9, 5, 0, 20, -4, 12, 16, 7], 12)
        expected_answer = [(16, -4), (5, 7), (12, 0)]
        self.assertNotEmpty(answer)
        self.assertTrue(analyzer_utils.list_are_equal(answer, expected_answer))
        pass

    def test_naive_n_square_one_pair_answer_small_case(self):
        answer = algorithms.naive_n_square([3, 6, -1, -2, -4, 10, -1000, 0, 23, 8, 7], 6)
        expected_answer = [(0, 6), (-2, 8), (7, -1), (10, -4)]
        self.assertNotEmpty(answer)
        self.assertTrue(analyzer_utils.list_are_equal(answer, expected_answer))
        pass

    def test_naive_n_square_small_random_cases(self):
        answer_sizes = {}
        for size in range(constants.SIZE_FROM, constants.SIZE_TO):
            for _ in range(constants.MAX_ITERATION_BY_SIZE):
                number_list = data_generator.get_random_list(size, size * 2)
                x = data_generator.get_random_x(size)
                answer = algorithms.naive_n_square(number_list, x)

                answer_sizes[len(answer)] = answer_sizes[len(answer)] + 1 if len(answer) in answer_sizes else 1

                self.assertTrue(analyzer_utils.all_are_int_pairs(answer))
                self.assertTrue(analyzer_utils.list_has_no_repeated_pairs(answer))
                self.assertTrue(analyzer_utils.all_pairs_sum_x(answer, x))

        print(f"\n\nAnswer sizes found in naive O(n^2) algorithm random tests: \n\n{answer_sizes}\n\n")

    def assertAnswerList(self, answer_naive, answer, x):
        if analyzer_utils.list_are_equal(answer, answer_naive) == False:
            print()
            print(x)
            print(answer_naive)
            print(answer)
            print()
        self.assertTrue(analyzer_utils.list_are_equal(answer, answer_naive))
        self.assertTrue(analyzer_utils.all_are_int_pairs(answer))
        self.assertTrue(analyzer_utils.list_has_no_repeated_pairs(answer))
        self.assertTrue(analyzer_utils.all_pairs_sum_x(answer, x))

    def test_set_based_solution_small_random_cases(self):
        answer_sizes = {}
        for size in range(constants.SIZE_FROM, constants.SIZE_TO):
            for _ in range(constants.MAX_ITERATION_BY_SIZE):
                number_list = data_generator.get_random_list(size, size * 2)
                x = data_generator.get_random_x(size)

                answer_naive = algorithms.naive_n_square(number_list, x)
                answer = algorithms.set_based_solution(number_list, x)

                answer_sizes[len(answer)] = answer_sizes[len(answer)] + 1 if len(answer) in answer_sizes else 1

                self.assertAnswerList(answer_naive, answer, x)

        print(f"\n\nAnswer sizes found in set based solution O(n) algorithm random tests: \n\n{answer_sizes}\n\n")

    def test_sort_and_bs_based_solution_small_random_cases(self):
        answer_sizes = {}
        for size in range(constants.SIZE_FROM, constants.SIZE_TO):
            for _ in range(constants.MAX_ITERATION_BY_SIZE):
                number_list = data_generator.get_random_list(size, size * 2)
                x = data_generator.get_random_x(size)

                answer_naive = algorithms.naive_n_square(number_list, x)
                answer = algorithms.sort_and_binary_search_based_solution(number_list, x)

                answer_sizes[len(answer)] = answer_sizes[len(answer)] + 1 if len(answer) in answer_sizes else 1

                self.assertAnswerList(answer_naive, answer, x)

        print(
            f"\n\nAnswer sizes found in sort and binary search based solution O(n log n) algorithm random tests: \n\n{answer_sizes}\n\n"
        )

    def test_input_magnitud_limited_based_solution_small_random_cases(self):
        answer_sizes = {}
        for size in range(constants.SIZE_FROM, constants.SIZE_TO):
            for _ in range(constants.MAX_ITERATION_BY_SIZE):
                number_list = data_generator.get_random_list(size, size * 2)
                x = data_generator.get_random_x(size)
                answer_naive = algorithms.naive_n_square(number_list, x)
                answer = algorithms.limited_magnitude_in_numbers_based_solution(number_list, x)

                answer_sizes[len(answer)] = answer_sizes[len(answer)] + 1 if len(answer) in answer_sizes else 1

                self.assertAnswerList(answer_naive, answer, x)

        print(
            f"\n\nAnswer sizes found in input magnitude based solution O(max(n,m)) algorithm random tests: \n\n{answer_sizes}\n\n"
        )

    def test_all_algorithms_with_file(self):
        with open(constants.INPUT_TEST_CASES_FILE, "r") as file:
            input = [line.rstrip() for line in file]
        with open(constants.OUTPUT_TEST_CASES_FILE, "r") as file:
            correct_output = [line.rstrip() for line in file]

        self.assertTrue(len(input) == len(correct_output))

        for i in range(len(input)):
            arr = input[i].split(" ")
            self.assertTrue(len(arr) == 2)
            number_list = list(map(int, arr[0].split(",")))
            x = int(arr[1])
            correct_answer = []
            for str in correct_output[i].split(","):
                arr = str.split(" ")
                correct_answer.append((int(arr[0]), int(arr[1])))

            answer_naive = algorithms.naive_n_square(number_list, x)
            answer_set_based = algorithms.set_based_solution(number_list, x)
            answer_sort_based = algorithms.sort_and_binary_search_based_solution(number_list, x)
            answer_limited_magnitud = algorithms.limited_magnitude_in_numbers_based_solution(number_list, x)

            self.assertAnswerList(correct_answer, answer_naive, x)
            self.assertAnswerList(correct_answer, answer_set_based, x)
            self.assertAnswerList(correct_answer, answer_sort_based, x)
            self.assertAnswerList(correct_answer, answer_limited_magnitud, x)
        print(f"\n\nNon trivial test from file: \n\n{len(input)}\n\n")


if __name__ == "__main__":
    unittest.main()
