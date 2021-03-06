import os
import signal
import time
import unittest
import xml

import stomp
from stomp import exception

from testutils import *


class TransformationListener(ConnectionListener):
    def __init__(self):
        self.message = None
    
    def on_before_message(self, headers, body):
        if 'transformation' in headers:
            trans_type = headers['transformation']
            if trans_type != 'jms-map-xml':
                return body

            try:
                entries = {}
                doc = xml.dom.minidom.parseString(body)
                rootElem = doc.documentElement
                for entryElem in rootElem.getElementsByTagName("entry"):
                    pair = []
                    for node in entryElem.childNodes:
                        if not isinstance(node, xml.dom.minidom.Element): continue
                        pair.append(node.firstChild.nodeValue)
                    assert len(pair) == 2
                    entries[pair[0]] = pair[1]
                return (headers, entries)
            except Exception:
                #
                # unable to parse message. return original
                #
                return (headers, body)
                
    def on_message(self, headers, body):
        self.message = body
                    

class TestMessageTransform(unittest.TestCase):

    def setUp(self):
        conn = stomp.Connection(get_standard_host())
        listener = TransformationListener()
        conn.set_listener('', listener)
        conn.start()
        conn.connect('admin', 'password', wait=True)
        self.conn = conn
        self.listener = listener
        
    def tearDown(self):
        if self.conn:
            self.conn.disconnect()
       
    def testbasic(self):
        self.conn.subscribe(destination='/queue/test', id=1, ack='auto')

        self.conn.send(body='''<map>
    <entry>
        <string>name</string>
        <string>Dejan</string>
    </entry>
    <entry>
        <string>city</string>
        <string>Belgrade</string>
    </entry>
</map>''', destination='/queue/test', headers={'transformation':'jms-map-xml'})

        time.sleep(2)
        
        self.assert_(self.listener.message.__class__ == dict, 'Message type should be dict after transformation')
        self.assert_(self.listener.message['name'] == 'Dejan', 'Missing an expected dict element')
        self.assert_(self.listener.message['city'] == 'Belgrade', 'Missing an expected dict element')
