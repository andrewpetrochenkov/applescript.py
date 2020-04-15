import os
import subprocess

from ._result import Result
from ._temp import _tempfile

def _run(applescript, background=False):
    """run applescript file/string"""
    if not background:
        args = ["osascript", "-"]
        kwargs = dict(stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    else:
        f = applescript if os.path.exists(applescript) else _tempfile()
        if not os.path.exists(applescript):
            open(f,'w').write(applescript)
        args = ["osascript", f]
        kwargs = {'stdout':open(os.devnull, 'wb'),'stderr':open(os.devnull, 'wb')}
    proc = subprocess.Popen(args,**kwargs)
    if not background:
        cmd = open(applescript).read() if os.path.exists(applescript) else applescript
        out, err = proc.communicate(input=cmd.encode("utf-8"))
        return Result(proc.returncode,out, err)
