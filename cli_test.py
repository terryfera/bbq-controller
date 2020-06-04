import time
from modules.db import create_cook, create_connection, log_data
from modules.monitor import adjust_temp

database = "db/bbqc.db"

conn = create_connection(database)

if __name__ == "__main__":
    with conn:
        # create a new cookid
        """cook = (
            "2020-06-04",
            "2020-06-04 15:30:00",
            "2020-06-04 17:04:00",
            "My first DB Cook",
        )
        cookid = create_cook(conn, cook)
        print(conn)"""
        # logitem = ("2", "2020-06-04 15:30:30", "164", "224", "TRUE", "35")
        # log_data(conn, logitem)

        adjust_temp(conn, "2", "155", "225")
