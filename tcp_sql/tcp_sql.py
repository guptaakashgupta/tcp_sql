# -*- coding: utf-8 -*-

"""Main module."""

import csv
import re

import logging

from filter_operations import filter_rows
from format_query_output import format_query_result
logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )

# def get_query_results(data):
#     '''
#         Takes a Sql query string as an input
#         parse the query and return query results from it
#     '''
#     tokens = data.split(';')
#     if(len(tokens) == 2):
#         query = tokens[0].lower().split(' ')
#         # only SELECT * FROM TABLE_NAME and SELECT * FROM TABLE_NAME WHERE Age>40; is supported;
#         if(len(query) == 4 or len(query) == 6):
#             if(query[0] == 'select' and query[2] == 'from' or (len(query) == 6 and query[4] == 'where')):
#                 file_name = query[3] + '.csv'

#                 with open(file_name, 'r') as file:
#                     rows = []
#                     csvreader = csv.DictReader(file)

#                     for row in csvreader:
#                         rows.append(row)

#                     if(len(query)==6):
#                         filter_criteria = query[5]
#                         rows = filter_rows(rows,filter_criteria)
#                     # return select * from Table_name output
#                     if (query[1] == '*'):
#                         return format_query_result(rows)

#                     else:
#                         if rows:
#                             field_list = query[1].split(',')
#                             fields_set = set(field_list)
#                             table_key_set = set(rows[0].keys())
#                             # fields set in input must be a subset table_key_set
#                             if(len(table_key_set&fields_set)==len(fields_set)):
#                                 list_columns_to_remove = list(table_key_set - fields_set)
#                                 for row in rows:
#                                     for column in list_columns_to_remove:
#                                         del row[column]

#                         return format_query_result(rows)

#     raise Exception('Invalid Sql Query\n')


def get_final_query_results(parsed_list):

    file_name = parsed_list[0] + '.csv'

    with open(file_name, 'r') as file:
        rows = []
        csvreader = csv.DictReader(file)

        for row in csvreader:
            rows.append(row)

        if(parsed_list[2]):
            filter_criteria = parsed_list[2]
            rows = filter_rows(rows,filter_criteria)
        # return select * from Table_name output
        if (parsed_list[1] == '*'):
            return format_query_result(rows)

        else:
            if rows:
                field_list = parsed_list[1]
                fields_set = set(field_list)
                table_key_set = set(rows[0].keys())
                # fields set in input must be a subset table_key_set
                if(len(table_key_set&fields_set)==len(fields_set)):
                    list_columns_to_remove = list(table_key_set - fields_set)
                    for row in rows:
                        for column in list_columns_to_remove:
                            del row[column]

            return format_query_result(rows)

