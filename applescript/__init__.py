#!/usr/bin/env python
import os
import only
import public
import runcmd
import temp
import applescript.tell


@only.osx
@public.add
def run(applescript, background=False):
    """run applescript file/string"""
    path = applescript
    if not os.path.exists(applescript):  # source code
        path = temp.tempfile()
        open(path, "w").write(applescript)
    args = ["osascript", path]
    return runcmd.run(args, background=background)
