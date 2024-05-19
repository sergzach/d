import sys

from d import patch_cls


# CUSTOM PATCHERS:
def user_patch(patching_module):
    patch_cls(
        patching_module=patching_module,
        user_patching_module=sys.modules[__name__],
        class_name='TestClass',
        method_name='foo'
    )


# ON_EXCEPTION:
def on_exception(e):
    print('Exception, see in IDE!')


# DEBUGGING_FUNCTIONS:
def foo(self, k):
    self.member()
    self.member()
    # raise Exception('Shit happens!')
    print('The new version of k 246.')
