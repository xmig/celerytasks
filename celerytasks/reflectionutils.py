"""
Copy tretiak@gmail.com / https://github.com/xmig
Any restriction for using
"""
import inspect
import os.path


def class_by_name(class_name):
    """ Load Class by a name
    @see http://stackoverflow.com/questions/547829/how-to-dynamically-load-a-python-class
    :param class_name: <str> Full class name. I.e "app.package.module.classname'
    :return: <cls> Loaded Class
    """

    idx = class_name.rfind(".")
    name = class_name[idx+1:len(class_name)]
    m = __import__(class_name[0:idx], globals(), locals(), [name])
    return getattr(m, name)


class INVOKED_DEPT:
    """Enum.
    Just for more understandable using 'function_name' function
    """
    CURRENT = 1
    PREVIOUS = 2
    BEFORE_PREVIOUS = 3


class INVOKED_PARAMETER:
    FUNCTION_NAME = 3
    MODULE_PATH = 1
    LINE_NUM = 2
    INVOKED_CODE = 4

_NAME_CANNOT_BE_DEFINED = "__NotDefined__"


def function_name(dept=INVOKED_DEPT.CURRENT):
    """Returns name of invoked function.
    :param dept: invoke dept. for 'this' particular function == 0
    """
    return _invoked(INVOKED_PARAMETER.FUNCTION_NAME, dept)


def function_name_tuple(dept=INVOKED_DEPT.CURRENT):
    try:
        stack = inspect.stack()[dept]
        fun = stack[INVOKED_PARAMETER.FUNCTION_NAME]
        mod = stack[INVOKED_PARAMETER.MODULE_PATH]
        mod_name = os.path.splitext(os.path.basename(mod))[0]

        return (fun, mod_name,)
    except:
        return (None, None,)


def line_num(dept=INVOKED_DEPT.CURRENT):
    """Returns line number a function was invoked.
    :param dept: invoke dept. for 'this' particular function == 0
    """
    return _invoked(INVOKED_PARAMETER.LINE_NUM, dept)


def module_path(dept=INVOKED_DEPT.CURRENT):
    """Returns module path for a function was invoked.
    :param dept: invoke dept. for 'this' particular function == 0
    """
    return _invoked(INVOKED_PARAMETER.MODULE_PATH, dept)


def _invoked(index, dept=INVOKED_DEPT.CURRENT):
    """Returns index element of invoked stack.
    :param dept: invoke dept. for 'this' particular function == 0\

    print inspect.stack()[1] >>
    (<frame object at 0x3e23d0>, '/Users/app/test/views.py', 48, 'do_something', ['    return function_name()\n'], 0)

    """
    try:
        return inspect.stack()[dept][index]
    except:
        return _NAME_CANNOT_BE_DEFINED


