class InvalidInputDataError(Exception):
    """Exception raised for errors in the input.

    Attributes:
        number_list -- the given number list
        x -- the given number to check for pairs than sum up to it
    """

    def __init__(
        self,
        number_list,
        x,
        message="Invalid input data, expecting a list with no duplicates of integers and a integer number x",
    ):
        self.number_list = number_list
        self.x = x
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"List: {self.number_list}, x: {self.x} -> {self.message}"


class InvalidAppArgumentsError(Exception):
    """Exception raised for errors in the program arguments.

    Attributes:
        args -- the given arguments for the app
    """

    def __init__(
        self,
        args,
        message="Invalid arguments set, expecting two arguments: a comma separated list with no spaces, of integers and a integer number x",
    ):
        if args is not None:
            self.args = args
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"args: {self.args} -> {self.message}"
