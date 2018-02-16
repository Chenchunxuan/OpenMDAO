# using this file to build the docs allows you to attach the debugger to the process.
if __name__ == '__main__':
    import sys
    import sphinx
    import os

    testargs = '-b html -d _build/doctrees . _build/html -t "usr"'.split(' ')
    sys.argv.extend(testargs)

    os.system("make clean")
    sys.exit(sphinx.main())
