from transport import *
from protocol import *


class StompConnection10(Transport, Protocol10):
    def __init__(self, 
                 host_and_ports = [ ('localhost', 61613) ], 
                 prefer_localhost = True,
                 try_loopback_connect = True,
                 reconnect_sleep_initial = 0.1,
                 reconnect_sleep_increase = 0.5,
                 reconnect_sleep_jitter = 0.1,
                 reconnect_sleep_max = 60.0,
                 reconnect_attempts_max = 3,
                 use_ssl = False,
                 ssl_key_file = None,
                 ssl_cert_file = None,
                 ssl_ca_certs = None,
                 ssl_cert_validator = None,
                 wait_on_receipt = False,
                 ssl_version = DEFAULT_SSL_VERSION,
                 timeout = None,
                 keepalive = None):
        Transport.__init__(self, host_and_ports, prefer_localhost, try_loopback_connect, 
            reconnect_sleep_initial, reconnect_sleep_increase, reconnect_sleep_jitter, reconnect_sleep_max, reconnect_attempts_max,
            use_ssl, ssl_key_file, ssl_cert_file, ssl_ca_certs, ssl_cert_validator, wait_on_receipt, ssl_version, timeout, keepalive, None)
        Protocol10.__init__(self, self)
        
    def disconnect(self, receipt = None, headers = {}, **keyword_headers):
        Protocol10.disconnect(self, receipt, headers, **keyword_headers)
        Transport.stop(self)


class StompConnection11(Transport, Protocol11):
    def __init__(self, 
                 host_and_ports = [ ('localhost', 61613) ], 
                 prefer_localhost = True,
                 try_loopback_connect = True,
                 reconnect_sleep_initial = 0.1,
                 reconnect_sleep_increase = 0.5,
                 reconnect_sleep_jitter = 0.1,
                 reconnect_sleep_max = 60.0,
                 reconnect_attempts_max = 3,
                 use_ssl = False,
                 ssl_key_file = None,
                 ssl_cert_file = None,
                 ssl_ca_certs = None,
                 ssl_cert_validator = None,
                 wait_on_receipt = False,
                 ssl_version = DEFAULT_SSL_VERSION,
                 timeout = None,
                 heartbeats = (0, 0),
                 keepalive = None,
                 vhost = None):
        Transport.__init__(self, host_and_ports, prefer_localhost, try_loopback_connect, 
            reconnect_sleep_initial, reconnect_sleep_increase, reconnect_sleep_jitter, reconnect_sleep_max, reconnect_attempts_max,
            use_ssl, ssl_key_file, ssl_cert_file, ssl_ca_certs, ssl_cert_validator, wait_on_receipt, ssl_version, timeout,
            keepalive, vhost)
        Protocol11.__init__(self, self, heartbeats)
        
    def disconnect(self, receipt = None, headers = {}, **keyword_headers):
        Protocol11.disconnect(self, receipt, headers, **keyword_headers)
        Transport.stop(self)


class StompConnection12(Transport, Protocol12):
    def __init__(self, 
                 host_and_ports = [ ('localhost', 61613) ], 
                 prefer_localhost = True,
                 try_loopback_connect = True,
                 reconnect_sleep_initial = 0.1,
                 reconnect_sleep_increase = 0.5,
                 reconnect_sleep_jitter = 0.1,
                 reconnect_sleep_max = 60.0,
                 reconnect_attempts_max = 3,
                 use_ssl = False,
                 ssl_key_file = None,
                 ssl_cert_file = None,
                 ssl_ca_certs = None,
                 ssl_cert_validator = None,
                 wait_on_receipt = False,
                 ssl_version = DEFAULT_SSL_VERSION,
                 timeout = None,
                 heartbeats = (0, 0),
                 keepalive = None,
                 vhost = None):
        Transport.__init__(self, host_and_ports, prefer_localhost, try_loopback_connect, 
            reconnect_sleep_initial, reconnect_sleep_increase, reconnect_sleep_jitter, reconnect_sleep_max, reconnect_attempts_max,
            use_ssl, ssl_key_file, ssl_cert_file, ssl_ca_certs, ssl_cert_validator, wait_on_receipt, ssl_version, timeout,
            keepalive, vhost)
        Protocol12.__init__(self, self, heartbeats)

    def disconnect(self):
        Protocol12.disconnect(self)
        Transport.stop(self)