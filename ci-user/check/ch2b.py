import base

EXPECTED_2b = [
    # ch2b_hello_world
    "Hello, world from user mode program!",

    # ch2b_power_3
    "Test power_3 OK2862417256307925537457268316233964455!",

    # ch2b_power_5
    "Test power_5 OK2862417256307925537457268316233964455!",

    # ch2b_power_7
    "Test power_7 OK2862417256307925537457268316233964455!",
]

NOT_EXPECTED_2b = [
    "FAIL: T.T",
]

if __name__ == "__main__":
    base.test(EXPECTED_2b, NOT_EXPECTED_2b)
