# -*- coding: utf-8 -*-
"""
    config
    ~~~~~~~~~~~~

    Implements the adminstrator privilege excalation.

    :copyright: (c) 2017 by Arun John Kuruvilla.
"""
import sys
import os

import ctypes
import enum

import config

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
        self.config = config.Config()

    def bootstrap(self, script):
        argument_line = "/k python " + script
        argument_line = u''.join(argument_line)

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
