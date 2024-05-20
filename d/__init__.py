import importlib


def reload(module):
    '''
    Use the function to reload a current mod.
    '''
    importlib.reload(module)


def patch_cls(
        *,
        patching_module,
        user_patching_module,
        class_name,
        method_name
):
    def create_debug_patched():
        def inner(*args, **kwargs):
            while True:
                try:
                    getattr(user_patching_module, 'user_patch')(patching_module)
                    getattr(user_patching_module, f'{method_name}')(*args, **kwargs)
                except Exception as e:
                    getattr(user_patching_module, 'on_exception')(e)
                finally:
                    if init.ask_repeat:
                        ans = input('Do repeat (y/any for no)? ')
                        if ans != 'y':
                            print(f'Debugging of {method_name} is finished.')
                            break
        return inner

    reload(user_patching_module)

    cls_ = getattr(patching_module, class_name)

    setattr(
        cls_,
        method_name,
        create_debug_patched()
    )


def patch_fn(
        *,
        patching_module,
        user_patching_module,
        function_name
):
    def create_debug_patched():
        def inner(*args, **kwargs):
            while True:
                try:
                    getattr(user_patching_module, 'user_patch')(patching_module)
                    getattr(user_patching_module, f'{function_name}')(*args, **kwargs)
                except Exception as e:
                    getattr(user_patching_module, 'on_exception')(e)
                finally:
                    if init.ask_repeat:
                        ans = input('Do repeat (y/any for no)? ')
                        if ans != 'y':
                            print(f'Debugging of {function_name} is finished.')
                            break
        return inner

    reload(user_patching_module)

    setattr(
        patching_module,
        function_name,
        create_debug_patched()
    )


def init(*, patching_module, user_patch_module, ask_repeat=True):
    init.ask_repeat = ask_repeat
    reload(user_patch_module)
    getattr(user_patch_module, 'user_patch')(patching_module)
