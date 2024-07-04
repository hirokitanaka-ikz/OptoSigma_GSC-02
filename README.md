
# GSC-02 Two-Axis Stage Controller (OptoSigma)

This repository contains code for controlling a two-axis stage controller (GSC-02) from OptoSigma using Python. The main components include the `GSC02Controller` class for interfacing with the motor driver and an example usage in `main.py`.

## Files

- `gsc02controller.py`: Contains the `GSC02Controller` class which provides methods to control the GSC-02 motor driver.
- `main.py`: Demonstrates how to use the `GSC02Controller` class to control the motor driver.

## Requirements

- Python 3.x
- `pyserial` library

You can install the required library using pip:

```bash
pip install pyserial
```

## Usage

1. **Initialize the Controller:**

   Ensure that the correct COM port is set for your environment in `main.py`:

   ```python
   COM_PORT = "COM4"
   ```

2. **Run the Example:**

   Execute `main.py` to see an example of how to use the `GSC02Controller` class:

   ```bash
   python main.py
   ```

## GSC02Controller Class

### Initialization

```python
controller = GSC02Controller(port="COM4", baud_rate=9600)
```

### Methods

- **send_command(command)**: Sends a command to the motor driver.
- **receive_response()**: Receives a response from the motor driver.
- **return_origin(axis, direction)**: Returns the specified axis to its origin.
- **set_relative_move(axis, Npulse)**: Moves the specified axis relatively by the given number of pulses.
- **set_absolute_move(axis, sign, pos)**: Moves the specified axis to an absolute position.
- **set_jog(axis, direction)**: Sets the jog movement for the specified axis.
- **drive()**: Executes the movement command.
- **stop(axis)**: Stops the movement of the specified axis.
- **emergency_stop()**: Executes an emergency stop.
- **set_origin(axis)**: Sets the current position as the origin for the specified axis.
- **set_speed(axis, min_speed_pps, max_speed_pps, acceleration_time)**: Sets the speed parameters for the specified axis.
- **get_position(axis)**: Gets the current position of the specified axis.
- **get_status()**: Gets the current status of the motor driver.
- **get_internal_info(param, axis=None)**: Gets internal information of the motor driver.
- **close()**: Closes the serial connection.

## Example Usage in main.py

The `main.py` file demonstrates how to use the `GSC02Controller` class to control the GSC-02 motor driver. It includes examples of:

- Initializing the controller.
- Homing the axes.
- Performing absolute and relative movements.
- Jogging the axes.
- Stopping movements.
- Querying positions and device status.

## License

This project is licensed under the MIT License.
