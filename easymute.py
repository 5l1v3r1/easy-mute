#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 ___   __   ___  _  _  __  __  _  _  ____  ___
(  _) (  ) / __)( \/ )(  \/  )( )( )(_  _)(  _)
 ) _) /__\ \__ \ \  /  )    (  )()(   )(   ) _)
(___)(_)(_)(___/(__/  (_/\/\_) \__/  (__) (___)

EasyMute controls pulseaudio profile. It can easily
switch between <off> and <output:analog-stereo>

Adding this to system keyboard shortcut (e.g. Super+M)
is highly recommended

(C) 2017 K4YT3X
Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: https://www.gnu.org/licenses/gpl-3.0.txt

"""
import os
import sys
import subprocess
import avalon


def muted():
    """
        Determines if the profile is already '<off>'
        Returns Boolean
    """
    section = False
    output = subprocess.Popen(["pacmd", "list", "cards"], stdout=subprocess.PIPE).communicate()[0]
    output = output.decode().split('\n')
    for line in output:
        if 'card(s) available' in line:
            section = True
        if section:
            if 'active profile:' in line:
                if '<off>' in line:
                    return True
                else:
                    return False
    return False


def printHelp():
    print(avalon.FM.BD + 'USAGE:')
    print('easymute on                    Turn on audio I/O')
    print('easymute off                   Turn off audio I/O')
    print('easymute (without arguments)   Switch between on & off' + avalon.FM.RST)


try:
    if sys.argv[1] == 'off':
        os.system('pacmd set-card-profile 0 off')
        print(avalon.FG.R + avalon.FM.BD + 'MUTED' + avalon.FG.W)
    elif sys.argv[1] == 'on':
        os.system('pacmd set-card-profile 0 output:analog-stereo')
        print(avalon.FG.G + avalon.FM.BD + 'UNMUTED' + avalon.FG.W)
    elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
        printHelp()
    else:
        avalon.error('Unrecognized argument: ' + sys.argv[1])
        printHelp()
except IndexError:
    if muted():
        os.system('pacmd set-card-profile 0 output:analog-stereo')
        print(avalon.FG.G + avalon.FM.BD + 'UNMUTED' + avalon.FG.W)
    else:
        os.system('pacmd set-card-profile 0 off')
        print(avalon.FG.R + avalon.FM.BD + 'MUTED' + avalon.FG.W)
