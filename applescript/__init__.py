#!/usr/bin/env python
__all__ = ['run']

import os
import only
import subprocess

import applescript.tell

from ._run import _run

@only.osx
def run(applescript, background=False, javascript=True):
    """run applescript file/string"""
    return _run(applescript, background, javascript)
