import unittest
from analyzer import analyzer_utils
from analyzer import exceptions


class AnalyzerUtilTests(unittest.TestCase):
    def test_raises_exception_when_list_is_none(self):
        with self.assertRaises(exceptions.InvalidInputDataError):
            analyzer_utils.validate_input(None, 1)
        pass

    def test_raises_exception_when_x_is_none(self):
        with self.assertRaises(exceptions.InvalidInputDataError):
            analyzer_utils.validate_input([1, 2, 3], None)
        pass

    def test_raises_exception_when_x_is_none(self):
        with self.assertRaises(exceptions.InvalidInputDataError):
            analyzer_utils.validate_input([1, 2, 3], 3.3)
        pass

    def test_raises_exception_when_list_is_empty(self):
        with self.assertRaises(exceptions.InvalidInputDataError):
            analyzer_utils.validate_input([], 4)
        pass

    def test_raises_exception_when_list_has_repeated_values(self):
        with self.assertRaises(exceptions.InvalidInputDataError):
            analyzer_utils.validate_input([1, 2, 1], 4)
        pass

    def test_raises_exception_when_list_has_None_values(self):
        with self.assertRaises(exceptions.InvalidInputDataError):
            analyzer_utils.validate_input([None, 2, 1], 4)
        pass

    def test_raises_exception_when_list_has_non_integer_floating_values(self):
        with self.assertRaises(exceptions.InvalidInputDataError):
            analyzer_utils.validate_input([3.2, 2, 1], 4)
        pass

    def test_raises_exception_when_list_has_non_integer_string_values(self):
        with self.assertRaises(exceptions.InvalidInputDataError):
            analyzer_utils.validate_input(["3", 2, 1], 4)
        pass

    def test_do_not_raises_exception_when_valid_arguments(self):
        analyzer_utils.validate_input([3, 2, 1], 4)
        pass

    def test_raises_exception_when_none_in_arguments(self):
        with self.assertRaises(exceptions.InvalidAppArgumentsError):
            analyzer_utils.validate_app_arguments(None)
        pass

    def test_raises_exception_when_too_few_app_arguments(self):
        with self.assertRaises(exceptions.InvalidAppArgumentsError):
            analyzer_utils.validate_app_arguments(["a"])
        pass

    def test_raises_exception_when_too_much_app_arguments(self):
        with self.assertRaises(exceptions.InvalidAppArgumentsError):
            analyzer_utils.validate_app_arguments(["a", "b", "c", "d"])
        pass

    def test_do_not_raises_exception_when_valid_arguments_size(self):
        analyzer_utils.validate_app_arguments(["a", "b", "c"])
        pass

    def test_all_are_int_pairs_when_false(self):
        self.assertFalse(analyzer_utils.all_are_int_pairs([(1, 2), (2, 1.0)]))
        self.assertFalse(analyzer_utils.all_are_int_pairs([(1, 2), 2]))
        self.assertFalse(analyzer_utils.all_are_int_pairs([(1, 2), "2"]))
        self.assertFalse(analyzer_utils.all_are_int_pairs([(1, 2.0)]))
        self.assertFalse(analyzer_utils.all_are_int_pairs([(1, 2, 4), (-1, 4), (4, -2), (1, 2)]))
        self.assertFalse(analyzer_utils.all_are_int_pairs([(1, 2), (-1, 4), (4, -2), 2]))
        pass

    def test_all_are_int_pairs_when_true(self):
        self.assertTrue(analyzer_utils.all_are_int_pairs([]))
        self.assertTrue(analyzer_utils.all_are_int_pairs([(1, 2)]))
        self.assertTrue(analyzer_utils.all_are_int_pairs([(1, 2), (-10, 13), (3, 0), (6, -3)]))
        self.assertTrue(analyzer_utils.all_are_int_pairs([(-12, 2), (-11, 1), (-10, 0), (6, -16)]))
        pass

    def test_are_int_pairs_and_equal_when_not_pairs_or_not_ints(self):
        self.assertFalse(analyzer_utils.are_int_pairs_and_equal(None, (1, 2)))
        self.assertFalse(analyzer_utils.are_int_pairs_and_equal((1, 2), None))
        self.assertFalse(analyzer_utils.are_int_pairs_and_equal((1, 2, 3), (1, 2)))
        self.assertFalse(analyzer_utils.are_int_pairs_and_equal((1, 2), (1, 2, 3)))
        self.assertFalse(analyzer_utils.are_int_pairs_and_equal((1), (1, 2)))
        self.assertFalse(analyzer_utils.are_int_pairs_and_equal((1, 2), (1)))
        self.assertFalse(analyzer_utils.are_int_pairs_and_equal((1, -1), (1, 2)))
        self.assertFalse(analyzer_utils.are_int_pairs_and_equal((1, 2), (1, 1)))
        self.assertFalse(analyzer_utils.are_int_pairs_and_equal((1, "1"), (1, 1)))
        self.assertFalse(analyzer_utils.are_int_pairs_and_equal((1, 1.0), (1, 1)))
        pass

    def test_are_int_pairs_and_equal_when_equal_and_tuple_pairs(self):
        self.assertTrue(analyzer_utils.are_int_pairs_and_equal((1, 2), (1, 2)))
        self.assertTrue(analyzer_utils.are_int_pairs_and_equal((2, 1), (1, 2)))
        self.assertTrue(analyzer_utils.are_int_pairs_and_equal((-2, -1), (-1, -2)))
        self.assertTrue(analyzer_utils.are_int_pairs_and_equal((2, -1), (-1, 2)))
        self.assertTrue(analyzer_utils.are_int_pairs_and_equal((-2, 1), (1, -2)))
        self.assertTrue(analyzer_utils.are_int_pairs_and_equal((1, 2), (2, 1)))
        self.assertTrue(analyzer_utils.are_int_pairs_and_equal((0, 2), (2, 0)))
        self.assertTrue(analyzer_utils.are_int_pairs_and_equal((2, 0), (0, 2)))
        self.assertTrue(analyzer_utils.are_int_pairs_and_equal((2, 0), (2, 0)))
        pass

    def test_list_are_equal_when_false(self):
        self.assertFalse(analyzer_utils.list_are_equal(None, [(1, 2)]))
        self.assertFalse(analyzer_utils.list_are_equal([(1, 2)], None))
        self.assertFalse(analyzer_utils.list_are_equal([(1, 2)], [(1, -2)]))
        self.assertFalse(analyzer_utils.list_are_equal([(1, 2)], []))
        self.assertFalse(analyzer_utils.list_are_equal([], [(1, 2)]))
        self.assertFalse(analyzer_utils.list_are_equal([(1, 2), (1, 3)], [(1, 2)]))
        self.assertFalse(analyzer_utils.list_are_equal([(1, 2)], [(1, 2), (1, 3)]))
        self.assertFalse(analyzer_utils.list_are_equal([(1, 2), (1, 3), (1, 4)], [(1, 2), (1, 3)]))
        pass

    def test_list_are_equal_when_true(self):
        self.assertTrue(analyzer_utils.list_are_equal(None, None))
        self.assertTrue(analyzer_utils.list_are_equal([], []))
        self.assertTrue(analyzer_utils.list_are_equal([(1, 2)], [(1, 2)]))
        self.assertTrue(analyzer_utils.list_are_equal([(1, 2)], [(2, 1)]))
        self.assertTrue(analyzer_utils.list_are_equal([(1, 2), (5, 4), (2, 3)], [(4, 5), (2, 1), (3, 2)]))
        self.assertTrue(analyzer_utils.list_are_equal([(1, -2)], [(1, -2)]))
        self.assertTrue(analyzer_utils.list_are_equal([(-1, 2)], [(2, -1)]))
        self.assertTrue(analyzer_utils.list_are_equal([(1, 2), (-5, 4), (2, -3)], [(4, -5), (2, 1), (-3, 2)]))
        pass

    def test_all_pairs_sum_x_when_false(self):
        self.assertFalse(analyzer_utils.all_pairs_sum_x([(1, 2)], 2))
        self.assertFalse(analyzer_utils.all_pairs_sum_x([(1, 2), (-1, 4), (4, -2)], 3))
        pass

    def test_all_pairs_sum_x_when_true(self):
        self.assertTrue(analyzer_utils.all_pairs_sum_x([], 2))
        self.assertTrue(analyzer_utils.all_pairs_sum_x([(1, 2)], 3))
        self.assertTrue(analyzer_utils.all_pairs_sum_x([(1, 2), (-10, 13), (3, 0), (6, -3)], 3))
        self.assertTrue(analyzer_utils.all_pairs_sum_x([(-12, 2), (-11, 1), (-10, 0), (6, -16)], -10))
        pass

    def test_list_has_no_repeated_pairs_when_false(self):
        self.assertFalse(analyzer_utils.list_has_no_repeated_pairs([(1, 2), (2, 1)]))
        self.assertFalse(analyzer_utils.list_has_no_repeated_pairs([(1, 2), (-1, 4), (4, -2), (1, 2)]))
        self.assertFalse(analyzer_utils.list_has_no_repeated_pairs([(1, 2), (-1, 4), (4, -2), (2, 1)]))
        pass

    def test_list_has_no_repeated_pairs_when_true(self):
        self.assertTrue(analyzer_utils.list_has_no_repeated_pairs([]))
        self.assertTrue(analyzer_utils.list_has_no_repeated_pairs([(1, 2)]))
        self.assertTrue(analyzer_utils.list_has_no_repeated_pairs([(1, 2), (-10, 13), (3, 0), (6, -3)]))
        self.assertTrue(analyzer_utils.list_has_no_repeated_pairs([(-12, 2), (-11, 1), (-10, 0), (6, -16)]))
        pass


if __name__ == "__main__":
    unittest.main()
