from matplotlib import pyplot as plt

from body import Body

from animator import Animator3D

EARTH_RADIUS = 6738 * 1000  # Radius in [m]
ground = Body(EARTH_RADIUS, "ground station")
server = Body(EARTH_RADIUS + 422 * 10 ** 3, "server")
satellite = Body(EARTH_RADIUS + 35678 * 10 ** 3, "satellite")

bodies = (ground, server, satellite)
timeseries = [*range(1, 100000)]
animator = Animator3D(bodies, timeseries)
# animator.animate(frames=1000)
animator._create_animation_frame(100)
plt.show()
