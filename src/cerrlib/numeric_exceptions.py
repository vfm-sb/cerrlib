"""Custom Numeric Exceptions"""

from typing import Any


class InvalidDecimalValueError(ValueError):

    def __init__(
        self,
        message: str = "Invalid Decimal Value",
        value: Any | None = None,
    ) -> None:
        self.message = message
        if value is not None:
            self.message += f">> '{value}' (Type: {type(value).__name__})."
        super().__init__(self.message)
