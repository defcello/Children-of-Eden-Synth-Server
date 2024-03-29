﻿####################################################################################################
# Copyright 2013 John Crawford
#
# This file is part of PatchCorral.
#
# PatchCorral is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PatchCorral is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PatchCorral.  If not, see <http://www.gnu.org/licenses/>.
####################################################################################################

## @file
#  Module Information.
#  @date 3/10/2013 Created file.  -jc
#  @author John Crawford

from MIDIDevice import MIDIVoice



NAME = 'GM'

PATCHES = [
  MIDIVoice('Piano 1', 121, 0, 0, 'AC.PIANO', 'GM 001'),
  MIDIVoice('Piano 1w', 121, 1, 0, 'AC.PIANO', 'GM 002'),
  MIDIVoice('European Pf', 121, 2, 0, 'AC.PIANO', 'GM 003'),
  MIDIVoice('Piano 2', 121, 0, 1, 'AC.PIANO', 'GM 004'),
  MIDIVoice('Piano 2w', 121, 1, 1, 'AC.PIANO', 'GM 005'),
  MIDIVoice('Piano 3', 121, 0, 2, 'AC.PIANO', 'GM 006'),
  MIDIVoice('Piano 3w', 121, 1, 2, 'AC.PIANO', 'GM 007'),
  MIDIVoice('Honky-tonk', 121, 0, 3, 'AC.PIANO', 'GM 008'),
  MIDIVoice('Honky-tonk 2', 121, 1, 3, 'AC.PIANO', 'GM 009'),
  MIDIVoice('E.Piano 1', 121, 0, 4, 'EL.PIANO', 'GM 010'),
  MIDIVoice('St.Soft EP', 121, 1, 4, 'EL.PIANO', 'GM 011'),
  MIDIVoice('FM+SA EP', 121, 2, 4, 'EL.PIANO', 'GM 012'),
  MIDIVoice('60\'s EP', 121, 3, 4, 'EL.PIANO', 'GM 013'),
  MIDIVoice('E.Piano 2', 121, 0, 5, 'EL.PIANO', 'GM 014'),
  MIDIVoice('Detuned EP 2', 121, 1, 5, 'EL.PIANO', 'GM 015'),
  MIDIVoice('St.FM EP', 121, 2, 5, 'EL.PIANO', 'GM 016'),
  MIDIVoice('EP Legend', 121, 3, 5, 'EL.PIANO', 'GM 017'),
  MIDIVoice('EP Phase', 121, 4, 5, 'EL.PIANO', 'GM 018'),
  MIDIVoice('Harpsichord', 121, 0, 6, 'KEYBOARDS', 'GM 019'),
  MIDIVoice('Coupled Hps.', 121, 1, 6, 'KEYBOARDS', 'GM 020'),
  MIDIVoice('Harpsi.w', 121, 2, 6, 'KEYBOARDS', 'GM 021'),
  MIDIVoice('Harpsi.o', 121, 3, 6, 'KEYBOARDS', 'GM 022'),
  MIDIVoice('Clav.', 121, 0, 7, 'KEYBOARDS', 'GM 023'),
  MIDIVoice('Pulse Clav', 121, 1, 7, 'KEYBOARDS', 'GM 024'),
  MIDIVoice('Celesta', 121, 0, 8, 'KEYBOARDS', 'GM 025'),
  MIDIVoice('Glockenspiel', 121, 0, 9, 'BELL', 'GM 026'),
  MIDIVoice('Music Box', 121, 0, 10, 'BELL', 'GM 027'),
  MIDIVoice('Vibraphone', 121, 0, 11, 'MALLET', 'GM 028'),
  MIDIVoice('Vibraphone w', 121, 1, 11, 'MALLET', 'GM 029'),
  MIDIVoice('Marimba', 121, 0, 12, 'MALLET', 'GM 030'),
  MIDIVoice('Marimba w', 121, 1, 12, 'MALLET', 'GM 031'),
  MIDIVoice('Xylophone', 121, 0, 13, 'MALLET', 'GM 032'),
  MIDIVoice('Tubular-bell', 121, 0, 14, 'BELL', 'GM 033'),
  MIDIVoice('Church Bell', 121, 1, 14, 'BELL', 'GM 034'),
  MIDIVoice('Carillon', 121, 2, 14, 'BELL', 'GM 035'),
  MIDIVoice('Santur', 121, 0, 15, 'PLUCKED', 'GM 036'),
  MIDIVoice('Organ 1', 121, 0, 16, 'ORGAN', 'GM 037'),
  MIDIVoice('Trem. Organ', 121, 1, 16, 'ORGAN', 'GM 038'),
  MIDIVoice('60\'s Organ 1', 121, 2, 16, 'ORGAN', 'GM 039'),
  MIDIVoice('70\'s E.Organ', 121, 3, 16, 'ORGAN', 'GM 040'),
  MIDIVoice('Organ 2', 121, 0, 17, 'ORGAN', 'GM 041'),
  MIDIVoice('Chorus Or.2', 121, 1, 17, 'ORGAN', 'GM 042'),
  MIDIVoice('Perc. Organ', 121, 2, 17, 'ORGAN', 'GM 043'),
  MIDIVoice('Organ 3', 121, 0, 18, 'ORGAN', 'GM 044'),
  MIDIVoice('Church Org.1', 121, 0, 19, 'ORGAN', 'GM 045'),
  MIDIVoice('Church Org.2', 121, 1, 19, 'ORGAN', 'GM 046'),
  MIDIVoice('Church Org.3', 121, 2, 19, 'ORGAN', 'GM 047'),
  MIDIVoice('Reed Organ', 121, 0, 20, 'ORGAN', 'GM 048'),
  MIDIVoice('Puff Organ', 121, 1, 20, 'ORGAN', 'GM 049'),
  MIDIVoice('Accordion Fr', 121, 0, 21, 'ACCORDION', 'GM 050'),
  MIDIVoice('Accordion It', 121, 1, 21, 'ACCORDION', 'GM 051'),
  MIDIVoice('HARMONICA', 121, 0, 22, 'HARMONICA', 'GM 052'),
  MIDIVoice('Bandoneon', 121, 0, 23, 'ACCORDION', 'GM 053'),
  MIDIVoice('Nylon-str.Gt', 121, 0, 24, 'AC.GUITAR', 'GM 054'),
  MIDIVoice('Ukulele', 121, 1, 24, 'AC.GUITAR', 'GM 055'),
  MIDIVoice('Nylon Gt.o', 121, 2, 24, 'AC.GUITAR', 'GM 056'),
  MIDIVoice('Nylon Gt.2', 121, 3, 24, 'AC.GUITAR', 'GM 057'),
  MIDIVoice('Steel-str.Gt', 121, 0, 25, 'AC.GUITAR', 'GM 058'),
  MIDIVoice('12-str.Gt', 121, 1, 25, 'AC.GUITAR', 'GM 059'),
  MIDIVoice('Mandolin', 121, 2, 25, 'AC.GUITAR', 'GM 060'),
  MIDIVoice('Steel + Body', 121, 3, 25, 'AC.GUITAR', 'GM 061'),
  MIDIVoice('Jazz Gt.', 121, 0, 26, 'EL.GUITAR', 'GM 062'),
  MIDIVoice('Pedal Steel', 121, 1, 26, 'EL.GUITAR', 'GM 063'),
  MIDIVoice('Clean Gt.', 121, 0, 27, 'EL.GUITAR', 'GM 064'),
  MIDIVoice('Chorus Gt.', 121, 1, 27, 'EL.GUITAR', 'GM 065'),
  MIDIVoice('Mid Tone GTR', 121, 2, 27, 'EL.GUITAR', 'GM 066'),
  MIDIVoice('Muted Gt.', 121, 0, 28, 'EL.GUITAR', 'GM 067'),
  MIDIVoice('Funk Pop', 121, 1, 28, 'EL.GUITAR', 'GM 068'),
  MIDIVoice('Funk Gt.2', 121, 2, 28, 'EL.GUITAR', 'GM 069'),
  MIDIVoice('Jazz Man', 121, 3, 28, 'EL.GUITAR', 'GM 070'),
  MIDIVoice('Overdrive Gt', 121, 0, 29, 'DIST.GUITAR', 'GM 071'),
  MIDIVoice('Guitar Pinch', 121, 1, 29, 'DIST.GUITAR', 'GM 072'),
  MIDIVoice('DistortionGt', 121, 0, 30, 'DIST.GUITAR', 'GM 073'),
  MIDIVoice('Feedback Gt.', 121, 1, 30, 'DIST.GUITAR', 'GM 074'),
  MIDIVoice('Dist Rtm GTR', 121, 2, 30, 'DIST.GUITAR', 'GM 075'),
  MIDIVoice('Gt.Harmonics', 121, 0, 31, 'EL.GUITAR', 'GM 076'),
  MIDIVoice('Gt. Feedback', 121, 1, 31, 'EL.GUITAR', 'GM 077'),
  MIDIVoice('Acoustic Bs.', 121, 0, 32, 'BASS', 'GM 078'),
  MIDIVoice('Fingered Bs.', 121, 0, 33, 'BASS', 'GM 079'),
  MIDIVoice('Finger Slap', 121, 1, 33, 'BASS', 'GM 080'),
  MIDIVoice('Picked Bass', 121, 0, 34, 'BASS', 'GM 081'),
  MIDIVoice('Fretless Bs.', 121, 0, 35, 'BASS', 'GM 082'),
  MIDIVoice('Slap Bass 1', 121, 0, 36, 'BASS', 'GM 083'),
  MIDIVoice('Slap Bass 2', 121, 0, 37, 'BASS', 'GM 084'),
  MIDIVoice('Synth Bass 1', 121, 0, 38, 'SYNTH BASS', 'GM 085'),
  MIDIVoice('SynthBass101', 121, 1, 38, 'SYNTH BASS', 'GM 086'),
  MIDIVoice('Acid Bass', 121, 2, 38, 'SYNTH BASS', 'GM 087'),
  MIDIVoice('Clavi Bass', 121, 3, 38, 'SYNTH BASS', 'GM 088'),
  MIDIVoice('Hammer', 121, 4, 38, 'SYNTH BASS', 'GM 089'),
  MIDIVoice('Synth Bass 2', 121, 0, 39, 'SYNTH BASS', 'GM 090'),
  MIDIVoice('Beef FM Bass', 121, 1, 39, 'SYNTH BASS', 'GM 091'),
  MIDIVoice('RubberBass 2', 121, 2, 39, 'SYNTH BASS', 'GM 092'),
  MIDIVoice('Attack Pulse', 121, 3, 39, 'SYNTH BASS', 'GM 093'),
  MIDIVoice('Violin', 121, 0, 40, 'STRINGS', 'GM 094'),
  MIDIVoice('Slow Violin', 121, 1, 40, 'STRINGS', 'GM 095'),
  MIDIVoice('Viola', 121, 0, 41, 'STRINGS', 'GM 096'),
  MIDIVoice('Cello', 121, 0, 42, 'STRINGS', 'GM 097'),
  MIDIVoice('Contrabass', 121, 0, 43, 'STRINGS', 'GM 098'),
  MIDIVoice('Tremolo Str', 121, 0, 44, 'STRINGS', 'GM 099'),
  MIDIVoice('PizzicatoStr', 121, 0, 45, 'STRINGS', 'GM 100'),
  MIDIVoice('Harp', 121, 0, 46, 'PLUCKED', 'GM 101'),
  MIDIVoice('Yang Qin', 121, 1, 46, 'PLUCKED', 'GM 102'),
  MIDIVoice('Timpani', 121, 0, 47, 'PERCUSSION', 'GM 103'),
  MIDIVoice('Orche str', 121, 0, 48, 'STRINGS', 'GM 104'),
  MIDIVoice('Orchestra', 121, 1, 48, 'STRINGS', 'GM 105'),
  MIDIVoice('60s Strings', 121, 2, 48, 'STRINGS', 'GM 106'),
  MIDIVoice('Slow Strings', 121, 0, 49, 'STRINGS', 'GM 107'),
  MIDIVoice('Syn.Strings1', 121, 0, 50, 'STRINGS', 'GM 108'),
  MIDIVoice('Syn.Strings3', 121, 1, 50, 'STRINGS', 'GM 109'),
  MIDIVoice('Syn.Strings2', 121, 0, 51, 'SOFT PAD', 'GM 110'),
  MIDIVoice('Choir Aahs', 121, 0, 52, 'VOX', 'GM 111'),
  MIDIVoice('Chorus Aahs', 121, 1, 52, 'VOX', 'GM 112'),
  MIDIVoice('Voice Oohs', 121, 0, 53, 'VOX', 'GM 113'),
  MIDIVoice('Humming', 121, 1, 53, 'VOX', 'GM 114'),
  MIDIVoice('SynVox', 121, 0, 54, 'VOX', 'GM 115'),
  MIDIVoice('Analog Voice', 121, 1, 54, 'VOX', 'GM 116'),
  MIDIVoice('OrchestraHit', 121, 0, 55, 'HIT&STAB', 'GM 117'),
  MIDIVoice('Bass Hit', 121, 1, 55, 'HIT&STAB', 'GM 118'),
  MIDIVoice('6th Hit', 121, 2, 55, 'HIT&STAB', 'GM 119'),
  MIDIVoice('Euro Hit', 121, 3, 55, 'HIT&STAB', 'GM 120'),
  MIDIVoice('Trumpet', 121, 0, 56, 'AC.BRASS', 'GM 121'),
  MIDIVoice('Dark Trumpet', 121, 1, 56, 'AC.BRASS', 'GM 122'),
  MIDIVoice('Trombone', 121, 0, 57, 'AC.BRASS', 'GM 123'),
  MIDIVoice('Trombone 2', 121, 1, 57, 'AC.BRASS', 'GM 124'),
  MIDIVoice('Bright Tb', 121, 2, 57, 'AC.BRASS', 'GM 125'),
  MIDIVoice('Tuba', 121, 0, 58, 'AC.BRASS', 'GM 126'),
  MIDIVoice('MutedTrumpet', 121, 0, 59, 'AC.BRASS', 'GM 127'),
  MIDIVoice('MuteTrumpet2', 121, 1, 59, 'AC.BRASS', 'GM 128'),
  MIDIVoice('French Horns', 121, 0, 60, 'AC.BRASS', 'GM 129'),
  MIDIVoice('Fr.Horn 2', 121, 1, 60, 'AC.BRASS', 'GM 130'),
  MIDIVoice('Brass 1', 121, 0, 61, 'AC.BRASS', 'GM 131'),
  MIDIVoice('Brass 2', 121, 1, 61, 'AC.BRASS', 'GM 132'),
  MIDIVoice('Synth Brass1', 121, 0, 62, 'SYNTH BRASS', 'GM 133'),
  MIDIVoice('Pro Brass', 121, 1, 62, 'SYNTH BRASS', 'GM 134'),
  MIDIVoice('Oct SynBrass', 121, 2, 62, 'SYNTH BRASS', 'GM 135'),
  MIDIVoice('Jump Brass', 121, 3, 62, 'SYNTH BRASS', 'GM 136'),
  MIDIVoice('Synth Brass2', 121, 0, 63, 'SYNTH BRASS', 'GM 137'),
  MIDIVoice('SynBrass sfz', 121, 1, 63, 'SYNTH BRASS', 'GM 138'),
  MIDIVoice('Velo Brass 1', 121, 2, 63, 'SYNTH BRASS', 'GM 139'),
  MIDIVoice('Soprano Sax', 121, 0, 64, 'SAX', 'GM 140'),
  MIDIVoice('Alto Sax', 121, 0, 65, 'SAX', 'GM 141'),
  MIDIVoice('Tenor Sax', 121, 0, 66, 'SAX', 'GM 142'),
  MIDIVoice('Baritone Sax', 121, 0, 67, 'SAX', 'GM 143'),
  MIDIVoice('Oboe', 121, 0, 68, 'WIND', 'GM 144'),
  MIDIVoice('English Horn', 121, 0, 69, 'WIND', 'GM 145'),
  MIDIVoice('Bassoon', 121, 0, 70, 'WIND', 'GM 146'),
  MIDIVoice('Clarinet', 121, 0, 71, 'WIND', 'GM 147'),
  MIDIVoice('Piccolo', 121, 0, 72, 'FLUTE', 'GM 148'),
  MIDIVoice('FLUTE', 121, 0, 73, 'FLUTE', 'GM 149'),
  MIDIVoice('Recorder', 121, 0, 74, 'FLUTE', 'GM 150'),
  MIDIVoice('Pan Flute', 121, 0, 75, 'FLUTE', 'GM 151'),
  MIDIVoice('Bottle Blow', 121, 0, 76, 'FLUTE', 'GM 152'),
  MIDIVoice('Shakuhachi', 121, 0, 77, 'ETHNIC', 'GM 153'),
  MIDIVoice('Whistle', 121, 0, 78, 'FLUTE', 'GM 154'),
  MIDIVoice('Ocarina', 121, 0, 79, 'FLUTE', 'GM 155'),
  MIDIVoice('Square Wave', 121, 0, 80, 'HARD LEAD', 'GM 156'),
  MIDIVoice('MG Square', 121, 1, 80, 'HARD LEAD', 'GM 157'),
  MIDIVoice('2600 Sine', 121, 2, 80, 'HARD LEAD', 'GM 158'),
  MIDIVoice('Saw Wave', 121, 0, 81, 'HARD LEAD', 'GM 159'),
  MIDIVoice('OB2 Saw', 121, 1, 81, 'HARD LEAD', 'GM 160'),
  MIDIVoice('Doctor Solo', 121, 2, 81, 'HARD LEAD', 'GM 161'),
  MIDIVoice('Natural Lead', 121, 3, 81, 'HARD LEAD', 'GM 162'),
  MIDIVoice('SequencedSaw', 121, 4, 81, 'HARD LEAD', 'GM 163'),
  MIDIVoice('Syn.Calliope', 121, 0, 82, 'SOFT LEAD', 'GM 164'),
  MIDIVoice('Chiffer Lead', 121, 0, 83, 'SOFT LEAD', 'GM 165'),
  MIDIVoice('Charang', 121, 0, 84, 'HARD LEAD', 'GM 166'),
  MIDIVoice('Wire Lead', 121, 1, 84, 'HARD LEAD', 'GM 167'),
  MIDIVoice('Solo Vox', 121, 0, 85, 'SOFT LEAD', 'GM 168'),
  MIDIVoice('5th Saw Wave', 121, 0, 86, 'HARD LEAD', 'GM 169'),
  MIDIVoice('Bass & Lead', 121, 0, 87, 'HARD LEAD', 'GM 170'),
  MIDIVoice('Delayed Lead', 121, 1, 87, 'HARD LEAD', 'GM 171'),
  MIDIVoice('Fantasia', 121, 0, 88, 'OTHER SYNTH', 'GM 172'),
  MIDIVoice('Warm Pad', 121, 0, 89, 'SOFT PAD', 'GM 173'),
  MIDIVoice('Sine Pad', 121, 1, 89, 'SOFT PAD', 'GM 174'),
  MIDIVoice('Polysynth', 121, 0, 90, 'OTHER SYNTH', 'GM 175'),
  MIDIVoice('Space Voice', 121, 0, 91, 'VOX', 'GM 176'),
  MIDIVoice('Itopia', 121, 1, 91, 'VOX', 'GM 177'),
  MIDIVoice('Bowed Glass', 121, 0, 92, 'SOFT PAD', 'GM 178'),
  MIDIVoice('Metal Pad', 121, 0, 93, 'BRIGHT PAD', 'GM 179'),
  MIDIVoice('Halo Pad', 121, 0, 94, 'BRIGHT PAD', 'GM 180'),
  MIDIVoice('Sweep Pad', 121, 0, 95, 'SOFT PAD', 'GM 181'),
  MIDIVoice('Ice Rain', 121, 0, 96, 'OTHER SYNTH', 'GM 182'),
  MIDIVoice('Soundtrack', 121, 0, 97, 'SOFT PAD', 'GM 183'),
  MIDIVoice('Crystal', 121, 0, 98, 'BELL', 'GM 184'),
  MIDIVoice('Syn Mallet', 121, 1, 98, 'BELL', 'GM 185'),
  MIDIVoice('Atmosphere', 121, 0, 99, 'AC.GUITAR', 'GM 186'),
  MIDIVoice('Brightness', 121, 0, 100, 'OTHER SYNTH', 'GM 187'),
  MIDIVoice('Goblin', 121, 0, 101, 'PULSATING', 'GM 188'),
  MIDIVoice('Echo Drops', 121, 0, 102, 'BRIGHT PAD', 'GM 189'),
  MIDIVoice('Echo Bell', 121, 1, 102, 'BRIGHT PAD', 'GM 190'),
  MIDIVoice('Echo Pan', 121, 2, 102, 'BRIGHT PAD', 'GM 191'),
  MIDIVoice('Star Theme', 121, 0, 103, 'BRIGHT PAD', 'GM 192'),
  MIDIVoice('Sitar', 121, 0, 104, 'PLUCKED', 'GM 193'),
  MIDIVoice('Sitar 2', 121, 1, 104, 'PLUCKED', 'GM 194'),
  MIDIVoice('Banjo', 121, 0, 105, 'PLUCKED', 'GM 195'),
  MIDIVoice('Shamisen', 121, 0, 106, 'PLUCKED', 'GM 196'),
  MIDIVoice('Koto', 121, 0, 107, 'PLUCKED', 'GM 197'),
  MIDIVoice('Taisho Koto', 121, 1, 107, 'PLUCKED', 'GM 198'),
  MIDIVoice('Kalimba', 121, 0, 108, 'PLUCKED', 'GM 199'),
  MIDIVoice('Bagpipe', 121, 0, 109, 'ETHNIC', 'GM 200'),
  MIDIVoice('Fiddle', 121, 0, 110, 'STRINGS', 'GM 201'),
  MIDIVoice('Shanai', 121, 0, 111, 'ETHNIC', 'GM 202'),
  MIDIVoice('Tinkle Bell', 121, 0, 112, 'BELL', 'GM 203'),
  MIDIVoice('Agogo', 121, 0, 113, 'PERCUSSION', 'GM 204'),
  MIDIVoice('Steel Drums', 121, 0, 114, 'MALLET', 'GM 205'),
  MIDIVoice('Woodblock', 121, 0, 115, 'PERCUSSION', 'GM 206'),
  MIDIVoice('Castanets', 121, 1, 115, 'PERCUSSION', 'GM 207'),
  MIDIVoice('Taiko', 121, 0, 116, 'PERCUSSION', 'GM 208'),
  MIDIVoice('Concert BD', 121, 1, 116, 'PERCUSSION', 'GM 209'),
  MIDIVoice('Melo. Tom 1', 121, 0, 117, 'PERCUSSION', 'GM 210'),
  MIDIVoice('Melo. Tom 2', 121, 1, 117, 'PERCUSSION', 'GM 211'),
  MIDIVoice('Synth Drum', 121, 0, 118, 'PERCUSSION', 'GM 212'),
  MIDIVoice('808 Tom', 121, 1, 118, 'PERCUSSION', 'GM 213'),
  MIDIVoice('Elec Perc', 121, 1, 118, 'PERCUSSION', 'GM 214'),
  MIDIVoice('Reverse Cym.', 121, 0, 119, 'PERCUSSION', 'GM 215'),
  MIDIVoice('Gt.FretNoise', 121, 0, 120, 'AC.GUITAR', 'GM 216'),
  MIDIVoice('Gt.Cut Noise', 121, 1, 120, 'AC.GUITAR', 'GM 217'),
  MIDIVoice('String Slap', 121, 2, 120, 'AC.GUITAR', 'GM 218'),
  MIDIVoice('Breath Noise', 121, 0, 121, 'SYNTH FX', 'GM 219'),
  MIDIVoice('Fl.Key Click', 121, 1, 121, 'SYNTH FX', 'GM 220'),
  MIDIVoice('Seashore', 121, 0, 122, 'SOUND FX', 'GM 221'),
  MIDIVoice('Rain', 121, 1, 122, 'SOUND FX', 'GM 222'),
  MIDIVoice('Thunder', 121, 2, 122, 'SOUND FX', 'GM 223'),
  MIDIVoice('WIND', 121, 3, 122, 'SOUND FX', 'GM 224'),
  MIDIVoice('Stream', 121, 4, 122, 'SOUND FX', 'GM 225'),
  MIDIVoice('Bubble', 121, 5, 122, 'SOUND FX', 'GM 226'),
  MIDIVoice('Bird', 121, 0, 123, 'SOUND FX', 'GM 227'),
  MIDIVoice('Dog', 121, 1, 123, 'SOUND FX', 'GM 228'),
  MIDIVoice('Horse-Gallop', 121, 2, 123, 'SOUND FX', 'GM 229'),
  MIDIVoice('Bird 2', 121, 3, 123, 'SOUND FX', 'GM 230'),
  MIDIVoice('Telephone 1', 121, 0, 124, 'SOUND FX', 'GM 231'),
  MIDIVoice('Telephone 2', 121, 1, 124, 'SOUND FX', 'GM 232'),
  MIDIVoice('DoorCreaking', 121, 2, 124, 'SOUND FX', 'GM 233'),
  MIDIVoice('Door', 121, 3, 124, 'SOUND FX', 'GM 234'),
  MIDIVoice('Scratch', 121, 4, 124, 'SOUND FX', 'GM 235'),
  MIDIVoice('Wind Chimes', 121, 5, 124, 'SOUND FX', 'GM 236'),
  MIDIVoice('Helicopter', 121, 0, 125, 'SOUND FX', 'GM 237'),
  MIDIVoice('Car-Engine', 121, 1, 125, 'SOUND FX', 'GM 238'),
  MIDIVoice('Car-Stop', 121, 2, 125, 'SOUND FX', 'GM 239'),
  MIDIVoice('Car-Pass', 121, 3, 125, 'SOUND FX', 'GM 240'),
  MIDIVoice('Car-Crash', 121, 4, 125, 'SOUND FX', 'GM 241'),
  MIDIVoice('Siren', 121, 5, 125, 'SOUND FX', 'GM 242'),
  MIDIVoice('Train', 121, 6, 125, 'SOUND FX', 'GM 243'),
  MIDIVoice('Jetplane', 121, 7, 125, 'SOUND FX', 'GM 244'),
  MIDIVoice('Starship', 121, 8, 125, 'SOUND FX', 'GM 245'),
  MIDIVoice('Burst Noise', 121, 9, 125, 'SOUND FX', 'GM 246'),
  MIDIVoice('Applause', 121, 0, 126, 'SOUND FX', 'GM 247'),
  MIDIVoice('Laughing', 121, 1, 126, 'SOUND FX', 'GM 248'),
  MIDIVoice('Screaming', 121, 2, 126, 'SOUND FX', 'GM 249'),
  MIDIVoice('Punch', 121, 3, 126, 'SOUND FX', 'GM 250'),
  MIDIVoice('Heart Beat', 121, 4, 126, 'SOUND FX', 'GM 251'),
  MIDIVoice('Footsteps', 121, 5, 126, 'SOUND FX', 'GM 252'),
  MIDIVoice('Gun Shot', 121, 0, 127, 'SOUND FX', 'GM 253'),
  MIDIVoice('Machine Gun', 121, 1, 127, 'SOUND FX', 'GM 254'),
  MIDIVoice('Lasergun', 121, 2, 127, 'SOUND FX', 'GM 255'),
  MIDIVoice('Explosion', 121, 3, 127, 'SOUND FX', 'GM 256'),
]
