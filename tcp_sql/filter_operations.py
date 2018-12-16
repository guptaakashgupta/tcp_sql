def filter_rows(rows, filter_criteria):

    if '<=' in filter_criteria:
        filters = filter_criteria.split('<=')
        if len(filters)==2:
            return apply_less_than_equal_operator(rows, filters[0], filters[1])

    if '<' in filter_criteria:
        filters = filter_criteria.split('<')
        if len(filters) == 2:
            return apply_less_than_operator(rows, filters[0], filters[1])

    if '>=' in filter_criteria:
        filters = filter_criteria.split('>=')
        if len(filters) == 2:
            return apply_greater_than_equal_operator(rows, filters[0], filters[1])

    if '>' in filter_criteria:
        filters = filter_criteria.split('>')
        if len(filters) == 2:
            return apply_greater_than_operator(rows, filters[0], filters[1])

    if '!=' in filter_criteria:
        filters = filter_criteria.split('!=')
        if len(filters) == 2:
            return apply_not_equal_operator(rows, filters[0], filters[1])

    if '=' in filter_criteria:
        filters = filter_criteria.split('=')
        if len(filters) == 2:
            return apply_equal_operator(rows, filters[0], filters[1])


def apply_less_than_operator(rows, column_name, compare_value):
    filtered_data = []
    for row in rows:
        if row[column_name] < compare_value:
            filtered_data.append(row)

    return filtered_data

def apply_less_than_equal_operator(rows, column_name, compare_value):
    filtered_data = []
    for row in rows:
        if row[column_name] <= compare_value:
            filtered_data.append(row)

    return filtered_data

def apply_greater_than_operator(rows, column_name, compare_value):
    filtered_data = []
    for row in rows:
        if row[column_name] > compare_value:
            filtered_data.append(row)

    return filtered_data

def apply_greater_than_equal_operator(rows, column_name, compare_value):
    filtered_data = []
    for row in rows:
        if row[column_name] >= compare_value:
            filtered_data.append(row)

    return filtered_data

def apply_equal_operator(rows, column_name, compare_value):
    filtered_data = []
    for row in rows:
        if row[column_name] == compare_value:
            filtered_data.append(row)

    return filtered_data

def apply_not_equal_operator(rows, column_name, compare_value):
    filtered_data = []
    for row in rows:
        if row[column_name] != compare_value:
            filtered_data.append(row)

    return filtered_data