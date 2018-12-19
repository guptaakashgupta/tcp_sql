def filter_rows(rows, filter_criteria):
    is_int = False
    try:
        int(filter_criteria[2])
        is_int = True
    except Exception as e:
        filter_criteria[2] = filter_criteria[2].strip('\"\'')


    if '<=' in filter_criteria and is_int:
        # filters = filter_criteria.split('<=')
        filters = filter_criteria
        # if len(filters)==2:
        return apply_less_than_equal_operator(rows, filters[0], int(filters[2]))

    if '<' in filter_criteria and is_int:
        # filters = filter_criteria.split('<')
        filters = filter_criteria
        # if len(filters) == 2:
        return apply_less_than_operator(rows, filters[0], int(filters[2]))

    if '>=' in filter_criteria and is_int:
        # filters = filter_criteria.split('>=')
        filters = filter_criteria
        # if len(filters) == 2:
        return apply_greater_than_equal_operator(rows, filters[0], int(filters[2]))

    if '>' in filter_criteria and is_int:
        # filters = filter_criteria.split('>')
        filters = filter_criteria
        # if len(filters) == 2:
        return apply_greater_than_operator(rows, filters[0], int(filters[2]))

    if '!=' in filter_criteria:
        # filters = filter_criteria.split('!=')
        filters = filter_criteria
        # if len(filters) == 2:
        return apply_not_equal_operator(rows, filters[0], filters[2])

    if '=' in filter_criteria:
        # filters = filter_criteria.split('=')
        filters = filter_criteria
        # if len(filters) == 2:
        return apply_equal_operator(rows, filters[0], filters[2])
    
    raise Exception('Invalid Where Clause operator and operand types\n')


def apply_less_than_operator(rows, column_name, compare_value):
    filtered_data = []
    for row in rows:
        if int(row[column_name]) < compare_value:
            filtered_data.append(row)

    return filtered_data

def apply_less_than_equal_operator(rows, column_name, compare_value):
    filtered_data = []
    for row in rows:
        if int(row[column_name]) <= compare_value:
            filtered_data.append(row)

    return filtered_data

def apply_greater_than_operator(rows, column_name, compare_value):
    filtered_data = []
    for row in rows:
        if int(row[column_name]) > compare_value:
            filtered_data.append(row)

    return filtered_data

def apply_greater_than_equal_operator(rows, column_name, compare_value):
    filtered_data = []
    for row in rows:
        if int(row[column_name]) >= compare_value:
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
        if not (row[column_name] == compare_value):
            filtered_data.append(row)

    return filtered_data