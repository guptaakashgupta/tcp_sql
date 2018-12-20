def format_query_result(rows):
    ans = ''
    if len(rows)>0:
        ans += ' '.join(rows[0].keys()) + '\n'

        for row in rows:
            ans += ' '.join(row.values()) + '\n'
    return ans if ans else 'Empty Set \n'