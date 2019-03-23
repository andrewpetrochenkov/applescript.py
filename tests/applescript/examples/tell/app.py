#!/usr/bin/env python
import applescript

applescript.tell.app("Terminal", 'do script "ls"')
applescript.tell.app("Terminal", 'do script "echo background"',background=True)
