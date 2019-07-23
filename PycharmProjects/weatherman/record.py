from datetime import datetime


class WeatherData:
    def __init__(self, data):
        self.date = datetime.strptime(data.get("PKT", data.get("PKST")), '%Y-%m-%d')
        self.highest_temp = int(data["Max TemperatureC"])
        self.lowest_temp = int(data["Min TemperatureC"])
        self.avg_humidity = int(data[" Mean Humidity"])
        self.highest_humidity = int(data["Max Humidity"])

