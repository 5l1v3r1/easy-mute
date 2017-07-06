# EasyMute
For those who gets tired muting their audio using profile options like me.

**Turning the volume all the way down doesn't stop KDE from playing alert sounds. Switch pulseaudio profile to 'off' is the best solution.** 

#
## Installation
~~~~
$ git clone https://github.com/K4YT3X/EasyMute.git
$ cd EasyMute
$ sudo mv easymute.py /usr/bin/easymute
$ sudo chmod 755 /usr/bin/easymute
$ sudo chown root: /usr/bin/easymute
~~~~

#
## Usage
**It is highly recommended that you map the key super+M to the command easymute. It makes things a lot faster & easier.**
~~~~
$ easymute on                      # Turn on audio I/O
$ easymute off                     # Turn off audio I/O
$ easymute (without arguments)     # Switch between on & off
~~~~

#
## Uninstall
~~~~
$ sudo rm -f /usr/bin/easymute
~~~~
