import unittest
from analyzer import algorithms
from analyzer import analyzer_utils
from analyzer import data_generator


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

    def test_naive_n_square_small_random_cases_size_1_to_300(self):
        answer_sizes = set()
        for size in range(1, 500):
            number_list = data_generator.get_random_list(size, size * 2)
            x = data_generator.get_random_x(size)
            answer = algorithms.naive_n_square(number_list, x)
            answer_sizes.add(len(answer))
            self.assertTrue(analyzer_utils.all_are_int_pairs(answer))
            self.assertTrue(analyzer_utils.list_has_no_repeated_pairs(answer))
            self.assertTrue(analyzer_utils.all_pairs_sum_x(answer, x))

        print(f"\n\nAnswer sizes found in naive algorithm random tests: \n\n{answer_sizes}\n\n")


if __name__ == "__main__":
    unittest.main()
