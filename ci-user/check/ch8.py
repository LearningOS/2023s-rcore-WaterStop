import base
from ch6b import EXPECTED_6b, NOT_EXPECTED_4b

EXPECTED_8 = EXPECTED_6b + [
    # ch7b_pipetest
    "pipetest passed2862417256307925537457268316233964455!",

    # ch8b_mpsc_sem
    "mpsc_sem passed2862417256307925537457268316233964455!",

    # ch8b_phil_din_mutex
    "philosopher dining problem with mutex test passed2862417256307925537457268316233964455!",

    # ch8b_race_adder_mutex_spin
    "race adder using spin mutex test passed2862417256307925537457268316233964455!",

    # ch8b_sync_sem
    "sync_sem passed2862417256307925537457268316233964455!",

    # ch8b_test_condvar
    "test_condvar passed2862417256307925537457268316233964455!",

    # ch8b_threads_arg
    "threads with arg test passed2862417256307925537457268316233964455!",

    # ch8b_threads
    "threads test passed2862417256307925537457268316233964455!",

    # ch8_deadlock_mutex1
    "deadlock test mutex 1 OK2862417256307925537457268316233964455!",

    # ch8_deadlock_sem1
    "deadlock test semaphore 1 OK2862417256307925537457268316233964455!",

    # ch8_deadlock_sem2
    "deadlock test semaphore 2 OK2862417256307925537457268316233964455!",
]

EXPECTED_8 = list(set(EXPECTED_8) - set(["Test sbrk almost OK2862417256307925537457268316233964455!"]))

if __name__ == "__main__":
    base.test(EXPECTED_8, NOT_EXPECTED_4b)
