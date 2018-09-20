import time
from pprint import pprint

import requests

from db import monitora_limiar, delete_data

from setconf import *

INTERVALO = 1


def config():
    post()


def clear():
    delete_data()


def al():
    return alll()


def monitor(limiar=11250000):
    while True:
        if time.time() % INTERVALO == 0:
            pprint(time.time())

            rrs_trs = monitora_limiar(limiar)
            print(rrs_trs)

            if rrs_trs != ([], []):
                delete(rrs_trs)
                break

