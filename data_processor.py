import statistics
from datetime import datetime


class DataProcessor:
    def generate_analytics(self, data):
        # functions from statistics:
        mean = round((statistics.mean([x[1] for x in data])), 2)
        median = round((statistics.median([x[1] for x in data])), 2)
        stdev = round((statistics.stdev([x[1] for x in data])), 2)

        min_value = round(min([x[1] for x in data]), 2)
        max_value = round(max([x[1] for x in data]), 2)

        start_time = data[0][0]
        end_time = data[-1][0]

        return {
            "data": [x[1] for x in data],
            "mean": mean,
            "median": median,
            "stdev": stdev,
            "min": min_value,
            "max": max_value,
            "start_time": start_time,
            "end_time": end_time,
        }
