﻿####################################################################################################
# Copyright 2013 John Crawford
#
# This file is part of SynthServer.
#
# SynthServer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SynthServer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SynthServer.  If not, see <http://www.gnu.org/licenses/>.
####################################################################################################

## @file
#  Module for communicating with Roland Fantom-XR connected over USB MIDI.
#  @date 3/8/2013 Created file.  -jc
#  @author John Crawford

from . import UserVoices, PRA, PRB, PRC, PRD, PRE, PRF, PRG, PRH, GM, SRX04, SRX05, SRX06, SRX07, SRX09
from engine import mididevice
import itertools
import rtmidi



#Available categories:
# AC.BRASS
# AC.GUITAR
# AC.PIANO
# ACCORDION
# BASS
# BEAT&GROOVE
# BELL
# BRIGHT PAD
# COMBINATION
# DIST.GUITAR
# DRUMS
# EL.GUITAR
# EL.PIANO
# ETHNIC
# FLUTE
# FRETTED
# HARD LEAD
# HARMONICA
# HIT&STAB
# KEYBOARDS          #Clavinet, Harpsichord, Celesta
# MALLET
# ORCHESTRA
# ORGAN
# OTHER SYNTH
# PERCUSSION
# PLUCKED
# PULSATING
# SAX
# SOFT LEAD
# SOFT PAD
# SOUND FX
# STRINGS
# SYNTH BASS
# SYNTH BRASS
# SYNTH FX
# TECHNO SYNTH
# VOX
# WIND

class MIDIOutDevice(mididevice.MIDIOutDevice):

  ID = 'FANTOM-X'  #Note that at least in Windows this can sometimes show up like "4- FANTOM-X"

  def __init__(self, id=None, defaultChannel=None):
    if id is None:
      MIDIOutDevice.ID
    voices = list(itertools.chain(*map(
      lambda x: x.PATCHES,
      [
        UserVoices, PRA, PRB, PRC, PRD, PRE, PRF, PRG, PRH, GM, SRX04, SRX05, SRX06, SRX07, SRX09,
      ],
    )))
    super().__init__(id, voices, defaultChannel)
