<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/applescript.svg?maxAge=3600)](https://pypi.org/project/applescript/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/applescript.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/applescript.py/)

#### Installation
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
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>