from sensor import Sensor
from data_processor import DataProcessor
from communication import Communication
from device import Device
from dashboard import Dashboard


def main():
    sensor = Sensor(0, 35)

    data_processor = DataProcessor()

    communication = Communication("https://central-server.example.com")
    device = Device(sensor, data_processor, communication)

    dashboard = Dashboard()

    device.collect_data(5)
    processed_data = device.process_data()

    device.send_data_to_server(processed_data)
    device.receive_data_from_server()

    dashboard.display_data(device.data)
    dashboard.display_analytics(processed_data)


if (
    __name__ == "__main__"
):  # is a common Python idiom that checks whether the current module is being run as the main program or if it is being imported as a module into another program.
    main()
