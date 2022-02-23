import math

import numpy as np
import numpy.typing as npt

from utils import Position, InclinationValueError


class Body:
    _GRAVITATIONAL_CONSTANT = 6.6743 * 10 ** -11

    def __init__(self, orbit_radius,
                 name, central_body_mass=5.972 * 10 ** 24,
                 inclination=0):
        self.name = name
        self.central_body_mass = central_body_mass
        self.orbit_radius = orbit_radius
        self.inclination = inclination

        self.radial_velocity = math.sqrt(
            (self._GRAVITATIONAL_CONSTANT * self.central_body_mass)
            / (self.orbit_radius ** 3)
        )

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.orbit_radius < other.orbit_radius

    @property
    def inclination(self):
        return math.degrees(self._inclination)

    @inclination.setter
    def inclination(self, value: float) -> None:
        if 0 <= value <= 360:
            self._inclination = math.radians(value)
            return

        raise InclinationValueError(value=value,
                                    message="Inclination should be provided in degrees in range of 0 360")

    def _get_true_anomaly(self, t: int) -> float:
        """
        Function used to get true anomaly object of a Body

        :param  int t: Time of motion in seconds
        :return: Returns a true anomaly in time t
        """
        return (self.radial_velocity * t) % math.radians(360)

    def _get_position(self, t: int) -> Position:
        """
        Function used to get Position object of a Body

        :param int t: Time of motion in seconds
        :return: Position of body in time t
        """
        true_anomaly = self._get_true_anomaly(t)
        return np.array([
            self.orbit_radius * math.sin(true_anomaly) * math.cos(self.inclination),
            self.orbit_radius * math.sin(true_anomaly) * math.sin(self.inclination),
            self.orbit_radius * math.cos(true_anomaly)
        ])

    def get_pos_by_timeseries(self, timeseries: list) -> npt.NDArray[Position]:
        """
        Function used to get position changes over time

        :param list timeseries: Timeseries
        """
        positions = [self._get_position(t) for t in timeseries]

        return np.array(positions)
