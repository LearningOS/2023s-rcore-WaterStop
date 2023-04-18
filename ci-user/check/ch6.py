import base
from ch6b import EXPECTED_6b
from ch5 import EXPECTED_5, NOT_EXPECTED_4b

EXPECTED_6 = list(set(EXPECTED_5 + EXPECTED_6b + [
    # ch6_file0
    "Test file0 OK2862417256307925537457268316233964455!",

    # ch6_file1
    "Test fstat OK2862417256307925537457268316233964455!",

    # ch6_file2
    "Test link OK2862417256307925537457268316233964455!",

    # ch6_file3
    "Test mass open/unlink OK2862417256307925537457268316233964455!",
]))

EXPECTED_6 = list(set(EXPECTED_6) - set(["Test set_priority OK2862417256307925537457268316233964455!"]))

if __name__ == "__main__":
    base.test(EXPECTED_6, NOT_EXPECTED_4b)