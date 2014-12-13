dotfiles
========

This is Sam's collection of Linux dotfiles. To install, simple type
`./install.py` and the script will prompt you to install each file
listed in `files.list`. If any of the files already exist, they will
be backed up (by appending `.bkp` to their name) first, unless the `-n`
argument is given, in which case they will be overritten.

Usage:
------

```
usage: install.py [-h] [-n] [-v]

dotfiles installer

optional arguments:
  -h, --help       show this help message and exit
  -n, --no-backup  Disable the writing of backup files if destination files
                   exist
  -v, --verbose    Be verbose when updating symlinks
```
