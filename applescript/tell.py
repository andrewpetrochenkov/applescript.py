#!/usr/bin/env python
import only
import public
import runcmd
import temp


def _tempfile(content):
    path = temp.tempfile()
    open(path, "w").write(content)
    return path


@only.osx
@public.add
def app(appname, applescript, background=False):
    """execute applescript `tell application "VLC" ...`"""
    code = """tell app "%s"
    %s
end tell
""" % (appname, applescript)
    path = _tempfile(code)
    args = ["osascript", path]
    return runcmd.run(args, background=background)
