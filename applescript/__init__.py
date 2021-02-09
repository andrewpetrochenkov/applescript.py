__all__ = ['run']


import os
import subprocess

import applescript.tell

from ._run import _run


def run(applescript, background=False, javascript=False):
    """run applescript file/string"""
    return _run(applescript, background, javascript)
