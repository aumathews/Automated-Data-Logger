# Local Telemetry Ingestion Pipeline

## Project Overview
This project bridges the gap between hardware microcontrollers and PC-side data science. It utilizes an ESP32 to generate environmental telemetry and a standard Python script (`logger.py`) to intercept that data over a serial connection. The data is timestamped and appended to a persistent CSV file for long-term analysis.

## Prerequisites
* Python 3.x installed on the host PC.
* `pyserial` library installed (`pip install pyserial`).
* An ESP32 connected via USB, running a script that prints numeric data to standard output.

## Execution
1. Ensure the ESP32 is plugged in and running its emitter script.
2. **Important:** Close Thonny or any other Serial Monitor, as only one program can access a COM port at a time.
3. Update the `COM_PORT` variable in `logger.py` to match your system.
4. Run the script:

    python logger.py

5. Press `Ctrl+C` to gracefully stop the ingestion and securely save the CSV file.
