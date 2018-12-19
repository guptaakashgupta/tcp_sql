from pyparsing import CaselessKeyword, delimitedList, Each, Forward, Group, Optional, Word, alphas,alphanums, nums, oneOf, ZeroOrMore, quotedString

keywords = ["select", "from", "where", "group by", "order by", "and", "or"]

[select, _from, where, groupby, orderby, _and, _or] = [ CaselessKeyword(word) for word in keywords ]

table = column = Word(alphanums)
columns = Group(delimitedList(column))
s_int = Word(nums    )
# columnVal = s_int | quotedString
ident = Word(alphanums)
columnVal = s_int | ident | quotedString

whereCond = (column + oneOf("= != < > >= <=") + columnVal)

# whereExpr = whereCond + ZeroOrMore((_and | _or) + whereCond)
whereExpr = whereCond
selectStmt = Forward().setName("select statement")

selectStmt << (select + ('*' | columns).setResultsName("columns") + _from + table.setResultsName("table") + Optional(where + Group(whereExpr), '').setResultsName("where").setDebug(False) + Each([Optional(groupby + columns("groupby"),'').setDebug(False), Optional(orderby + columns("orderby"),'').setDebug(False)]))

def parse_input_query(query):
    parsed_query = selectStmt.parseString(query)
    return [parsed_query.table, parsed_query.columns.asList(), parsed_query.where.asList()[1] if parsed_query.where.asList()[0] else []]

if __name__ == "__main__":
    print(parse_input_query('SELECT id, username, email FROM users WHERE username = "johnabc"'))
    print(parse_input_query('SELECT id, username, email FROM users WHERE age > 24'))
    print(parse_input_query('SELECT id, username, email FROM users'))
    
    
