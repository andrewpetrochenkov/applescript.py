<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/applescript.svg?maxAge=3600)](https://pypi.org/project/applescript/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/applescript.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/applescript.py/actions)

### Installation
```bash
$ [sudo] pip install applescript
```

#### Examples
```python
>>> import applescript
>>> r = applescript.run('return 1')
>>> r = applescript.run('path/to/file.applescript')

>>> r.code
0
>>> r.out
'hello world'
>>> r.err
''
```

`tell application "appname"`
```python
>>> applescript.tell.app("Terminal",'do script "ls"')
>>> applescript.tell.app("Terminal",'do script "ls"',background=True)
```

javascript (JXA)
```python
>>> applescript.run('...',javascript=True)
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
