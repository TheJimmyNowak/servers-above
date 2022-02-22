import numpy.typing as npt

Position = npt.NDArray[float]


class InclinationValueError(Exception):
    """Custom error raised when inclination is not in proper range"""

    def __init__(self, value: float, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)
