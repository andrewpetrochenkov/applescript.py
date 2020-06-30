#!/usr/bin/env python
import applescript

r = applescript.run('["hello", "world"].join(" ");', javascript=True)
print(r.out)
