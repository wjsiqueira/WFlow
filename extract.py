import pdb
import subprocess

from pprint import pprint
from db import *

import os


import requests

STATS = {}

def extract(datapath, stat, INTERVALO):

    STATS[datapath] = STATS.get(datapath, {})

    STATS[datapath][stat.port_no] = STATS[datapath].get(stat.port_no, {
        'primeira_vez': True,
        'rx_bytes_ant': 0,
        'tx_bytes_ant': 0,
    })

    if STATS[datapath][stat.port_no]['primeira_vez']:
        STATS[datapath][stat.port_no]['primeira_vez'] = False
        STATS[datapath][stat.port_no]['rx_bytes_ant'] = stat.rx_bytes
        STATS[datapath][stat.port_no]['tx_bytes_ant'] = stat.tx_bytes
    else:
        STATS[datapath][stat.port_no]['rx_taxa'] = (stat.rx_bytes - STATS[datapath][stat.port_no]['rx_bytes_ant']) / INTERVALO
        STATS[datapath][stat.port_no]['rx_bytes_ant'] = stat.rx_bytes
        STATS[datapath][stat.port_no]['tx_taxa'] = (stat.tx_bytes - STATS[datapath][stat.port_no]['tx_bytes_ant']) / INTERVALO
        STATS[datapath][stat.port_no]['tx_bytes_ant'] = stat.tx_bytes

        #pprint(STATS)

        manda_pro_banco(datapath, stat.port_no, stat.duration_sec, stat.duration_nsec, 
                    stat.tx_bytes, 
                    STATS[datapath][stat.port_no]['tx_taxa'], 
                    stat.rx_bytes, 
                    STATS[datapath][stat.port_no]['rx_taxa'], 
                    stat.tx_errors, stat.rx_errors, stat.tx_packets, stat.rx_packets, stat.tx_dropped, stat.rx_dropped, stat.rx_frame_err, stat.rx_over_err, stat.rx_crc_err, stat.collisions)

