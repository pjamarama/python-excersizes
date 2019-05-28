def enforce(*types):
    def decorator(fn):
        def new_func(*args, **kwargs):
            # convert args into mutable thing
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))
            return fn(*newargs, **kwargs)
        return new_func
    return decorator

@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

repeat_msg('Hey!', 4)
