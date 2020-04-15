#!/usr/bin/env python
import os
import only
import public
import subprocess

import applescript.tell

from ._run import _run

@only.osx
@public.add
def run(applescript, background=False):
    """run applescript file/string"""
    return _run(applescript, background)
