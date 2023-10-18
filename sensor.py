import random
from datetime import datetime

class Sensor:
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
        
    def read_data(self):
        data = round(random.uniform(self.minimum, self.maximum), 2)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return (timestamp, data)


