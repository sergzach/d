# TODO
Like Watchman or StatReloader but only for declared currently functions.

At the start - periodically check my own file, in some moment - functions from patching modules may be inavailable, but become available later.

https://github.com/django/django/blob/main/django/utils/autoreload.py

# The Goal

To debug python processes changing function/method bodies without stopping an executing python process, so, to save your time because of possibly long operations of starting web server (and so on), **not calling previous functions to reach the current debugging line.**

# Troubleshooting

**Case 1.** If not all the functions are imported from your <d_example.py> patch module then check for execution errors when importing the <d_example.py> (for example, `ImportError`).

**Case 2.** Decorators (now) may break the patch attempt (try implement defferred/periodical patching?).

Somehow create a copy with a function inner?
```
@pytest.fixture(scope="session", autouse=True)
def fill_hash_models():
    d_fill_hash_models()
```

# Usage

Create a user module with copy of function bodies to debug.

**Not need to have a special callback when method is not defined (when developing with d).** You may just update `user_patch(...)` in your `d_...py` file.


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

Debug in {paired to example.py} d_example.py -- the copy of function/methods in a repeating loop. Now you can change the function/method bodies in d_example.py without stopping a python process.

Also you can stop on breakpoint in d_example.py in your IDE.

# Addiotional

Possibly you can debug several modules simultaneously. Then define several `d_<name_of_debugging_module>.py` passing debugging modules (as for the one module in the example above).
