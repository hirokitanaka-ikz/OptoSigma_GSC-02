import serial

class GSC02Controller:
    def __init__(self, port, baud_rate=9600):
        self.ser = serial.Serial(
            port=port,
            baudrate=baud_rate,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=1
        )
        self.delimiter = "\r\n"

    def send_command(self, command):
        full_command = f"{command}{self.delimiter}"
        self.ser.write(full_command.encode())

    def receive_response(self):
        response = self.ser.read_until(self.delimiter.encode()).decode().strip()
        return response

    def return_origin(self, axis:int, direction:str):
        self.send_command(f"H:{axis}{direction}")

    def set_relative_move(self, axis:int, Npulse:int):
        if Npulse > 0:
            self.send_command(f"M:{axis}+P{Npulse}")
        elif Npulse < 0:
            Npulse = abs(Npulse)
            self.send_command(f"M:{axis}-P{Npulse}")

    def set_absolute_move(self, axis:int, sign:str, pos:int):
        self.send_command(f"A:{axis}{sign}P{pos}")

    def set_jog(self, axis:int, direction:str):
        self.send_command(f"J:{axis}{direction}")

    def drive(self):
        self.send_command("G:")

    def stop(self, axis:int):
        self.send_command(f"L:{axis}")

    def emergency_stop(self):
        self.send_command("L:E")

    def set_origin(self, axis):
        self.send_command(f"R:{axis}")

    def set_speed(self, axis, min_speed_pps:int=500, max_speed_pps:int=5000, acceleration_time:int=200):
        # min speed (S): 1 - 30000 pps
        # max speed (F): 1 - 30000 pps (F>=S)
        # acceleration/deceleration time: 1 - 1000 ms
        if min_speed_pps < 0 or max_speed_pps < 0 or acceleration_time < 0:
            print("parameter negative")
        self.send_command(f"D:{axis}S{min_speed_pps}F{max_speed_pps}R{acceleration_time}")

    def get_position(self, axis):
        self.send_command("Q:")
        response = self.receive_response().split(",")
        if axis==1:
            return response[0]
        if axis==2:
            return response[1]

    def get_status(self):
        self.send_command("!:")
        return self.receive_response()

    def get_internal_info(self, param, axis=None):
        if axis:
            self.send_command(f"?:{param}{axis}")
        else:
            self.send_command(f"?:{param}")
        return self.receive_response()

    def close(self):
        self.ser.close()
