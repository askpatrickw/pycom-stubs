"""
Module: 'network' on GPy v1.11
"""
# MCU: (sysname='GPy', nodename='GPy', release='1.20.2.rc6', version='v1.11-01f49f7 on 2020-02-28', machine='GPy with ESP32', pybytes='1.3.1')
# Stubber: 1.3.2

class Bluetooth:
    ''
    ADV_128SERVICE_DATA = 33
    ADV_128SRV_CMPL = 7
    ADV_128SRV_PART = 6
    ADV_16SRV_PART = 2
    ADV_32SERVICE_DATA = 32
    ADV_32SRV_CMPL = 5
    ADV_32SRV_PART = 4
    ADV_ADV_INT = 26
    ADV_APPEARANCE = 25
    ADV_BLE_ADDR_TYPE_PUBLIC = 0
    ADV_BLE_ADDR_TYPE_RANDOM = 1
    ADV_BLE_ADDR_TYPE_RPA_PUBLIC = 2
    ADV_BLE_ADDR_TYPE_RPA_RANDOM = 3
    ADV_CHNL_37 = 1
    ADV_CHNL_38 = 2
    ADV_CHNL_39 = 4
    ADV_CHNL_ALL = 7
    ADV_DEV_CLASS = 13
    ADV_FILTER_ALLOW_SCAN_ANY_CON_ANY = 0
    ADV_FILTER_ALLOW_SCAN_ANY_CON_WLST = 2
    ADV_FILTER_ALLOW_SCAN_WLST_CON_ANY = 1
    ADV_FILTER_ALLOW_SCAN_WLST_CON_WLST = 3
    ADV_FLAG = 1
    ADV_MANUFACTURER_DATA = 255
    ADV_NAME_CMPL = 9
    ADV_NAME_SHORT = 8
    ADV_SERVICE_DATA = 22
    ADV_T16SRV_CMPL = 3
    ADV_TX_PWR = 10
    ADV_TYPE_DIRECT_IND_HIGH = 1
    ADV_TYPE_DIRECT_IND_LOW = 4
    ADV_TYPE_IND = 0
    ADV_TYPE_NONCONN_IND = 3
    ADV_TYPE_SCAN_IND = 2
    CHAR_CONFIG_INDICATE = 2
    CHAR_CONFIG_NOTIFY = 1
    CHAR_NOTIFY_EVENT = 32
    CHAR_READ_EVENT = 8
    CHAR_SUBSCRIBE_EVENT = 128
    CHAR_WRITE_EVENT = 16
    CLIENT_CONNECTED = 2
    CLIENT_DISCONNECTED = 4
    CONN_ADV = 0
    CONN_DIR_ADV = 1
    DISC_ADV = 2
    EXT_ANT = 1
    INT_ANT = 0
    NEW_ADV_EVENT = 1
    NON_CONN_ADV = 3
    PERM_READ = 1
    PERM_READ_ENCRYPTED = 2
    PERM_READ_ENC_MITM = 4
    PERM_WRITE = 16
    PERM_WRITE_ENCRYPTED = 32
    PERM_WRITE_ENC_MITM = 64
    PERM_WRITE_SIGNED = 128
    PERM_WRITE_SIGNED_MITM = 256
    PROP_AUTH = 64
    PROP_BROADCAST = 1
    PROP_EXT_PROP = 128
    PROP_INDICATE = 32
    PROP_NOTIFY = 16
    PROP_READ = 2
    PROP_WRITE = 8
    PROP_WRITE_NR = 4
    PUBLIC_ADDR = 0
    PUBLIC_RPA_ADDR = 2
    RANDOM_ADDR = 1
    RANDOM_RPA_ADDR = 3
    SCAN_RSP = 4
    TX_PWR_0 = 4
    TX_PWR_ADV = 9
    TX_PWR_CONN = 0
    TX_PWR_DEFAULT = 11
    TX_PWR_N12 = 0
    TX_PWR_N3 = 3
    TX_PWR_N6 = 2
    TX_PWR_N9 = 1
    TX_PWR_P3 = 5
    TX_PWR_P6 = 6
    TX_PWR_P9 = 7
    TX_PWR_SCAN = 10
    def advertise():
        pass

    def callback():
        pass

    def connect():
        pass

    def deinit():
        pass

    def disconnect_client():
        pass

    def events():
        pass

    def gatts_mtu():
        pass

    def get_adv():
        pass

    def get_advertisements():
        pass

    def init():
        pass

    def isscanning():
        pass

    def modem_sleep():
        pass

    def nvram_erase():
        pass

    def resolve_adv_data():
        pass

    def service():
        pass

    def set_advertisement():
        pass

    def set_advertisement_params():
        pass

    def set_advertisement_raw():
        pass

    def set_pin():
        pass

    def start_scan():
        pass

    def stop_scan():
        pass

    timeout = None
    def tx_power():
        pass

Coap = None

class LTE:
    ''
    EVENT_COVERAGE_LOSS = 1
    IP = 'IP'
    IPV4V6 = 'IPV4V6'
    def attach():
        pass

    def connect():
        pass

    def deinit():
        pass

    def detach():
        pass

    def dettach():
        pass

    def disconnect():
        pass

    def events():
        pass

    def factory_reset():
        pass

    def iccid():
        pass

    def imei():
        pass

    def init():
        pass

    def isattached():
        pass

    def isconnected():
        pass

    def lte_callback():
        pass

    def modem_upgrade_mode():
        pass

    def pppresume():
        pass

    def pppsuspend():
        pass

    def reconnect_uart():
        pass

    def reset():
        pass

    def send_at_cmd():
        pass

    def time():
        pass

    def ue_coverage():
        pass

MDNS = None

class Server:
    ''
    def deinit():
        pass

    def init():
        pass

    def isrunning():
        pass

    def timeout():
        pass


class WLAN:
    ''
    AP = 2
    COUNTRY_POL_AUTO = 0
    COUNTRY_POL_MAN = 1
    def Connected_ap_pwd():
        pass

    EVENT_PKT_ANY = 63
    EVENT_PKT_CTRL = 2
    EVENT_PKT_DATA = 4
    EVENT_PKT_DATA_AMPDU = 32
    EVENT_PKT_DATA_MPDU = 16
    EVENT_PKT_MGMT = 1
    EVENT_PKT_MISC = 8
    EXT_ANT = 1
    FILTER_CTRL_PKT_ACK = 536870912
    FILTER_CTRL_PKT_ALL = -8388608
    FILTER_CTRL_PKT_BA = 33554432
    FILTER_CTRL_PKT_BAR = 16777216
    FILTER_CTRL_PKT_CFEND = -1073741824
    FILTER_CTRL_PKT_CFENDACK = 0
    FILTER_CTRL_PKT_CTS = 268435456
    FILTER_CTRL_PKT_PSPOLL = 67108864
    FILTER_CTRL_PKT_WRAPPER = 8388608
    HT20 = 1
    HT40 = 2
    INT_ANT = 0
    PHY_11_B = 1
    PHY_11_G = 2
    PHY_11_N = 3
    PHY_LOW_RATE = 4
    SCAN_ACTIVE = 0
    SCAN_PASSIVE = 1
    SECONDARY_CHN_ABOVE = 1
    SECONDARY_CHN_BELOW = 2
    SECONDARY_CHN_NONE = 0
    SMART_CONF_DONE = 64
    SMART_CONF_TIMEOUT = 128
    STA = 1
    STA_AP = 3
    WEP = 1
    WPA = 2
    WPA2 = 3
    WPA2_ENT = 5
    def antenna():
        pass

    def ap_sta_list():
        pass

    def auth():
        pass

    def bandwidth():
        pass

    def bssid():
        pass

    def callback():
        pass

    def channel():
        pass

    def connect():
        pass

    def country():
        pass

    def ctrl_pkt_filter():
        pass

    def deinit():
        pass

    def disconnect():
        pass

    def events():
        pass

    def hostname():
        pass

    def ifconfig():
        pass

    def init():
        pass

    def isconnected():
        pass

    def joined_ap_info():
        pass

    def mac():
        pass

    def max_tx_power():
        pass

    def mode():
        pass

    def promiscuous():
        pass

    def scan():
        pass

    def send_raw():
        pass

    def smartConfig():
        pass

    def ssid():
        pass

    def wifi_packet():
        pass

    def wifi_protocol():
        pass

