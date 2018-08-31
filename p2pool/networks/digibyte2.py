from p2pool.bitcoin import networks

PARENT=networks.nets['digibyte2']
SHARE_PERIOD = 25
CHAIN_LENGTH = 24*60*60//10
REAL_CHAIN_LENGTH = 24*60*60//10
TARGET_LOOKBEHIND = 200
SPREAD = 30
IDENTIFIER = '48242A6E7BF4DFEB'.decode('hex')
PREFIX = '48242A6E405A15EB'.decode('hex')
P2P_PORT = 5024
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 5055
BOOTSTRAP_ADDRS = 'dgbsolo.brutang.work pocketburgers.ddnsfree.com 204.93.127.197 triplezen.tk'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool'
VERSION_CHECK = lambda v: None if 6160400 <= v else 'DigiByte version too old. Upgrade to 6.16.4 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['nversionbips', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 1600
NEW_MINIMUM_PROTOCOL_VERSION = 1700
SEGWIT_ACTIVATION_VERSION = 17
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
