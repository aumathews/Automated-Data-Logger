import serial
import csv
import os
from datetime import datetime

COM_PORT = "COM3"
BAUD_RATE = 115200
CSV_FILENAME = "sensor_data.csv"
DEVICE_ID = "ESP32_Node_1"

print(f"Connecting to ESP32 on {COM_PORT}...")

try:
    with serial.Serial(
        port=COM_PORT,
        baudrate=BAUD_RATE,
        timeout=1
    ) as ser:

        print("Serial connection established!")
        print("Waiting for temperature data...")
        print("Press Ctrl+C to stop.\n")

        write_header = (
            not os.path.exists(CSV_FILENAME)
            or os.path.getsize(CSV_FILENAME) == 0
        )

        with open(
            CSV_FILENAME,
            mode="a",
            newline="",
            encoding="utf-8"
        ) as file:

            csv_writer = csv.writer(file)

            if write_header:
                csv_writer.writerow([
                    "Timestamp",
                    "Device_ID",
                    "Temperature_F"
                ])
                file.flush()

            while True:
                raw_data = ser.readline().decode(
                    "utf-8",
                    errors="ignore"
                ).strip()

                if not raw_data:
                    continue

                try:
                    temperature = float(raw_data)

                except ValueError:
                    print(f"Ignored: {raw_data}")
                    continue

                current_time = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

                print(
                    f"[{current_time}] "
                    f"{DEVICE_ID}: "
                    f"{temperature:.2f} F"
                )

                csv_writer.writerow([
                    current_time,
                    DEVICE_ID,
                    temperature
                ])

                file.flush()

except serial.SerialException as e:
    print(f"\nSERIAL ERROR: {e}")
    print("Check the COM port and USB connection.")
    print("Make sure Thonny is disconnected.")

except KeyboardInterrupt:
    print("\nData collection stopped by user.")

except OSError as e:
    print(f"\nFILE ERROR: {e}")

finally:
    print("Serial logger shutdown complete.")
    