import sys
import time


def wait_for_3s():
    time.sleep(3)


def wait_for_5s():
    time.sleep(5)


def wait_for_10s():
    time.sleep(10)


if __name__ == '__main__':
    actions = {'wait_for_3s': wait_for_3s,
               'wait_for_5s': wait_for_5s,
               'wait_for_10s': wait_for_10s}

    action = sys.argv[1]
    args = sys.argv[2:]
    actions[action](*args)