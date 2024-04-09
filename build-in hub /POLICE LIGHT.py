from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub()

# Turn the light on and off 5 times.
for i in range(5):

    hub.light.on(Color.BLUE)
    wait(100)
    hub.light.on(Color.RED)
    wait(100)

    
