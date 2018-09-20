from pprint import pprint
from db import *


STATS = {}

def extract(datapath, stat, INTERVALO):

    ALPHA = 0.2

    STATS[datapath] = STATS.get(datapath, {})

    STATS[datapath][stat.port_no] = STATS[datapath].get(stat.port_no, {
        'primeira_vez': True,
        'rx_bytes_ant': 0,
        'tx_bytes_ant': 0,

        'rx_media': 0,
        'tx_media': 0,
    })

    if STATS[datapath][stat.port_no]['primeira_vez']:
        STATS[datapath][stat.port_no]['primeira_vez'] = False

        STATS[datapath][stat.port_no]['rx_bytes_ant'] = stat.rx_bytes
        STATS[datapath][stat.port_no]['rx_media'] = stat.rx_bytes

        STATS[datapath][stat.port_no]['tx_bytes_ant'] = stat.tx_bytes
        STATS[datapath][stat.port_no]['tx_media'] = stat.tx_bytes

    else:
        rx_taxa = (stat.rx_bytes - STATS[datapath][stat.port_no]['rx_bytes_ant']) / INTERVALO
        STATS[datapath][stat.port_no]['rx_taxa'] = rx_taxa
        STATS[datapath][stat.port_no]['rx_bytes_ant'] = stat.rx_bytes

        STATS[datapath][stat.port_no]['rx_media'] = ((ALPHA) * rx_taxa + (1-ALPHA) * STATS[datapath][stat.port_no]['rx_media'])

        tx_taxa = (stat.tx_bytes - STATS[datapath][stat.port_no]['tx_bytes_ant']) / INTERVALO
        STATS[datapath][stat.port_no]['tx_taxa'] = tx_taxa
        STATS[datapath][stat.port_no]['tx_bytes_ant'] = stat.tx_bytes

        STATS[datapath][stat.port_no]['tx_media'] = ((ALPHA) * tx_taxa + (1-ALPHA) * STATS[datapath][stat.port_no]['tx_media'])

        #pprint(STATS)

        manda_pro_banco(datapath, stat.port_no, stat.duration_sec, stat.duration_nsec,
                        stat.tx_bytes,
                        STATS[datapath][stat.port_no]['tx_taxa'],
                        STATS[datapath][stat.port_no]['rx_media'],
                        stat.rx_bytes,
                        STATS[datapath][stat.port_no]['rx_taxa'],
                        STATS[datapath][stat.port_no]['tx_media'],
                        stat.tx_errors, stat.rx_errors)
