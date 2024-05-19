import importlib
import sys


def get_cur_module():
    return sys.modules[__name__]


def reload():
    '''
    Use the function to reload a current mod.
    '''
    importlib.reload(get_cur_module())


def patch_func(patching_module, func_name):
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
        getattr(get_cur_module(), f'd_{func_name}')
    )


def patch_cls(patching_module, class_name, method_name):
    def create_debug_patched_method(debug_method):
        def inner(*args, **kwargs):
            while True:
                try:
                    user_patch(patching_module)
                    getattr(get_cur_module(), f'd_{method_name}')(*args, **kwargs)
                except Exception as e:
                    print('Exception, see in IDE!')
                    on_exception(e)
                finally:
                    input('Press any key to repeat...')
        return inner

    reload()

    cls_ = getattr(patching_module, class_name)

    setattr(
        cls_,
        method_name,
        create_debug_patched_method(
            getattr(get_cur_module(), f'd_{method_name}')
        )
    )


def print_file(filename):
    with open(filename, 'rb') as f:
        return f.read()

# CHANGEABLE_PART

# CUSTOM PATCHERS:
def user_patch(patching_module):
    patch_cls(patching_module, 'TestClass', 'foo')

# ON_EXCEPTION:
def on_exception(e):
    l = 4

# DEBUGGING_FUNCTIONS:
def d_foo(self, k):
    print('The new version of k 240.')

# ENTRYPOINT
def init(patching_module):
    user_patch(patching_module)
