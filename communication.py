# comment each line with an explination, at the end  the code should be veiwed as it is written by you (a professional developer)


class Communication:
    def __init__(
        self, server_url
    ):  # __init__ method that takes a single argument server_url
        self.server_url = server_url  # now server_url is an instance variable that can be accessed by other methods within the class

    def send_data(
        self, data
    ):  # this methods prints the server where the data was sent and the data itself
        print(f"Sending data to {self.server_url}: {data}")

    def receive_data(self):  # this method prints where the data was received from
        print(f"Receiving data from {self.server_url}")
