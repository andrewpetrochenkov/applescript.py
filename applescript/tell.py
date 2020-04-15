#!/usr/bin/env python
import only
import public

from ._run import _run


@only.osx
@public.add
def app(appname, applescript, background=False):
    """execute applescript `tell application "VLC" ...`"""
    cmd = """tell app "%s"
    %s
end tell
""" % (appname, applescript)
    return _run(cmd,background)
