# -*- coding: utf-8 -*-

import logging
import SocketServer
from pyparsing import ParseException

from tcp_sql import get_query_results, get_final_query_results
from parse_sql import parse_input_query

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
        self.data = None
        while self.data != 'exit':
            self.data = self.request.recv(1024).strip().lower()
            print("{} sent:".format(self.client_address[0]))
            print(self.data)
            if self.data != 'exit':
                try:
                    list_data = parse_input_query(self.data)
                    # print(list)
                    if 'where' in self.data and not list_data[2]:
                        raise Exception('Incomplete where clause\n')
                    query_result = get_final_query_results(list_data)
                    # query_result = get_query_results(self.data)
                except ParseException as e:
                    query_result = str(e)+'\n'
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
