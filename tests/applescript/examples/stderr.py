#!/usr/bin/env python
import applescript

r = applescript.run('log "hello world"')
print(r.err)
