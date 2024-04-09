from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub()

# Turn the light on and off 5 times.
while True:
    hub.light.on(Color.BLUE)
    wait(200)
    hub.light.on(Color.RED)
    wait(200)
    

    
