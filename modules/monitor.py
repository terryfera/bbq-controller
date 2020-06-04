import time
import datetime
from modules.db import log_data


def gen_timestamp():
    """
    Return timestamp in SQL datetime format
    """

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    return timestamp


def adjust_temp(conn, cookid, current_temp, target_temp):
    """
    Adjust temperature until it reaches within 10% of target
    """
    current_temp = int(current_temp)
    target_temp = int(target_temp)

    while current_temp != (target_temp * 0.95) or current_temp != (target_temp * 1.05):
        if current_temp > target_temp:
            while current_temp > target_temp or current_temp > (target_temp * 1.05):
                current_temp = round((current_temp * 0.97), 2)

                print(
                    f"Current Temperature is {current_temp}: no fan required, waiting to lower"
                )

                logitem = (cookid, gen_timestamp(), current_temp, "224", "TRUE", "35")

                log_data(conn, logitem)

                time.sleep(2)
            else:
                print(
                    f"Current Temperature is {current_temp}: target temperature reached"
                )

                logitem = (cookid, gen_timestamp(), current_temp, "224", "TRUE", "35")

                log_data(conn, logitem)

                break
        elif current_temp < target_temp:
            while current_temp < (target_temp * 0.95):
                current_temp = round((current_temp * 1.03), 2)
                print(f"Current Temperature is {current_temp}: raising with fan")

                logitem = (cookid, gen_timestamp(), current_temp, "224", "TRUE", "35")

                log_data(conn, logitem)

                time.sleep(2)
            else:
                print(
                    f"Current Temperature is {current_temp}: target temperature reached"
                )

                logitem = (cookid, gen_timestamp(), current_temp, "224", "TRUE", "35")

                log_data(conn, logitem)

                break
        else:
            print(f"Nothing to do")
            break

    return current_temp


"""
while monitor_temp == 1:
    print(f"The current temperature is {current_temp}")
    current_temp = int(input("Enter new temp: "))
    print(f"The new temperature is {current_temp}")
    current_temp = adjust_temp(current_temp, target_temp)
"""
