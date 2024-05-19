
import sys

import d
import d_example


def bold(substring):
    return f'\033[1m{substring}\033[0m'


class TestClass:
    def member(self):
        print('In member function.')

    def foo(self, k):
        print(k)
        print(f'Replace the function in TestClass with {bold("d.")}')


def foo2(k):
    print(k)
    print(f'Replace the global function with {bold("d.")}')


def main():
    d.init(
        patching_module=sys.modules[__name__],
        user_patch_module=d_example,
        ask_repeat=True
    )

    test_class = TestClass()
    test_class.foo(25)
    test_class.foo(26)
    foo2(26)


if __name__ == '__main__':
    main()
