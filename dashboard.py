import random
from datetime import datetime
import statistics
import matplotlib.pyplot as plt


class Dashboard:
    def display_data(self, data):
        print(
            "------------------------------------------- Displaying data: -----------------------------------------"
        )
        for timestamp, value in data:
            print(f"{timestamp} - {value}")

    def display_analytics(self, analytics):
        print(
            "----------------------------------------- Displaying analytics: --------------------------------------"
        )
        print(f"Minimum value: {analytics['min']}")
        print(f"Maximum value: {analytics['max']}")
        print(f"Average value: {analytics['mean']}")
        print(f"Median value: {analytics['median']}")
        print(f"Standard deviation: {analytics['stdev']}")

        print(
            "------------------------------------------- Displaying time: ---------------------------------"
        )
        print(f"Start time: {analytics['start_time']}")
        print(f"End time: {analytics['end_time']}")
