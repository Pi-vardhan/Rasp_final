import Adafruit_DHT

# Set the sensor type and the GPIO pin number
sensor = Adafruit_DHT.DHT22
pin = 16  # GPIO pin where the DATA pin of the DHT22 is connected

def read_dht22():
    """
    Reads humidity and temperature from the DHT22 sensor.
    Returns:
        tuple: (temperature, humidity) if successful, otherwise None.
    """
    humidity, temperature = Adafruit_DHT.read(sensor, pin)
    
    if humidity is not None and temperature is not None:
        return temperature, humidity
    else:
        print("Failed to retrieve data from the sensor")
        return None

# Example usage in the main code
if __name__ == "__main__":
    try:
        while True:
            result = read_dht22()
            if result:
                temperature, humidity = result
                print(f'Temperature: {temperature:.1f}°C, Humidity: {humidity:.1f}%')
    except KeyboardInterrupt:
        print("Exiting program")
