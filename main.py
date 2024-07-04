from gsc02controller import GSC02Controller
import time
COM_PORT = "COM4"


def wait_until_ready(controller):
    while True:
        if controller.get_status() == "R":
            break
        time.sleep(0.1)


def homing(controller):
    controller.return_origin(axis=1, direction="-")
    wait_until_ready(controller=controller)
    controller.set_origin(axis=1)
    controller.set_origin(axis=2)


def main():
    # create an object
    controller = GSC02Controller(port=COM_PORT)

    # just in case if there is an active process
    controller.stop(axis=1)
    controller.stop(axis=2)

    # get device name
    device_name = controller.get_internal_info(param="N")
    print(f"Device Name: {device_name}")

    # homing
    homing(controller=controller)

    # get positions
    print(f"Stage1: {controller.get_position(axis=1)}")
    print(f"Stage2: {controller.get_position(axis=2)}")

    # absolute move
    controller.set_absolute_move(axis=1, sign="+", pos=10000)
    controller.drive()
    wait_until_ready(controller=controller)
    controller.set_absolute_move(axis=2, sign="+", pos=1000)
    controller.drive()
    wait_until_ready(controller=controller)

    # get positions
    print(f"Stage1: {controller.get_position(axis=1)}")
    print(f"Stage2: {controller.get_position(axis=2)}")

    # relative move
    controller.set_relative_move(axis=1, Npulse=-10000)
    controller.drive()
    wait_until_ready(controller=controller)
    controller.set_relative_move(axis=2, pos=-1000)
    controller.drive()
    wait_until_ready(controller=controller)

    # get positions
    print(f"Stage1: {controller.get_position(axis=1)}")
    print(f"Stage2: {controller.get_position(axis=2)}")

    # jog
    controller.set_jog(axis=1, direction="+")
    controller.drive()
    time.sleep(5)
    controller.stop(axis=1)
    controller.set_jog(axis=2, direction="+")
    controller.drive()
    time.sleep(5)
    controller.stop(axis=2)

    # get positions
    print(f"Stage1: {controller.get_position(axis=1)}")
    print(f"Stage2: {controller.get_position(axis=2)}")

    # Close the connection
    controller.close()


if __name__ == "__main__":
    main()