#!python
# coding: utf-8
import sys
import ctypes

def command(argv=None, debug=True):
    shell32 = ctypes.windll.shell32
    if argv is None and shell32.IsUserAnAdmin():
        return True
    if argv is None:
        argv = sys.argv
    if hasattr(sys, '_MEIPASS'):
        # Support pyinstaller wrapped program.
        arguments = map(unicode, argv[1:])
    else:
        arguments = map(unicode, argv)
    argument_line = u''.join(arguments)
    print argument_line
    executable = unicode("cmd.exe")
    if debug:
        print 'Command line: ', executable, argument_line
    ret = shell32.ShellExecuteW(None, u"runas", executable, "/k " + argument_line, None, 1)
    print ret
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