import base
from ch6b import EXPECTED_6b, NOT_EXPECTED_4b

EXPECTED_7b = EXPECTED_6b + [
    # ch7b_sig_simple
    "signal_simple: Done",

    # ch7b_pipetest
    "pipetest passed2862417256307925537457268316233964455!",

    # ch7b_pipe_large_test
    "pipe_large_test passed2862417256307925537457268316233964455!",
]

if __name__ == '__main__':
    base.test(EXPECTED_7b, NOT_EXPECTED_4b)
