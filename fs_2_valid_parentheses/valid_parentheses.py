def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    parens = list(parens)
    if parens.count("(") == parens.count(")") or parens[0]==")" or parens[-1]=="(":
        return False
    for char in parens:
        if len(parens)==0:
            return True
        if char == "(":
            if parens.index(")") != -1:
                parens.pop(parens.index("("))
                parens.pop(parens.index(")"))
            if parens.index(")") == -1:
                return False