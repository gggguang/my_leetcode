s = "[([]])"


def isValid(s: str) -> bool:
    op = ["(", "[", "{"]
    cl = [")", "]", "}"]
    con = []
    for char in s:
        if char in cl and cl.index(char) not in con:
            return False

        elif char in op:
            con.append(op.index(char))

        elif char in cl and cl.index(char) == con[-1]:
            # con.remove(cl.index(char))
            con.pop()
        print(con)

    return True if len(con) == 0 else False


aa = isValid(s)
print(aa)

"""
    if char in cl:
        if cl.index(char) in con:
            con.remove(cl.index(char))
    print(con)
"""

