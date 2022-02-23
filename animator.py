import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
from matplotlib import animation
from typing import Tuple

from body import Body
from abc import ABC, abstractmethod


class Animator(ABC):
    def __init__(self, bodies: Tuple[Body], timeseries: list):
        self.bodies = bodies
        self.timeseries = timeseries
        self.bodies_positions = self._generate_bodies_positions()

    def _generate_bodies_positions(self) -> npt.NDArray:
        """
        Generates positions for each body by timeseries.
        """
        positions = np.zeros([len(self.timeseries), len(self.bodies) * 3])

        for index, body in enumerate(self.bodies):
            positions[:, index * 3:(index + 1) * 3] = body.get_pos_by_timeseries(self.timeseries)

        return np.rot90(positions)

    @abstractmethod
    def _create_animation_frame(self, t: int) -> None:
        """
        Function to create ONE timeframe of animation

        :param int t: Current frame
        """
        pass

    def animate(self, interval=10, frames=100, filename='simulation.gif') -> None:
        """
        Creates animation and saves it as a file
        """
        print("Animation will be with ya in a moment. Just wait! ^^")
        anim = animation.FuncAnimation(plt.gcf(),
                                       self._create_animation_frame,
                                       interval=interval, frames=frames)
        anim.save(filename)
        print("Here it is! Enjoy in your sexy orbits ")


class Animator3D(Animator):
    """
    Class to create 3D animation based on bodies.
    """

    def __init__(self, bodies: Tuple[Body], timeseries: list):
        super().__init__(bodies, timeseries)
        plt.axes(projection='3d')

    def _create_animation_frame(self, t: int) -> None:
        plt.cla()
        bodies_positions = self.bodies_positions[:, :t]

        for i, body in enumerate(self.bodies):
            body_positions = bodies_positions[i * 3:(i + 1) * 3, :]
            x, y, z = body_positions
            plt.plot(z, x, y, label=str(body))  # TODO:  CHANGE COORDINATES SYSTEM
            plt.legend()


class Animator2D(Animator):
    """
    Class to create 2D animation based on bodies.
    """
    def __init__(self, bodies: Tuple[Body], timeseries: list):
        super(Animator2D, self).__init__(bodies, timeseries)

        f = plt.figure()
        f.set_figwidth(10)
        f.set_figheight(10)
        highest_orbit = max(bodies).orbit_radius
        self.axes_range = [-highest_orbit, highest_orbit]

    def _create_animation_frame(self, t: int) -> None:
        plt.cla()
        bodies_positions = self.bodies_positions[:, :t]

        for i, body in enumerate(self.bodies):
            body_positions = bodies_positions[i * 3:(i + 1) * 3, :]
            x, y, z = body_positions
            plt.plot(x, z, label=str(body))
            plt.legend()
            plt.xlim(self.axes_range)
            plt.ylim(self.axes_range)
