""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    determines the duration between the initial and last shutdown events documented in the provided log file
    """
    shutdown_events = get_shutdown_events(logfile)
    first_shutdown_event = shutdown_events[0].split()[1]
    last_shutdown_event = shutdown_events[-1].split()[1]
    first_shutdown_timestamp = logstamp_to_datetime(first_shutdown_event)
    last_shutdown_timestamp = logstamp_to_datetime(last_shutdown_event)
    return last_shutdown_timestamp - first_shutdown_timestamp






# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
