import base
from ch5b import EXPECTED_5b, NOT_EXPECTED_4b

EXPECTED_6b = EXPECTED_5b + [
    # ch6b_filetest_simple.rs
    "file_test passed2862417256307925537457268316233964455!",
]

if __name__ == '__main__':
    base.test(EXPECTED_6b, NOT_EXPECTED_4b)
