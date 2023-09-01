from p2pool.bitcoin import networks

PARENT = networks.nets['digibyte']
SHARE_PERIOD = 25
CHAIN_LENGTH = 24*60*60//10
REAL_CHAIN_LENGTH = 24*60*60//10
TARGET_LOOKBEHIND = 200
SPREAD = 30
IDENTIFIER = '1bfe01eff5ba4e38'.decode('hex')
PREFIX = '1bfe01eff652e4b7'.decode('hex')
P2P_PORT = 5024
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 5025
BOOTSTRAP_ADDRS = [
        'triplezen.org',
        'zen-solo.com',
        ]
ANNOUNCE_CHANNEL = '#p2pool'
VERSION_CHECK = lambda v: None if 82200 <= v else 'DigiByte version too old. Upgrade to 7.17.2 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['csv', 'segwit', 'odo', 'testdummy'])
MINIMUM_PROTOCOL_VERSION = 1600
NEW_MINIMUM_PROTOCOL_VERSION = 1700
SEGWIT_ACTIVATION_VERSION = 17
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
