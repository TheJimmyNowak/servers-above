import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
from matplotlib import animation

from body import Body
from utils import Position


class Animator:
    """
    Class to create animation based on bodies.
    """

    def __init__(self, bodies: tuple[Body], timeseries: list):
        self.bodies = bodies
        self.timeseries = timeseries

    def _generate_bodies_positions(self) -> npt.NDArray[Position]:
        """
        Generates positions for each body by timeseries.
        """
        positions = np.zeros([len(self.bodies)*3, len(self.timeseries)])

        for index, body in enumerate(self.bodies):
            positions[index*3:(index+1)*3, :] = body.get_pos_by_timeseries(self.timeseries).reshape((3, 1))
        # TODO: Cannot insert position in one field
        return positions

    def _create_animation_frame(self, t: int) -> None:
        """
        Function to create ONE timeframe of animation

        :param int t: Current frame
        """
        plt.cla()

        for body_positions in self._generate_bodies_positions():  # TODO: Cut returned value
            plt.plot(body_positions[0], body_positions[1], body_positions[2])

        plt.rcParams["figure.autolayout"] = True
        plt.xlim([-60000000, 60000000])
        plt.ylim([-60000000, 60000000])

    def animate(self, interval=10, frames=10, filename='simulation.gif') -> None:
        """
        Creates animation and saves it as a file
        """
        anim = animation.FuncAnimation(plt.gcf(),
                                       self._create_animation_frame,
                                       interval=interval, frames=frames)
        anim.save(filename, writer='imagemagic')