import serial
import time

# Configure Serial Port
SERIAL_PORT = "/dev/ttyUSB1"  # Change to /dev/ttyS0 if using GPIO UART
BAUD_RATE = 115200

try:
    # Open serial connection
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud.")
    while True:
        # Read response
        # response = ser.readline().decode().strip()
        data = ser.readline()
        if len(data) > 0:
            print(data.decode('utf-8'))

except serial.SerialException as e:
    print(f"Error: {e}")
