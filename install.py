#!/usr/bin/env python

import os
import shutil

FILES_LIST = 'files.list'

def confirm(prompt_prefix):
    answer = raw_input(prompt_prefix + ' [y/n] ')
    if answer.lower() == 'y':
        return True
    else:
        return False

def install_file(src, dest):
    if os.path.lexists(dest):
        # return if this file has already been installed, or confirm to override if it hasn't
        try:
            if os.path.samefile(src, dest):
                print('%s has already been installed to %s' % (src, dest))
                return
        except OSError:
            pass
        do_install = confirm('%s: destination %s already exists: override? (a backup will be created first)' % (src, dest))
    else:
        do_install = confirm('%s: install to %s?' % (src, dest))

    if do_install:
        if os.path.lexists(dest):
            bkp_path = dest + '.bkp'
            if os.path.exists(bkp_path):
                print('%s: backup %s already exists... please remove it' % (src, bkp_path))
                return
            shutil.move(dest, bkp_path)

        os.symlink(src, dest)

def main():
    source_dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(source_dir, FILES_LIST), 'r') as fp:
        for line in fp:
            cleaned = line.strip()
            if len(cleaned) == 0:
                continue
            fields = cleaned.split(' ')
            assert len(fields) == 2
            src = os.path.join(source_dir, fields[0])
            dest = os.path.abspath(os.path.expanduser(fields[1]))
            install_file(src, dest)


if __name__ == '__main__':
    main()
