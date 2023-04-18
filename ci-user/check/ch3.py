import base

EXPECTED_3 = [
    # ch3_sleep
    r"get_time OK2862417256307925537457268316233964455! (\d+)",
    "Test sleep OK2862417256307925537457268316233964455!",

    # ch3_sleep1
    r"current time_msec = (\d+)",
    r"time_msec = (\d+) after sleeping (\d+) ticks, delta = (\d+)ms!",
    "Test sleep1 passed2862417256307925537457268316233964455!",

    # ch3_taskinfo
    "string from task info test",
    "Test task info OK2862417256307925537457268316233964455!",
]

if __name__ == "__main__":
    base.test(EXPECTED_3)
