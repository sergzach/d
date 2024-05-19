# The Goal

To debug python processes changing function/method bodies without stopping an executing python process, so, to save your time because of possibly long operations of starting web server (and so on), **not calling previous functions to reach the current debugging line.**


# Usage

Create a user module with copy of function bodies to debug.


```
# d_example.py
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
```

Add `d.init(...)` call in your module where you want to debug.

```
# example.py
import d
import d_example
...
# Objects we want to debug.
class TestClass:
    def member(self):
        print('In member function.')

    def foo(self, k):
        print(k)
        print(f'Replace the function in TestClass with {bold("d.")}')


def foo2(k):
    print(k)
    print(f'Replace the global function with {bold("d.")}')
...
def main():
    d.init(
        patching_module=sys.modules[__name__],
        user_patch_module=d_example,
        ask_repeat=True
    )
    ...
```

# Addiotional

Possibly you can debug several modules simultaneously. Then define several `d_files.py` passing debugging modules (as for the one module in the example above).

Debug in {paired to example.py} d_example.py -- the copy of function/methods in a repeating loop. Now you can change the function/method bodies in d_example.py without stopping a python process.

Also you can stop on breakpoint in d_example.py in your IDE.
