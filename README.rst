=======
tcp_sql
=======


.. image:: https://img.shields.io/pypi/v/tcp_sql.svg
        :target: https://pypi.python.org/pypi/tcp_sql

.. image:: https://img.shields.io/travis/guptaakashgupta/tcp_sql.svg
        :target: https://travis-ci.org/guptaakashgupta/tcp_sql

.. image:: https://readthedocs.org/projects/tcp-sql/badge/?version=latest
        :target: https://tcp-sql.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




TCP server that takes SQL like statements, finds rows from a fixed CSV file that match the query, and prints the results


* Free software: GNU General Public License v3
* Documentation: https://tcp-sql.readthedocs.io.


Features
--------

* Returns query outputs from a TCP server
* Support * in the select query
* Support different fields in the where clause
* Support multiple fields in the select query (not just name,id)

Expected Program Run
--------

* telnet 127.0.0.1 9999
> select name, id from actors where age<=21;
