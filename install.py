#!/usr/bin/env python

import os
import shutil

FILES_LIST = 'files.list'

def confirm(prompt_prefix):
    answer = raw_input(prompt_prefix + ' [y/n/q] ')
    a = answer.lower()
    if a == 'y':
        return True
    elif a == 'n':
        return False
    else:
        exit(0)

def install_file(src, dest, write_backup=False):
    if os.path.lexists(dest):
        # return if this file has already been installed, or confirm to override if it hasn't
        try:
            if os.path.samefile(src, dest):
                print('%s has already been installed to %s' % (src, dest))
                return
        except OSError:
            pass
        if write_backup:
            backup_str = '(a backup will be created first)'
        else:
            backup_str = '(*no* backup will be made)'
        do_install = confirm('%s: destination %s already exists: override? %s' % (src, dest, backup_str))
    else:
        do_install = confirm('%s: install to %s?' % (src, dest))

    if do_install:
        # if the destination exists and we want a backup, make it
        if write_backup and os.path.lexists(dest):
            bkp_path = dest + '.bkp'

            # if the backup already exists, remove it
            if os.path.lexists(bkp_path):
                if os.path.isdir(bkp_path):
                    shutil.rmtree(bkp_path)
                else:
                    os.remove(bkp_path)

            os.rename(dest, bkp_path)

        # otherwise, remove the dest
        if not write_backup and os.path.lexists(dest):
            if os.path.isdir(dest):
                shutil.rmtree(dest)
            else:
                os.remove(dest)

        try:
            os.makedirs(os.path.dirname(dest))
        except OSError:
            pass

        # install
        os.symlink(src, dest)

def main(config):
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
            install_file(src, dest, config.backup)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='dotfiles installer')
    parser.add_argument('-n', '--no-backup', dest='backup', action='store_false',
            help='Disable the writing of backup files if destination files exist')
    args = parser.parse_args()

    main(args)
