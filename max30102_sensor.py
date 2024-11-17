# max30102_sensor.py
from heartrate_monitor import HeartRateMonitor
import time

def read_max30102(raw=False, duration=30):
    """
    Reads data from the MAX30102 sensor and returns heart rate and SpO2 data.
    Args:
        raw (bool): If True, reads raw data; otherwise, reads calculated result.
        duration (int): Duration in seconds to read from the sensor.
    Returns:
        list of tuples: A list of (heart_rate, spo2) readings.
    """
    readings = []

    print("Starting MAX30102 sensor...")
    hrm = HeartRateMonitor(print_raw=raw, print_result=(not raw))
    hrm.start_sensor()

    start_time = time.time()
    try:
        while time.time() - start_time < duration:
            # Assuming HeartRateMonitor has attributes for heart rate and SpO2
            heart_rate = getattr(hrm, 'heart_rate', None)
            spo2 = getattr(hrm, 'spo2', None)
            
            # Add to readings if both values are available
            if heart_rate is not None and spo2 is not None:
                readings.append((heart_rate, spo2))
                
            time.sleep(1)  # Check once per second, adjust as needed for frequency

    except KeyboardInterrupt:
        print("Keyboard interrupt detected, stopping sensor...")
    
    hrm.stop_sensor()
    print("MAX30102 sensor stopped.")
    return readings
