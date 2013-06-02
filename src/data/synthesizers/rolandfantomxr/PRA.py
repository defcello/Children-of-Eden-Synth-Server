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



NAME = 'PR-A'

PATCHES = [
  MIDIVoice('So true...', 87, 64, 0, 'AC.PIANO', 'PR-A 001'),
  MIDIVoice('ConcertPiano', 87, 64, 1, 'AC.PIANO', 'PR-A 002'),
  MIDIVoice('Warm Piano', 87, 64, 2, 'AC.PIANO', 'PR-A 003'),
  MIDIVoice('Warm Pad Pno', 87, 64, 3, 'AC.PIANO', 'PR-A 004'),
  MIDIVoice('Warm Str Pno', 87, 64, 4, 'AC.PIANO', 'PR-A 005'),
  MIDIVoice('BealeSt Walk', 87, 64, 5, 'AC.PIANO', 'PR-A 006'),
  MIDIVoice('Rapsody', 87, 64, 6, 'AC.PIANO', 'PR-A 007'),
  MIDIVoice('JD-800 Piano', 87, 64, 7, 'AC.PIANO', 'PR-A 008'),
  MIDIVoice('SA Dance Pno', 87, 64, 8, 'AC.PIANO', 'PR-A 009'),
  MIDIVoice('FS E-Grand', 87, 64, 9, 'AC.PIANO', 'PR-A 010'),
  MIDIVoice('FS Blend Pno', 87, 64, 10, 'AC.PIANO', 'PR-A 011'),
  MIDIVoice('LA Piano', 87, 64, 11, 'AC.PIANO', 'PR-A 012'),
  MIDIVoice('FS 70\'EP', 87, 64, 12, 'EL.PIANO', 'PR-A 013'),
  MIDIVoice('StageEP Trem', 87, 64, 13, 'EL.PIANO', 'PR-A 014'),
  MIDIVoice('Back2the60s', 87, 64, 14, 'EL.PIANO', 'PR-A 015'),
  MIDIVoice('Tine EP', 87, 64, 15, 'EL.PIANO', 'PR-A 016'),
  MIDIVoice('LEO EP', 87, 64, 16, 'EL.PIANO', 'PR-A 017'),
  MIDIVoice('LonesomeRoad', 87, 64, 17, 'EL.PIANO', 'PR-A 018'),
  MIDIVoice('Age\'n\'Tines', 87, 64, 18, 'EL.PIANO', 'PR-A 019'),
  MIDIVoice('Brill TremEP', 87, 64, 19, 'EL.PIANO', 'PR-A 020'),
  MIDIVoice('Crystal EP', 87, 64, 20, 'EL.PIANO', 'PR-A 021'),
  MIDIVoice('Celestial EP', 87, 64, 21, 'EL.PIANO', 'PR-A 022'),
  MIDIVoice('Spirit Tines', 87, 64, 22, 'EL.PIANO', 'PR-A 023'),
  MIDIVoice('Psycho EP', 87, 64, 23, 'EL.PIANO', 'PR-A 024'),
  MIDIVoice('Mk2 Stg phsr', 87, 64, 24, 'EL.PIANO', 'PR-A 025'),
  MIDIVoice('SA Stacks', 87, 64, 25, 'EL.PIANO', 'PR-A 026'),
  MIDIVoice('Backing PhEP', 87, 64, 26, 'EL.PIANO', 'PR-A 027'),
  MIDIVoice('Balladeer', 87, 64, 27, 'EL.PIANO', 'PR-A 028'),
  MIDIVoice('Remember', 87, 64, 28, 'EL.PIANO', 'PR-A 029'),
  MIDIVoice('FS Wurly', 87, 64, 29, 'EL.PIANO', 'PR-A 030'),
  MIDIVoice('Wurly Trem', 87, 64, 30, 'EL.PIANO', 'PR-A 031'),
  MIDIVoice('Super Wurly', 87, 64, 31, 'EL.PIANO', 'PR-A 032'),
  MIDIVoice('Pulse EPno', 87, 64, 32, 'EL.PIANO', 'PR-A 033'),
  MIDIVoice('Fonky Fonky', 87, 64, 33, 'EL.PIANO', 'PR-A 034'),
  MIDIVoice('FM EP', 87, 64, 34, 'EL.PIANO', 'PR-A 035'),
  MIDIVoice('FM-777', 87, 64, 35, 'EL.PIANO', 'PR-A 036'),
  MIDIVoice('FM EPad', 87, 64, 36, 'EL.PIANO', 'PR-A 037'),
  MIDIVoice('D6 Clavi', 87, 64, 37, 'KEYBOARDS', 'PR-A 038'),
  MIDIVoice('Cutter Clavi', 87, 64, 38, 'KEYBOARDS', 'PR-A 039'),
  MIDIVoice('FS Clavi', 87, 64, 39, 'KEYBOARDS', 'PR-A 040'),
  MIDIVoice('Funky D', 87, 64, 40, 'KEYBOARDS', 'PR-A 041'),
  MIDIVoice('Phase Clavi', 87, 64, 41, 'KEYBOARDS', 'PR-A 042'),
  MIDIVoice('BPF Clavi Ph', 87, 64, 42, 'KEYBOARDS', 'PR-A 043'),
  MIDIVoice('Pulse Clavi', 87, 64, 43, 'KEYBOARDS', 'PR-A 044'),
  MIDIVoice('Analog Clavi', 87, 64, 44, 'KEYBOARDS', 'PR-A 045'),
  MIDIVoice('Reso Clavi', 87, 64, 45, 'KEYBOARDS', 'PR-A 046'),
  MIDIVoice('Harpsy Clavi', 87, 64, 46, 'KEYBOARDS', 'PR-A 047'),
  MIDIVoice('FS Harpsi', 87, 64, 47, 'KEYBOARDS', 'PR-A 048'),
  MIDIVoice('Amadeus', 87, 64, 48, 'KEYBOARDS', 'PR-A 049'),
  MIDIVoice('FS Celesta', 87, 64, 49, 'KEYBOARDS', 'PR-A 050'),
  MIDIVoice('FS Glocken', 87, 64, 50, 'BELL', 'PR-A 051'),
  MIDIVoice('Music Bells', 87, 64, 51, 'BELL', 'PR-A 052'),
  MIDIVoice('FS Musicbox', 87, 64, 52, 'BELL', 'PR-A 053'),
  MIDIVoice('MuBox Pad', 87, 64, 53, 'BELL', 'PR-A 054'),
  MIDIVoice('Kalimbells', 87, 64, 54, 'BELL', 'PR-A 055'),
  MIDIVoice('Himalaya Ice', 87, 64, 55, 'BELL', 'PR-A 056'),
  MIDIVoice('Dreaming Box', 87, 64, 56, 'BELL', 'PR-A 057'),
  MIDIVoice('Step Ice', 87, 64, 57, 'BELL', 'PR-A 058'),
  MIDIVoice('FS Bell 1', 87, 64, 58, 'BELL', 'PR-A 059'),
  MIDIVoice('FS Bell 2', 87, 64, 59, 'BELL', 'PR-A 060'),
  MIDIVoice('Candy Bell', 87, 64, 60, 'BELL', 'PR-A 061'),
  MIDIVoice('FS Chime', 87, 64, 61, 'BELL', 'PR-A 062'),
  MIDIVoice('Bell Ring', 87, 64, 62, 'BELL', 'PR-A 063'),
  MIDIVoice('Tubular Bell', 87, 64, 63, 'BELL', 'PR-A 064'),
  MIDIVoice('5th Key', 87, 64, 64, 'BELL', 'PR-A 065'),
  MIDIVoice('Vibrations', 87, 64, 65, 'MALLET', 'PR-A 066'),
  MIDIVoice('FS Vibe', 87, 64, 66, 'MALLET', 'PR-A 067'),
  MIDIVoice('FS Marimba', 87, 64, 67, 'MALLET', 'PR-A 068'),
  MIDIVoice('FS Xylo', 87, 64, 68, 'MALLET', 'PR-A 069'),
  MIDIVoice('Ethno Keys', 87, 64, 69, 'MALLET', 'PR-A 070'),
  MIDIVoice('Synergy MLT', 87, 64, 70, 'MALLET', 'PR-A 071'),
  MIDIVoice('Steel Drums', 87, 64, 71, 'MALLET', 'PR-A 072'),
  MIDIVoice('Xylosizer', 87, 64, 72, 'MALLET', 'PR-A 073'),
  MIDIVoice('Toy Box', 87, 64, 73, 'MALLET', 'PR-A 074'),
  MIDIVoice('FullDraw Org', 87, 64, 74, 'ORGAN', 'PR-A 075'),
  MIDIVoice('StakDraw Org', 87, 64, 75, 'ORGAN', 'PR-A 076'),
  MIDIVoice('FullStop Org', 87, 64, 76, 'ORGAN', 'PR-A 077'),
  MIDIVoice('FS Perc Org', 87, 64, 77, 'ORGAN', 'PR-A 078'),
  MIDIVoice('Euro Organ', 87, 64, 78, 'ORGAN', 'PR-A 079'),
  MIDIVoice('Perky Organ', 87, 64, 79, 'ORGAN', 'PR-A 080'),
  MIDIVoice('LoFi PercOrg', 87, 64, 80, 'ORGAN', 'PR-A 081'),
  MIDIVoice('Rochno Org', 87, 64, 81, 'ORGAN', 'PR-A 082'),
  MIDIVoice('R&B Organ 1', 87, 64, 82, 'ORGAN', 'PR-A 083'),
  MIDIVoice('R&B Organ 2', 87, 64, 83, 'ORGAN', 'PR-A 084'),
  MIDIVoice('Zepix Organ', 87, 64, 84, 'ORGAN', 'PR-A 085'),
  MIDIVoice('Peep Durple', 87, 64, 85, 'ORGAN', 'PR-A 086'),
  MIDIVoice('FS Dist Bee', 87, 64, 86, 'ORGAN', 'PR-A 087'),
  MIDIVoice('60\'s Org 1', 87, 64, 87, 'ORGAN', 'PR-A 088'),
  MIDIVoice('60\'s Org 2', 87, 64, 88, 'ORGAN', 'PR-A 089'),
  MIDIVoice('FS SoapOpera', 87, 64, 89, 'ORGAN', 'PR-A 090'),
  MIDIVoice('Chapel Organ', 87, 64, 90, 'ORGAN', 'PR-A 091'),
  MIDIVoice('Grand Pipe', 87, 64, 91, 'ORGAN', 'PR-A 092'),
  MIDIVoice('Masked Opera', 87, 64, 92, 'ORGAN', 'PR-A 093'),
  MIDIVoice('Pipe Org/Mod', 87, 64, 93, 'ORGAN', 'PR-A 094'),
  MIDIVoice('Vodkakordion', 87, 64, 94, 'ACCORDION', 'PR-A 095'),
  MIDIVoice('Squeeze Me!', 87, 64, 95, 'ACCORDION', 'PR-A 096'),
  MIDIVoice('Guinguette', 87, 64, 96, 'ACCORDION', 'PR-A 097'),
  MIDIVoice('Harmonderca', 87, 64, 97, 'HARMONICA', 'PR-A 098'),
  MIDIVoice('BluesHrp V/S', 87, 64, 98, 'HARMONICA', 'PR-A 099'),
  MIDIVoice('Green Bullet', 87, 64, 99, 'HARMONICA', 'PR-A 100'),
  MIDIVoice('SoftNyln Gtr', 87, 64, 100, 'AC.GUITAR', 'PR-A 101'),
  MIDIVoice('FS Nylon Gt', 87, 64, 101, 'AC.GUITAR', 'PR-A 102'),
  MIDIVoice('Wet Nyln Gtr', 87, 64, 102, 'AC.GUITAR', 'PR-A 103'),
  MIDIVoice('Pre Mass Hum', 87, 64, 103, 'AC.GUITAR', 'PR-A 104'),
  MIDIVoice('Thick Steel', 87, 64, 104, 'AC.GUITAR', 'PR-A 105'),
  MIDIVoice('Uncle Martin', 87, 64, 105, 'AC.GUITAR', 'PR-A 106'),
  MIDIVoice('Wide Ac Gtr', 87, 64, 106, 'AC.GUITAR', 'PR-A 107'),
  MIDIVoice('Comp Stl Gtr', 87, 64, 107, 'AC.GUITAR', 'PR-A 108'),
  MIDIVoice('Stl Gtr Duo', 87, 64, 108, 'AC.GUITAR', 'PR-A 109'),
  MIDIVoice('FS 12str Gtr', 87, 64, 109, 'AC.GUITAR', 'PR-A 110'),
  MIDIVoice('So good !', 87, 64, 110, 'AC.GUITAR', 'PR-A 111'),
  MIDIVoice('Muted Gtr Pk', 87, 64, 111, 'EL.GUITAR', 'PR-A 112'),
  MIDIVoice('StratSeq\'nce', 87, 64, 112, 'EL.GUITAR', 'PR-A 113'),
  MIDIVoice('Fixx it', 87, 64, 113, 'EL.GUITAR', 'PR-A 114'),
  MIDIVoice('Jazz Guitar', 87, 64, 114, 'EL.GUITAR', 'PR-A 115'),
  MIDIVoice('DynoJazz Gtr', 87, 64, 115, 'EL.GUITAR', 'PR-A 116'),
  MIDIVoice('Wet TC', 87, 64, 116, 'EL.GUITAR', 'PR-A 117'),
  MIDIVoice('Clean Gtr', 87, 64, 117, 'EL.GUITAR', 'PR-A 118'),
  MIDIVoice('Crimson Gtr', 87, 64, 118, 'EL.GUITAR', 'PR-A 119'),
  MIDIVoice('Touchee Funk', 87, 64, 119, 'EL.GUITAR', 'PR-A 120'),
  MIDIVoice('Plug n\' Gig', 87, 64, 120, 'EL.GUITAR', 'PR-A 121'),
  MIDIVoice('Kinda Kurt', 87, 64, 121, 'EL.GUITAR', 'PR-A 122'),
  MIDIVoice('Nice Oct Gtr', 87, 64, 122, 'EL.GUITAR', 'PR-A 123'),
  MIDIVoice('Strat Gtr', 87, 64, 123, 'EL.GUITAR', 'PR-A 124'),
  MIDIVoice('JC Strat Bdy', 87, 64, 124, 'EL.GUITAR', 'PR-A 125'),
  MIDIVoice('Twin StratsB', 87, 64, 125, 'EL.GUITAR', 'PR-A 126'),
  MIDIVoice('BluNoteStrat', 87, 64, 126, 'EL.GUITAR', 'PR-A 127'),
  MIDIVoice('FS Funk Gtr', 87, 64, 127, 'EL.GUITAR', 'PR-A 128'),
]