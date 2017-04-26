#!python
# coding: utf-8
import sys
import os

import ctypes
import enum

'''
def command(argv=None, debug=False):
    shell32 = ctypes.windll.shell32
    if argv is None and shell32.IsUserAnAdmin():
        return True
    if argv is None:
        argv = sys.argv
    if hasattr(sys, '_MEIPASS'):
        arguments = map(unicode, argv[1:])
    else:
        arguments = map(unicode, argv)
    argument_line = u''.join(arguments)
    executable = unicode("cmd.exe")
    if debug:
        print 'Command line: ', executable, argument_line
    ret = shell32.ShellExecuteW(None, u"runas", executable, "/k " + argument_line, None, 1)
    if int(ret) <= 32:
        return False
    return None


if __name__ == '__main__':
    ret = command()
    if ret is True:
        print 'I have admin privilege.'
        raw_input('Press ENTER to exit.')
    elif ret is None:
        print 'I am elevating to admin privilege.'
        raw_input('Press ENTER to exit.')
    else:
        print 'Error(ret=%d): cannot elevate privilege.' % (ret, )

'''

class SW(enum.IntEnum):

    HIDE = 0
    MAXIMIZE = 3
    MINIMIZE = 6
    RESTORE = 9
    SHOW = 5
    SHOWDEFAULT = 10
    SHOWMAXIMIZED = 3
    SHOWMINIMIZED = 2
    SHOWMINNOACTIVE = 7
    SHOWNA = 8
    SHOWNOACTIVATE = 4
    SHOWNORMAL = 1


class ERROR(enum.IntEnum):

    ZERO = 0
    FILE_NOT_FOUND = 2
    PATH_NOT_FOUND = 3
    BAD_FORMAT = 11
    ACCESS_DENIED = 5
    ASSOC_INCOMPLETE = 27
    DDE_BUSY = 30
    DDE_FAIL = 29
    DDE_TIMEOUT = 28
    DLL_NOT_FOUND = 32
    NO_ASSOC = 31
    OOM = 8
    SHARE = 26

class Admin(object):
    def __init__(self):
        return 

    def bootstrap(self, script_path):
        # Get current working directory

        argument_line = "/k python " + script_path
        argument_line = u''.join(argument_line)
        print argument_line

        hinstance = ctypes.windll.shell32.ShellExecuteW(
            None, 
            u'runas', 
            unicode("cmd.exe"), 
            argument_line, 
            None, 
            SW.SHOWNORMAL
        )
        if hinstance <= 32:
            raise RuntimeError(ERROR(hinstance))
