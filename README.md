Children of Eden Synth Server
=============================
This is a program I wrote to enable 3 keyboardists to use one Roland Fantom XR to produce the sound necessary to play their parts in "Children of Eden".  This software has long been out of commission, but it worked well enough for the show especially considering how little time I had to work on it.  ^_^;;;

I started to convert this into "PatchCorral" a more general-purpose synth driving application written in Python before splitting it into its own project (https://github.com/defcello/PatchCorral) after opting for an engine rewrite.  The original web server code should still be mostly operational...

License
=======
GNU GPL v3 (http://www.gnu.org/licenses/#GPL)

Installation
============
This project requires:
 - Python 3.3 (will likely work on any Python 3 version)
 - "pyrtmidi" (http://trac.assembla.com/pkaudio/wiki/pyrtmidi) installed as a library for Python 3.3.
   - Note that the current public version of "pyrtmidi" supports Python 2.  I adapted and compiled it for Python 3, but never got permission from the original author to share the revised code.
   - You may want to check out "python-rtmidi" (https://pypi.python.org/pypi/python-rtmidi) that I ended up using for PatchCorral.
 - PySide
   - Note that this is for the elements of PatchCorral that are still in here.  You shouldn't need PySide for the web server.

Usage
=====
1. Execute "bin/main.py".
2. If everything works well, you'll get a Windows terminal with IP address information for the web server.  Just point an Internet Browser to that IP address (e.g. "http://192.168.0.1") and you should be ready for the floodwaters!

What's Next?
============
This project served its purpose well enough, but it was far from perfect.  If I were to ever pick it up again, I'd replace the web interface with a proper web application framework.  I'd also redesign the web UI to be a status monitor, using MIDI keyboard events and/or swipes to change instruments instead of requiring the user to tap on the screen.
