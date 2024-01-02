# 连入规则等



def connectRule(rule_func):
    def inner(args1, args2):
        return rule_func(args1, args2)
    return inner

