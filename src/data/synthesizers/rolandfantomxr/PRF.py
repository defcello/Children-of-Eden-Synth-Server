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
#  Module Information.
#  @date 3/10/2013 Created file.  -jc
#  @author John Crawford

from engine.mididevice import MIDIVoice



NAME = 'PR-F'

PATCHES = [
  MIDIVoice('ConcertGrand', 87, 69, 0, 'AC.PIANO', 'PR-F 001'),
  MIDIVoice('Hall Concert', 87, 69, 1, 'AC.PIANO', 'PR-F 002'),
  MIDIVoice('Bright Tune', 87, 69, 2, 'AC.PIANO', 'PR-F 003'),
  MIDIVoice('Mellow Tune', 87, 69, 3, 'AC.PIANO', 'PR-F 004'),
  MIDIVoice('Back E-Grand', 87, 69, 4, 'EL.PIANO', 'PR-F 005'),
  MIDIVoice('EP mkI', 87, 69, 5, 'EL.PIANO', 'PR-F 006'),
  MIDIVoice('Stage EP', 87, 69, 6, 'EL.PIANO', 'PR-F 007'),
  MIDIVoice('MKS20EnsemEP', 87, 69, 7, 'EL.PIANO', 'PR-F 008'),
  MIDIVoice('UltimatGrand', 87, 69, 8, 'AC.PIANO', 'PR-F 009'),
  MIDIVoice('X Pure Grand', 87, 69, 9, 'AC.PIANO', 'PR-F 010'),
  MIDIVoice('Studio Grand', 87, 69, 10, 'AC.PIANO', 'PR-F 011'),
  MIDIVoice('88ConcertPno', 87, 69, 11, 'AC.PIANO', 'PR-F 012'),
  MIDIVoice('DryStudio88', 87, 69, 12, 'AC.PIANO', 'PR-F 013'),
  MIDIVoice('First Choice', 87, 69, 13, 'AC.PIANO', 'PR-F 014'),
  MIDIVoice('Rokkin\' pF', 87, 69, 14, 'AC.PIANO', 'PR-F 015'),
  MIDIVoice('Dark Grand', 87, 69, 15, 'AC.PIANO', 'PR-F 016'),
  MIDIVoice('Piano Oz', 87, 69, 16, 'AC.PIANO', 'PR-F 017'),
  MIDIVoice('Grand Hall', 87, 69, 17, 'AC.PIANO', 'PR-F 018'),
  MIDIVoice('X Piano +Str', 87, 69, 18, 'AC.PIANO', 'PR-F 019'),
  MIDIVoice('Arie Piano', 87, 69, 19, 'AC.PIANO', 'PR-F 020'),
  MIDIVoice('Cicada Piano', 87, 69, 20, 'AC.PIANO', 'PR-F 021'),
  MIDIVoice('Clare Voyent', 87, 69, 21, 'AC.PIANO', 'PR-F 022'),
  MIDIVoice('X Piano +Pad', 87, 69, 22, 'AC.PIANO', 'PR-F 023'),
  MIDIVoice('X Piano +Vox', 87, 69, 23, 'AC.PIANO', 'PR-F 024'),
  MIDIVoice('FX Piano', 87, 69, 24, 'AC.PIANO', 'PR-F 025'),
  MIDIVoice('AmbientPiano', 87, 69, 25, 'AC.PIANO', 'PR-F 026'),
  MIDIVoice('Tre EP', 87, 69, 26, 'EL.PIANO', 'PR-F 027'),
  MIDIVoice('Stage Phazer', 87, 69, 27, 'EL.PIANO', 'PR-F 028'),
  MIDIVoice('StageCabinet', 87, 69, 28, 'EL.PIANO', 'PR-F 029'),
  MIDIVoice('AMP EP', 87, 69, 29, 'EL.PIANO', 'PR-F 030'),
  MIDIVoice('VelPanWurly', 87, 69, 30, 'EL.PIANO', 'PR-F 031'),
  MIDIVoice('Mr.AXXE', 87, 69, 31, 'EL.PIANO', 'PR-F 032'),
  MIDIVoice('1983 EP', 87, 69, 32, 'EL.PIANO', 'PR-F 033'),
  MIDIVoice('EP Stack', 87, 69, 33, 'EL.PIANO', 'PR-F 034'),
  MIDIVoice('EP Belle', 87, 69, 34, 'EL.PIANO', 'PR-F 035'),
  MIDIVoice('Chocolate EP', 87, 69, 35, 'EL.PIANO', 'PR-F 036'),
  MIDIVoice('Abstract EP', 87, 69, 36, 'EL.PIANO', 'PR-F 037'),
  MIDIVoice('Ringy EP', 87, 69, 37, 'EL.PIANO', 'PR-F 038'),
  MIDIVoice('Hipchord', 87, 69, 38, 'EL.PIANO', 'PR-F 039'),
  MIDIVoice('Snappy Clav', 87, 69, 39, 'KEYBOARDS', 'PR-F 040'),
  MIDIVoice('Over-D6', 87, 69, 40, 'KEYBOARDS', 'PR-F 041'),
  MIDIVoice('CoupleHarpsi', 87, 69, 41, 'KEYBOARDS', 'PR-F 042'),
  MIDIVoice('HimalayaThaw', 87, 69, 42, 'BELL', 'PR-F 043'),
  MIDIVoice('Ballad Bells', 87, 69, 43, 'BELL', 'PR-F 044'),
  MIDIVoice('Bell Monitor', 87, 69, 44, 'BELL', 'PR-F 045'),
  MIDIVoice('SideBandBell', 87, 69, 45, 'BELL', 'PR-F 046'),
  MIDIVoice('SBF Saw Bell', 87, 69, 46, 'BELL', 'PR-F 047'),
  MIDIVoice('TubyRuesday', 87, 69, 47, 'BELL', 'PR-F 048'),
  MIDIVoice('Music Box 2', 87, 69, 48, 'BELL', 'PR-F 049'),
  MIDIVoice('AirPluck', 87, 69, 49, 'MALLET', 'PR-F 050'),
  MIDIVoice('Airie Vibez', 87, 69, 50, 'MALLET', 'PR-F 051'),
  MIDIVoice('Ringy Vibes', 87, 69, 51, 'MALLET', 'PR-F 052'),
  MIDIVoice('50`SteelDrms', 87, 69, 52, 'MALLET', 'PR-F 053'),
  MIDIVoice('VKHold4Speed', 87, 69, 53, 'ORGAN', 'PR-F 054'),
  MIDIVoice('X Perc Organ', 87, 69, 54, 'ORGAN', 'PR-F 055'),
  MIDIVoice('Rocky Organ', 87, 69, 55, 'ORGAN', 'PR-F 056'),
  MIDIVoice('Purple Organ', 87, 69, 56, 'ORGAN', 'PR-F 057'),
  MIDIVoice('Phono Organ', 87, 69, 57, 'ORGAN', 'PR-F 058'),
  MIDIVoice('Mid Pipe Org', 87, 69, 58, 'ORGAN', 'PR-F 059'),
  MIDIVoice('ParisRomance', 87, 69, 59, 'ACCORDION', 'PR-F 060'),
  MIDIVoice('La Seine', 87, 69, 60, 'ACCORDION', 'PR-F 061'),
  MIDIVoice('VntgAccrdion', 87, 69, 61, 'ACCORDION', 'PR-F 062'),
  MIDIVoice('Oktoberfest', 87, 69, 62, 'ACCORDION', 'PR-F 063'),
  MIDIVoice('NaturalNylon', 87, 69, 63, 'AC.GUITAR', 'PR-F 064'),
  MIDIVoice('Nylon Gtr VS', 87, 69, 64, 'AC.GUITAR', 'PR-F 065'),
  MIDIVoice('Double Nylon', 87, 69, 65, 'AC.GUITAR', 'PR-F 066'),
  MIDIVoice('Mellow Nylon', 87, 69, 66, 'AC.GUITAR', 'PR-F 067'),
  MIDIVoice('FlamencoGt X', 87, 69, 67, 'AC.GUITAR', 'PR-F 068'),
  MIDIVoice('El Toro Gtr', 87, 69, 68, 'AC.GUITAR', 'PR-F 069'),
  MIDIVoice('Dyna Nylon', 87, 69, 69, 'AC.GUITAR', 'PR-F 070'),
  MIDIVoice('NylonGt /HO', 87, 69, 70, 'AC.GUITAR', 'PR-F 071'),
  MIDIVoice('Nylon 4way', 87, 69, 71, 'AC.GUITAR', 'PR-F 072'),
  MIDIVoice('Nyl-Intro', 87, 69, 72, 'AC.GUITAR', 'PR-F 073'),
  MIDIVoice('Nylon Dreams', 87, 69, 73, 'AC.GUITAR', 'PR-F 074'),
  MIDIVoice('With Love', 87, 69, 74, 'AC.GUITAR', 'PR-F 075'),
  MIDIVoice('Amore Story', 87, 69, 75, 'AC.GUITAR', 'PR-F 076'),
  MIDIVoice('Interlude', 87, 69, 76, 'AC.GUITAR', 'PR-F 077'),
  MIDIVoice('Sweet Tears', 87, 69, 77, 'AC.GUITAR', 'PR-F 078'),
  MIDIVoice('WithALtlHelp', 87, 69, 78, 'AC.GUITAR', 'PR-F 079'),
  MIDIVoice('Double Track', 87, 69, 79, 'EL.GUITAR', 'PR-F 080'),
  MIDIVoice('Mystic Gtr', 87, 69, 80, 'EL.GUITAR', 'PR-F 081'),
  MIDIVoice('Cut Thru Wah', 87, 69, 81, 'EL.GUITAR', 'PR-F 082'),
  MIDIVoice('GuitaratiuG', 87, 69, 82, 'EL.GUITAR', 'PR-F 083'),
  MIDIVoice('WahGt Riff', 87, 69, 83, 'EL.GUITAR', 'PR-F 084'),
  MIDIVoice('Larsen /Aft', 87, 69, 84, 'DIST.GUITAR', 'PR-F 085'),
  MIDIVoice('Darmstrat X', 87, 69, 85, 'DIST.GUITAR', 'PR-F 086'),
  MIDIVoice('Rockin\' Dly', 87, 69, 86, 'DIST.GUITAR', 'PR-F 087'),
  MIDIVoice('DistGt Mt', 87, 69, 87, 'DIST.GUITAR', 'PR-F 088'),
  MIDIVoice('GTR Heroes', 87, 69, 88, 'DIST.GUITAR', 'PR-F 089'),
  MIDIVoice('X Mute Bass', 87, 69, 89, 'BASS', 'PR-F 090'),
  MIDIVoice('Nu Finger Bs', 87, 69, 90, 'BASS', 'PR-F 091'),
  MIDIVoice('Soulfinger', 87, 69, 91, 'BASS', 'PR-F 092'),
  MIDIVoice('X Finger Bs1', 87, 69, 92, 'BASS', 'PR-F 093'),
  MIDIVoice('StickyOctave', 87, 69, 93, 'BASS', 'PR-F 094'),
  MIDIVoice('Bass & Amp', 87, 69, 94, 'BASS', 'PR-F 095'),
  MIDIVoice('Chorus Bass', 87, 69, 95, 'BASS', 'PR-F 096'),
  MIDIVoice('X 5String Bs', 87, 69, 96, 'BASS', 'PR-F 097'),
  MIDIVoice('6-Pack Stick', 87, 69, 97, 'BASS', 'PR-F 098'),
  MIDIVoice('Nu Pick Bass', 87, 69, 98, 'BASS', 'PR-F 099'),
  MIDIVoice('Comp Picker', 87, 69, 99, 'BASS', 'PR-F 100'),
  MIDIVoice('X Finger Bs2', 87, 69, 100, 'BASS', 'PR-F 101'),
  MIDIVoice('X Picked Bs', 87, 69, 101, 'BASS', 'PR-F 102'),
  MIDIVoice('Mutation', 87, 69, 102, 'BASS', 'PR-F 103'),
  MIDIVoice('X Slap Bass', 87, 69, 103, 'BASS', 'PR-F 104'),
  MIDIVoice('Fuzz Mute', 87, 69, 104, 'BASS', 'PR-F 105'),
  MIDIVoice('Doubled Bass', 87, 69, 105, 'BASS', 'PR-F 106'),
  MIDIVoice('NewAge Frtls', 87, 69, 106, 'BASS', 'PR-F 107'),
  MIDIVoice('Powerline', 87, 69, 107, 'SYNTH BASS', 'PR-F 108'),
  MIDIVoice('Reso SynBass', 87, 69, 108, 'SYNTH BASS', 'PR-F 109'),
  MIDIVoice('Synth Bassic', 87, 69, 109, 'SYNTH BASS', 'PR-F 110'),
  MIDIVoice('Down 4 It', 87, 69, 110, 'SYNTH BASS', 'PR-F 111'),
  MIDIVoice('Glider Bass', 87, 69, 111, 'SYNTH BASS', 'PR-F 112'),
  MIDIVoice('Fundamental', 87, 69, 112, 'SYNTH BASS', 'PR-F 113'),
  MIDIVoice('Artus Bass', 87, 69, 113, 'SYNTH BASS', 'PR-F 114'),
  MIDIVoice('Sweet & Low', 87, 69, 114, 'SYNTH BASS', 'PR-F 115'),
  MIDIVoice('Change It', 87, 69, 115, 'SYNTH BASS', 'PR-F 116'),
  MIDIVoice('the ONE', 87, 69, 116, 'SYNTH BASS', 'PR-F 117'),
  MIDIVoice('ChoruSE ONE', 87, 69, 117, 'SYNTH BASS', 'PR-F 118'),
  MIDIVoice('Eyes Bass', 87, 69, 118, 'SYNTH BASS', 'PR-F 119'),
  MIDIVoice('Secret Bass', 87, 69, 119, 'SYNTH BASS', 'PR-F 120'),
  MIDIVoice('Base BoX', 87, 69, 120, 'SYNTH BASS', 'PR-F 121'),
  MIDIVoice('Nu RnB Bass', 87, 69, 121, 'SYNTH BASS', 'PR-F 122'),
  MIDIVoice('D n\' Bass', 87, 69, 122, 'SYNTH BASS', 'PR-F 123'),
  MIDIVoice('DnB Bass 1', 87, 69, 123, 'SYNTH BASS', 'PR-F 124'),
  MIDIVoice('Fat Bottom', 87, 69, 124, 'SYNTH BASS', 'PR-F 125'),
  MIDIVoice('Deep S-E', 87, 69, 125, 'SYNTH BASS', 'PR-F 126'),
  MIDIVoice('Nu Bace', 87, 69, 126, 'SYNTH BASS', 'PR-F 127'),
  MIDIVoice('Mini Like!', 87, 69, 127, 'SYNTH BASS', 'PR-F 128'),
]