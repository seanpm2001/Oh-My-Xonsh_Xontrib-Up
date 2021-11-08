def _upp(args):
    """Get the path of an ancestor directory"""
    if not args or len(args) < 1:
        args = [1]
    balloons = ('../' * int(args[0]))
    return pf"{$PWD}/{balloons}".resolve()
aliases['upp'] = _upp
