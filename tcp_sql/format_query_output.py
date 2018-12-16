def format_query_result(rows):
    ans = ''
    ans += ' '.join(rows[0].keys()) + '\n'

    for row in rows:
        ans += ' '.join(row.values()) + '\n'
    return ans