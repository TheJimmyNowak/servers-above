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
        self.bodies_positions = self._generate_bodies_positions()
        plt.axes(projection='3d')
        plt.rcParams["figure.autolayout"] = True

    def _generate_bodies_positions(self) -> npt.NDArray[Position]:
        """
        Generates positions for each body by timeseries.
        """
        positions = np.zeros([len(self.bodies) * 3, len(self.timeseries)])

        for index, body in enumerate(self.bodies):
            positions[index * 3:(index + 1) * 3, :] = body.get_pos_by_timeseries(self.timeseries). \
                reshape((3, len(self.timeseries)))
        return positions

    def _create_animation_frame(self, t: int) -> None:
        """
        Function to create ONE timeframe of animation

        :param int t: Current frame
        """
        plt.cla()

        bodies_positions = self.bodies_positions[:, :t]
        for i in range(len(self.bodies)):  # TODO: Cut returned value
            body_positions = bodies_positions[i * 3:(i + 1) * 3, :]
            plt.plot(body_positions[0], body_positions[1],
                     body_positions[2], '.', label=str(self.bodies[i]))
            plt.legend()

        # plt.xlim([-60000000, 60000000])
        # plt.ylim([-60000000, 60000000])

    def animate(self, interval=10, frames=10, filename='simulation.gif') -> None:
        """
        Creates animation and saves it as a file
        """
        print("start")
        anim = animation.FuncAnimation(plt.gcf(),
                                       self._create_animation_frame,
                                       interval=interval, frames=frames)
        anim.save(filename, writer='imagemagic')
        print("stop")
