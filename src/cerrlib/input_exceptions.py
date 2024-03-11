"""Custom Input Exceptions"""


class MissingInputError(ValueError):
    def __init__(self, message: str = "Missing Input") -> None:
        self.message = message
        super().__init__(self.message)
