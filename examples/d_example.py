import sys

from d import patch_cls, patch_fn


# CUSTOM PATCHERS:
def user_patch(patching_module):
    patch_cls(
        patching_module=patching_module,
        user_patching_module=sys.modules[__name__],
        class_name='TestClass',
        method_name='foo'
    )

    patch_fn(
        patching_module=patching_module,
        user_patching_module=sys.modules[__name__],
        function_name='foo2'
    )


# ON_EXCEPTION:
def on_exception(e):
    print('Exception, see in IDE!')


# DEBUGGING_FUNCTIONS:
def foo(self, k):
    self.member()
    self.member()
    # raise Exception('Shit happens!')
    print('The new version of k 257.')


def foo2(k):
    print('foo2 has been patched!')
    print('Yeah!')
