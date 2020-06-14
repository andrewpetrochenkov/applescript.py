__all__ = ['app']

import only

from ._run import _run


@only.osx
def app(appname, applescript, background=False):
    """execute applescript `tell application "VLC" ...`"""
    cmd = """tell app "%s"
    %s
end tell
""" % (appname, applescript)
    return _run(cmd,background)
