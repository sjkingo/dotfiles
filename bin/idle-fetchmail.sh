#!/bin/bash
nohup fetchmail -f ~/.fetchmailrc.uq -v >nohup.uq &
nohup fetchmail -f ~/.fetchmailrc.devnull -v >nohup.devnull &
