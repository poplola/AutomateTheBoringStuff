#! Python 3 -> shebang line
# trafficLightSimulation.py
# Using an Assertion in a Traffic Light Simulation
"""
Say you’re building a traffic light simulation program. The data structure representing the stoplights at an intersection is a dictionary with keys 'ns' and 'ew', for the stoplights facing north-south and east-west, respectively. 
The values at these keys will be one of the strings 'green', 'yellow', or 'red'. The code would look something like this:
    market_2nd = {'ns': 'green', 'ew': 'red'} 
    mission_16th = {'ns': 'red', 'ew': 'green'}
These two variables will be for the intersections of Market Street and 2nd Street, and Mission Street and 16th Street. To start the project, 
you want to write a switchLights() function, which will take an intersection dictionary as an argument and switch the lights.
At first, you might think that switchLights() should simply switch each light to the next color in the sequence: Any 'green' values should change to 'yellow', 'yellow' values should change to 'red', and 'red' values should change to 'green'. 

But if while writing switchLights() you had added an assertion to check that at least one
of the lights is always red, you might have included the following at the bottom of the function:
assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
With this assertion in place, your program would crash with this error message:
"""

def switchLights(stoplight): 
    for key in stoplight.keys():
        if stoplight[key] == 'green': 
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow': 
            stoplight[key] = 'red'
        elif stoplight[key] == 'red': 
            stoplight[key] = 'green'
    
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

market_2nd = {'ns': 'green', 'ew': 'red'} 
mission_16th = {'ns': 'red', 'ew': 'green'}

switchLights(market_2nd)
