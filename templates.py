
import sys

import d


def bold(substring):
    return f'\033[1m{substring}\033[0m'


class TestClass:
    def foo(self, k):
        print(k)
        print(f'Replace the function in TestClass with {bold("d.")}')


def foo(k):
    print(k)
    print(f'Replace the global function with {bold("d.")}')


def main():
    d.init(sys.modules[__name__])

    test_class = TestClass()
    test_class.foo(25)
    #foo(26)


if __name__ == '__main__':
    main()
