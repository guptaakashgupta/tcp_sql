# -*- coding: utf-8 -*-

import logging
import SocketServer

from tcp_sql import get_query_results

logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )

class TCPServerforSQL(SocketServer.BaseRequestHandler):
    """
    The TCP Server class for SQl queries.

    Handle method to exchange data
    with TCP client.

    """

    def handle(self):
        # self.request - TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} sent:".format(self.client_address[0]))
        print(self.data)
        try:
            query_result = get_query_results(self.data)
        except IOError as e:
            query_result = 'Bad Table Name\n'
        except Exception as e:
            query_result = str(e)
        
        self.request.sendall(query_result)
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Init the TCP server object, bind it to the localhost on 9999 port
    tcp_server = SocketServer.TCPServer((HOST, PORT), TCPServerforSQL)

    # Activate the TCP server.
    # To abort the TCP server, press Ctrl-C.
    tcp_server.serve_forever()
