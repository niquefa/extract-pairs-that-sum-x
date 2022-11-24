from analyzer import data_generator
from analyzer import algorithms
from analyzer import constants


for size in range(constants.SIZE_FROM, constants.SIZE_TO):
    for _ in range(constants.MAX_ITERATION_BY_SIZE):
        number_list = data_generator.get_random_list(size, size * 2)
        x = data_generator.get_random_x(size)
        answer = algorithms.naive_n_square(number_list, x)

        if len(answer) == 0:
            continue

        with open(constants.INPUT_TEST_CASES_FILE, "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            file_object.write(",".join(str(item) for item in number_list) + " " + str(x))

        with open(constants.OUTPUT_TEST_CASES_FILE, "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            file_object.write(",".join(str(pair[0]) + " " + str(pair[1]) for pair in answer))
