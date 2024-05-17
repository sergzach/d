import importlib
import sys


def get_cur_module():
    return sys.modules[__name__]


def reload():
    '''
    Use the function to reload a current mod.
    '''
    importlib.reload(get_cur_module())


def patch_func(func_name):
    def create_debug_func(debug_func):
        def inner(*args, **kwargs):
            import pdb; pdb.set_trace()
            while True:
                try:
                    return debug_func(*args, **kwargs)
                except Exception as e:
                    print('Error, probably repatch.')
                    import pdb; pdb.set_trace()
                finally:
                    ans = input('Repeat (y/n)?')
                    if ans == 'n':
                        break
        return inner

    reload()
    globals()[func_name] = create_debug_func(
        get_cur_module()[func_name]
    )


def patch_cls(class_, method_name):
    def create_debug_patched_method(debug_method):
        def inner(*args, **kwargs):
            import pdb; pdb.set_trace()
            while True:
                try:
                    return debug_method(*args, **kwargs)
                except Exception as e:
                    print('Error, probably repatch.')
                    import pdb; pdb.set_trace()
                finally:
                    ans = input('Repeat (y/n)?')
                    if ans == 'n':
                        break
        return inner

    reload()
    class_.__dict__[method_name] = create_debug_patched_method(
        get_cur_module()[method_name]
    )


def print_file(filename):
    with open(filename, 'rb') as f:
        return f.read()


### Place here your patching functions and use patch_func() or patch_cls().
