from typing import Iterable

import matplotlib.pyplot as plt
import numpy as np

from body import Body
from utils import Position


class Animator:
    """
    Class to create animation based on bodies.
    """

    def __init__(self, bodies: tuple[Body], timeframes: list):
        self.bodies = bodies
        self.timeframes = timeframes

        self.bodies_history: np.ndarray([list[Position]]) = []

        for index, body in enumerate(self.bodies):
            self.bodies_history.insert(index, np.array([body.get_position(t) for t in timeframes]))

    def _get_coordinate_history(self, index) -> np.ndarray:
        li = [i[index] for i in self.bodies_history]

        return np.array(li)

    def animate(self, j):
        plt.cla()

        for index, body in enumerate(self.bodies):
            plt.plot(self._get_coordinate_history(0),
                     self._get_coordinate_history(1))

        print(self._get_coordinate_history(0))
        plt.rcParams["figure.autolayout"] = True
        plt.xlim([-60000000, 60000000])
        plt.ylim([-60000000, 60000000])
