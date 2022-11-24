import logging
from datetime import datetime
from analyzer import constants
from analyzer import exceptions


def parse_arguments(args):
    return list(map(int, args[1].split(","))), int(args[2])


def validate_app_arguments(args):
    if args is None:
        log_error(exceptions.InvalidAppArgumentsError(args), "Args list is None")
        raise exceptions.InvalidAppArgumentsError(args)

    if len(args) < 3:
        log_error(exceptions.InvalidAppArgumentsError(args), "Two few arguments")
        raise exceptions.InvalidAppArgumentsError(args)

    if len(args) > 3:
        log_error(exceptions.InvalidAppArgumentsError(args), "Two much arguments")
        raise exceptions.InvalidAppArgumentsError(args)


def validate_input(number_list, x):
    if number_list is None:
        log_error(exceptions.InvalidInputDataError(number_list, x), "List is None")
        raise exceptions.InvalidInputDataError(number_list, x)

    if x is None:
        log_error(exceptions.InvalidInputDataError(number_list, x), "x is None")
        raise exceptions.InvalidInputDataError(number_list, x)

    if not isinstance(x, int):
        log_error(exceptions.InvalidInputDataError(number_list, x), "x is not int")
        raise exceptions.InvalidInputDataError(number_list, x)

    if len(number_list) == 0:
        log_error(exceptions.InvalidInputDataError(number_list, x), "List is empty")
        raise exceptions.InvalidInputDataError(number_list, x)

    if any(number is None for number in number_list):
        log_error(exceptions.InvalidInputDataError(number_list, x), "List has None values")
        raise exceptions.InvalidInputDataError(number_list, x)

    if any(not isinstance(number, int) for number in number_list):
        log_error(exceptions.InvalidInputDataError(number_list, x), "List has not integer values")
        raise exceptions.InvalidInputDataError(number_list, x)

    if len(set(number_list)) != len(number_list):
        log_error(exceptions.InvalidInputDataError(number_list, x), "List has duplicates")
        raise exceptions.InvalidInputDataError(number_list, x)


def all_are_int_pairs(tuple_list):
    if tuple_list is None:
        return False
    if not isinstance(tuple_list, list):
        return False
    return all(isinstance(x, tuple) and are_tuple_pair_of_ints(x) for x in tuple_list)


def are_tuple_pair_of_ints(x):
    return x is not None and isinstance(x, tuple) and len(x) == 2 and all(isinstance(x, int) for x in list(x))


def are_int_pairs_and_equal(a, b):
    return are_tuple_pair_of_ints(a) and are_tuple_pair_of_ints(b) and sorted(a) == sorted(b)


def list_has_no_repeated_pairs(number_list):
    return len(set([tuple(sorted(x)) for x in number_list])) == len(number_list)


def list_are_equal(a, b):
    if a == None and b == None:
        return True
    if a == None or b == None:
        return False
    if len(a) != len(b):
        return False
    return sorted([sorted(x) for x in a]) == sorted([sorted(x) for x in b])


def all_pairs_sum_x(number_list, x):
    if number_list is None:
        return False
    if len(number_list) == 0:
        return True
    return all(
        isinstance(t, tuple) and len(t) == 2 and isinstance(t[0], int) and isinstance(t[1], int) and t[0] + t[1] == x
        for t in number_list
    )


def log_error(error_instance, message):
    logging.error(
        {
            "log_time": str(datetime.utcnow()),
            "error_instance_type": type(error_instance),
            "error_instance_args": error_instance.args,
            "error_message": message,
        }
    )
