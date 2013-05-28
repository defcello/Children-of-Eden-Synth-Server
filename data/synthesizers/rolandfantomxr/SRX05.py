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



NAME = 'XP-D - SRX-05 - Supreme Dance'

PATCHES = [
  MIDIVoice('SecretDancer', 93, 4, 0, 'BEAT&GROOVE', 'XP-D 001'),
  MIDIVoice('Mean Streets', 93, 4, 1, 'BEAT&GROOVE', 'XP-D 002'),
  MIDIVoice('E-tronic', 93, 4, 2, 'BEAT&GROOVE', 'XP-D 003'),
  MIDIVoice('License2chil', 93, 4, 3, 'BRIGHT PAD', 'XP-D 004'),
  MIDIVoice('Scratch Menu', 93, 4, 4, 'SOUND FX', 'XP-D 005'),
  MIDIVoice('Hit Specials', 93, 4, 5, 'HIT&STAB', 'XP-D 006'),
  MIDIVoice('Motivation', 93, 4, 6, 'STRINGS', 'XP-D 007'),
  MIDIVoice('Sine Vibrato', 93, 4, 7, 'SOFT LEAD', 'XP-D 008'),
  MIDIVoice('Acid Punch', 93, 4, 8, 'SYNTH BASS', 'XP-D 009'),
  MIDIVoice('E.Gtr Menu', 93, 4, 9, 'EL.GUITAR', 'XP-D 010'),
  MIDIVoice('Brite Flange', 93, 4, 10, 'BRIGHT PAD', 'XP-D 011'),
  MIDIVoice('Dance Vibes', 93, 4, 11, 'TECHNO SYNTH', 'XP-D 012'),
  MIDIVoice('N-Trance', 93, 4, 12, 'PULSATING', 'XP-D 013'),
  MIDIVoice('Phatt', 93, 4, 13, 'BEAT&GROOVE', 'XP-D 014'),
  MIDIVoice('DoubleDown', 93, 4, 14, 'BEAT&GROOVE', 'XP-D 015'),
  MIDIVoice('LoopFX Dark', 93, 4, 15, 'BEAT&GROOVE', 'XP-D 016'),
  MIDIVoice('Yo DJ', 93, 4, 16, 'BEAT&GROOVE', 'XP-D 017'),
  MIDIVoice('HH Piledrivr', 93, 4, 17, 'BEAT&GROOVE', 'XP-D 018'),
  MIDIVoice('Trush Head', 93, 4, 18, 'BEAT&GROOVE', 'XP-D 019'),
  MIDIVoice('Rap 21', 93, 4, 19, 'BEAT&GROOVE', 'XP-D 020'),
  MIDIVoice('Teknobeat', 93, 4, 20, 'BEAT&GROOVE', 'XP-D 021'),
  MIDIVoice('Filter Beat', 93, 4, 21, 'BEAT&GROOVE', 'XP-D 022'),
  MIDIVoice('FashionStyle', 93, 4, 22, 'BEAT&GROOVE', 'XP-D 023'),
  MIDIVoice('Strobobeat', 93, 4, 23, 'BEAT&GROOVE', 'XP-D 024'),
  MIDIVoice('SpaceGroove2', 93, 4, 24, 'BEAT&GROOVE', 'XP-D 025'),
  MIDIVoice('Underground', 93, 4, 25, 'BEAT&GROOVE', 'XP-D 026'),
  MIDIVoice('Extra Drive', 93, 4, 26, 'BEAT&GROOVE', 'XP-D 027'),
  MIDIVoice('NakedPrey', 93, 4, 27, 'BEAT&GROOVE', 'XP-D 028'),
  MIDIVoice('Mod It!', 93, 4, 28, 'BEAT&GROOVE', 'XP-D 029'),
  MIDIVoice('Broken\'Roll', 93, 4, 29, 'COMBINATION', 'XP-D 030'),
  MIDIVoice('Drew Groove', 93, 4, 30, 'COMBINATION', 'XP-D 031'),
  MIDIVoice('Beat Menu', 93, 4, 31, 'BEAT&GROOVE', 'XP-D 032'),
  MIDIVoice('Sinewave Bs', 93, 4, 32, 'SYNTH BASS', 'XP-D 033'),
  MIDIVoice('808 Bass', 93, 4, 33, 'SYNTH BASS', 'XP-D 034'),
  MIDIVoice('Low Bass 2', 93, 4, 34, 'SYNTH BASS', 'XP-D 035'),
  MIDIVoice('Low Bass 3', 93, 4, 35, 'SYNTH BASS', 'XP-D 036'),
  MIDIVoice('Low Bass 4', 93, 4, 36, 'SYNTH BASS', 'XP-D 037'),
  MIDIVoice('Hood Bass 2', 93, 4, 37, 'SYNTH BASS', 'XP-D 038'),
  MIDIVoice('Rubber Bs 21', 93, 4, 38, 'SYNTH BASS', 'XP-D 039'),
  MIDIVoice('Cheezee Bass', 93, 4, 39, 'SYNTH BASS', 'XP-D 040'),
  MIDIVoice('Bend Bs /sw', 93, 4, 40, 'SYNTH BASS', 'XP-D 041'),
  MIDIVoice('Saws Bass', 93, 4, 41, 'SYNTH BASS', 'XP-D 042'),
  MIDIVoice('Bass Kadett', 93, 4, 42, 'SYNTH BASS', 'XP-D 043'),
  MIDIVoice('Qube Bass', 93, 4, 43, 'SYNTH BASS', 'XP-D 044'),
  MIDIVoice('LegatoSynBs', 93, 4, 44, 'SYNTH BASS', 'XP-D 045'),
  MIDIVoice('15inch Bass', 93, 4, 45, 'SYNTH BASS', 'XP-D 046'),
  MIDIVoice('MG Filter Bs', 93, 4, 46, 'SYNTH BASS', 'XP-D 047'),
  MIDIVoice('Plk Bass', 93, 4, 47, 'SYNTH BASS', 'XP-D 048'),
  MIDIVoice('Flat SawBass', 93, 4, 48, 'SYNTH BASS', 'XP-D 049'),
  MIDIVoice('SH-101 Bass', 93, 4, 49, 'SYNTH BASS', 'XP-D 050'),
  MIDIVoice('Pulsing Bs', 93, 4, 50, 'SYNTH BASS', 'XP-D 051'),
  MIDIVoice('Arrpy', 93, 4, 51, 'SYNTH BASS', 'XP-D 052'),
  MIDIVoice('Acid Bass 2', 93, 4, 52, 'SYNTH BASS', 'XP-D 053'),
  MIDIVoice('Euro Bass 21', 93, 4, 53, 'SYNTH BASS', 'XP-D 054'),
  MIDIVoice('DarkEchoBass', 93, 4, 54, 'SYNTH BASS', 'XP-D 055'),
  MIDIVoice('UnisonSwBass', 93, 4, 55, 'SYNTH BASS', 'XP-D 056'),
  MIDIVoice('Dirty Bass', 93, 4, 56, 'SYNTH BASS', 'XP-D 057'),
  MIDIVoice('Comp NzBass', 93, 4, 57, 'SYNTH BASS', 'XP-D 058'),
  MIDIVoice('JunoDistBass', 93, 4, 58, 'SYNTH BASS', 'XP-D 059'),
  MIDIVoice('TB Dist Bs 1', 93, 4, 59, 'SYNTH BASS', 'XP-D 060'),
  MIDIVoice('TB Dist Bs 2', 93, 4, 60, 'SYNTH BASS', 'XP-D 061'),
  MIDIVoice('TB Dist Bs 3', 93, 4, 61, 'SYNTH BASS', 'XP-D 062'),
  MIDIVoice('Human Bass', 93, 4, 62, 'SYNTH BASS', 'XP-D 063'),
  MIDIVoice('Interferenz', 93, 4, 63, 'SYNTH BASS', 'XP-D 064'),
  MIDIVoice('16th SeqBass', 93, 4, 64, 'SYNTH BASS', 'XP-D 065'),
  MIDIVoice('Woofer Blow', 93, 4, 65, 'BASS', 'XP-D 066'),
  MIDIVoice('Guitaron Oct', 93, 4, 66, 'BASS', 'XP-D 067'),
  MIDIVoice('Finger Bass6', 93, 4, 67, 'BASS', 'XP-D 068'),
  MIDIVoice('Noisy P.Bass', 93, 4, 68, 'BASS', 'XP-D 069'),
  MIDIVoice('FeelBass', 93, 4, 69, 'BASS', 'XP-D 070'),
  MIDIVoice('Ethno Bass 3', 93, 4, 70, 'BASS', 'XP-D 071'),
  MIDIVoice('FAT Rave', 93, 4, 71, 'OTHER SYNTH', 'XP-D 072'),
  MIDIVoice('JUNO Rave', 93, 4, 72, 'OTHER SYNTH', 'XP-D 073'),
  MIDIVoice('4 x Saws', 93, 4, 73, 'OTHER SYNTH', 'XP-D 074'),
  MIDIVoice('Euro Saws', 93, 4, 74, 'OTHER SYNTH', 'XP-D 075'),
  MIDIVoice('Super Sawz', 93, 4, 75, 'OTHER SYNTH', 'XP-D 076'),
  MIDIVoice('Step Phaser', 93, 4, 76, 'OTHER SYNTH', 'XP-D 077'),
  MIDIVoice('Vade Retro', 93, 4, 77, 'OTHER SYNTH', 'XP-D 078'),
  MIDIVoice('Pulse Keys', 93, 4, 78, 'OTHER SYNTH', 'XP-D 079'),
  MIDIVoice('P5 Pluck', 93, 4, 79, 'OTHER SYNTH', 'XP-D 080'),
  MIDIVoice('Alpha Waves', 93, 4, 80, 'OTHER SYNTH', 'XP-D 081'),
  MIDIVoice('Andes', 93, 4, 81, 'OTHER SYNTH', 'XP-D 082'),
  MIDIVoice('Northern Pls', 93, 4, 82, 'OTHER SYNTH', 'XP-D 083'),
  MIDIVoice('R&B Pluck 2', 93, 4, 83, 'OTHER SYNTH', 'XP-D 084'),
  MIDIVoice('SynHarpsi', 93, 4, 84, 'OTHER SYNTH', 'XP-D 085'),
  MIDIVoice('Saw Wave HQ', 93, 4, 85, 'OTHER SYNTH', 'XP-D 086'),
  MIDIVoice('Sqr Wave HQ', 93, 4, 86, 'OTHER SYNTH', 'XP-D 087'),
  MIDIVoice('JU2 Wave 1', 93, 4, 87, 'OTHER SYNTH', 'XP-D 088'),
  MIDIVoice('JU2 Wave 2', 93, 4, 88, 'OTHER SYNTH', 'XP-D 089'),
  MIDIVoice('Pulse Wave 1', 93, 4, 89, 'OTHER SYNTH', 'XP-D 090'),
  MIDIVoice('Pulse Wave 2', 93, 4, 90, 'OTHER SYNTH', 'XP-D 091'),
  MIDIVoice('SpectrumWave', 93, 4, 91, 'OTHER SYNTH', 'XP-D 092'),
  MIDIVoice('Pure Sine 2', 93, 4, 92, 'OTHER SYNTH', 'XP-D 093'),
  MIDIVoice('Slippers', 93, 4, 93, 'OTHER SYNTH', 'XP-D 094'),
  MIDIVoice('Climb Maj7th', 93, 4, 94, 'OTHER SYNTH', 'XP-D 095'),
  MIDIVoice('Return2Minor', 93, 4, 95, 'OTHER SYNTH', 'XP-D 096'),
  MIDIVoice('FallingStar', 93, 4, 96, 'OTHER SYNTH', 'XP-D 097'),
  MIDIVoice('Convulsions', 93, 4, 97, 'PULSATING', 'XP-D 098'),
  MIDIVoice('CrazZzeee', 93, 4, 98, 'PULSATING', 'XP-D 099'),
  MIDIVoice('Creative', 93, 4, 99, 'PULSATING', 'XP-D 100'),
  MIDIVoice('Juno Slice', 93, 4, 100, 'PULSATING', 'XP-D 101'),
  MIDIVoice('Epic Slice', 93, 4, 101, 'PULSATING', 'XP-D 102'),
  MIDIVoice('Klang Werk', 93, 4, 102, 'PULSATING', 'XP-D 103'),
  MIDIVoice('Ouverture', 93, 4, 103, 'PULSATING', 'XP-D 104'),
  MIDIVoice('Tropic Slice', 93, 4, 104, 'PULSATING', 'XP-D 105'),
  MIDIVoice('Strained', 93, 4, 105, 'PULSATING', 'XP-D 106'),
  MIDIVoice('Wicked DJ 2', 93, 4, 106, 'PULSATING', 'XP-D 107'),
  MIDIVoice('Ultra Noise', 93, 4, 107, 'PULSATING', 'XP-D 108'),
  MIDIVoice('JunoArpeggio', 93, 4, 108, 'PULSATING', 'XP-D 109'),
  MIDIVoice('Autoarpeggio', 93, 4, 109, 'PULSATING', 'XP-D 110'),
  MIDIVoice('SeqOctarveEP', 93, 4, 110, 'PULSATING', 'XP-D 111'),
  MIDIVoice('Sync Vox', 93, 4, 111, 'PULSATING', 'XP-D 112'),
  MIDIVoice('Stack Clavi', 93, 4, 112, 'PULSATING', 'XP-D 113'),
  MIDIVoice('Pump up', 93, 4, 113, 'PULSATING', 'XP-D 114'),
  MIDIVoice('Sine Seq', 93, 4, 114, 'PULSATING', 'XP-D 115'),
  MIDIVoice('Seq Saws', 93, 4, 115, 'PULSATING', 'XP-D 116'),
  MIDIVoice('Finale Hit', 93, 4, 116, 'HIT&STAB', 'XP-D 117'),
  MIDIVoice('Big Hit 3', 93, 4, 117, 'HIT&STAB', 'XP-D 118'),
  MIDIVoice('AnswerMe!Hit', 93, 4, 118, 'HIT&STAB', 'XP-D 119'),
  MIDIVoice('LoungeLizard', 93, 4, 119, 'HIT&STAB', 'XP-D 120'),
  MIDIVoice('Disco Stabs', 93, 4, 120, 'HIT&STAB', 'XP-D 121'),
  MIDIVoice('12x12\'sDisco', 93, 4, 121, 'HIT&STAB', 'XP-D 122'),
  MIDIVoice('LittleDots', 93, 4, 122, 'HIT&STAB', 'XP-D 123'),
  MIDIVoice('TribalTechno', 93, 4, 123, 'HIT&STAB', 'XP-D 124'),
  MIDIVoice('Minor Bumwah', 93, 4, 124, 'HIT&STAB', 'XP-D 125'),
  MIDIVoice('Bobs Slide', 93, 4, 125, 'HIT&STAB', 'XP-D 126'),
  MIDIVoice('BrassHit 1', 93, 4, 126, 'HIT&STAB', 'XP-D 127'),
  MIDIVoice('BrassHit 2', 93, 4, 127, 'HIT&STAB', 'XP-D 128'),
  MIDIVoice('BrassHit 3', 93, 5, 0, 'HIT&STAB', 'XP-D 129'),
  MIDIVoice('BrassHit 4', 93, 5, 1, 'HIT&STAB', 'XP-D 130'),
  MIDIVoice('BrassHit 5', 93, 5, 2, 'HIT&STAB', 'XP-D 131'),
  MIDIVoice('BrassHit 6', 93, 5, 3, 'HIT&STAB', 'XP-D 132'),
  MIDIVoice('BrassHit 7', 93, 5, 4, 'HIT&STAB', 'XP-D 133'),
  MIDIVoice('SymphHit 1', 93, 5, 5, 'HIT&STAB', 'XP-D 134'),
  MIDIVoice('SymphHit 2', 93, 5, 6, 'HIT&STAB', 'XP-D 135'),
  MIDIVoice('SymphHit 3', 93, 5, 7, 'HIT&STAB', 'XP-D 136'),
  MIDIVoice('OrgTrnsplnt', 93, 5, 8, 'HIT&STAB', 'XP-D 137'),
  MIDIVoice('Organ Hit 3', 93, 5, 9, 'HIT&STAB', 'XP-D 138'),
  MIDIVoice('Organ Hit 4', 93, 5, 10, 'HIT&STAB', 'XP-D 139'),
  MIDIVoice('Chord Hit 1', 93, 5, 11, 'HIT&STAB', 'XP-D 140'),
  MIDIVoice('Chord Hit 2', 93, 5, 12, 'HIT&STAB', 'XP-D 141'),
  MIDIVoice('Chord Hit 3', 93, 5, 13, 'HIT&STAB', 'XP-D 142'),
  MIDIVoice('Chord Hit 4', 93, 5, 14, 'HIT&STAB', 'XP-D 143'),
  MIDIVoice('Crystal Hit', 93, 5, 15, 'HIT&STAB', 'XP-D 144'),
  MIDIVoice('Stamp Hit', 93, 5, 16, 'HIT&STAB', 'XP-D 145'),
  MIDIVoice('ThousandHit', 93, 5, 17, 'HIT&STAB', 'XP-D 146'),
  MIDIVoice('9th Hit', 93, 5, 18, 'HIT&STAB', 'XP-D 147'),
  MIDIVoice('Slap Hit 1', 93, 5, 19, 'HIT&STAB', 'XP-D 148'),
  MIDIVoice('Slap Hit 2', 93, 5, 20, 'HIT&STAB', 'XP-D 149'),
  MIDIVoice('Dust Hit', 93, 5, 21, 'HIT&STAB', 'XP-D 150'),
  MIDIVoice('Dist Hit 1', 93, 5, 22, 'HIT&STAB', 'XP-D 151'),
  MIDIVoice('Dist Hit 2', 93, 5, 23, 'HIT&STAB', 'XP-D 152'),
  MIDIVoice('Wah Hit', 93, 5, 24, 'HIT&STAB', 'XP-D 153'),
  MIDIVoice('Tremble Hit', 93, 5, 25, 'HIT&STAB', 'XP-D 154'),
  MIDIVoice('Dah Hit', 93, 5, 26, 'HIT&STAB', 'XP-D 155'),
  MIDIVoice('Pretty Hit', 93, 5, 27, 'HIT&STAB', 'XP-D 156'),
  MIDIVoice('Smoky Hit', 93, 5, 28, 'HIT&STAB', 'XP-D 157'),
  MIDIVoice('Fist Hit', 93, 5, 29, 'HIT&STAB', 'XP-D 158'),
  MIDIVoice('Clavy Hit', 93, 5, 30, 'HIT&STAB', 'XP-D 159'),
  MIDIVoice('Tread Hit', 93, 5, 31, 'HIT&STAB', 'XP-D 160'),
  MIDIVoice('Old Org Hit', 93, 5, 32, 'HIT&STAB', 'XP-D 161'),
  MIDIVoice('Cave Hit', 93, 5, 33, 'HIT&STAB', 'XP-D 162'),
  MIDIVoice('Thru Hit', 93, 5, 34, 'HIT&STAB', 'XP-D 163'),
  MIDIVoice('Mull Hit', 93, 5, 35, 'HIT&STAB', 'XP-D 164'),
  MIDIVoice('Electronica', 93, 5, 36, 'HIT&STAB', 'XP-D 165'),
  MIDIVoice('Ripper', 93, 5, 37, 'HIT&STAB', 'XP-D 166'),
  MIDIVoice('Bounce Hit1', 93, 5, 38, 'HIT&STAB', 'XP-D 167'),
  MIDIVoice('Bounce Hit2', 93, 5, 39, 'HIT&STAB', 'XP-D 168'),
  MIDIVoice('Hit OneShots', 93, 5, 40, 'HIT&STAB', 'XP-D 169'),
  MIDIVoice('Brass Stab', 93, 5, 41, 'TECHNO SYNTH', 'XP-D 170'),
  MIDIVoice('Null Zone', 93, 5, 42, 'TECHNO SYNTH', 'XP-D 171'),
  MIDIVoice('Loop Techno', 93, 5, 43, 'TECHNO SYNTH', 'XP-D 172'),
  MIDIVoice('Tribal RaveX', 93, 5, 44, 'TECHNO SYNTH', 'XP-D 173'),
  MIDIVoice('Raverlisious', 93, 5, 45, 'TECHNO SYNTH', 'XP-D 174'),
  MIDIVoice('2FingerRifff', 93, 5, 46, 'TECHNO SYNTH', 'XP-D 175'),
  MIDIVoice('UK Garage 01', 93, 5, 47, 'TECHNO SYNTH', 'XP-D 176'),
  MIDIVoice('UKgarage2002', 93, 5, 48, 'TECHNO SYNTH', 'XP-D 177'),
  MIDIVoice('XV-303', 93, 5, 49, 'TECHNO SYNTH', 'XP-D 178'),
  MIDIVoice('Psy-Tron', 93, 5, 50, 'TECHNO SYNTH', 'XP-D 179'),
  MIDIVoice('House128bpm', 93, 5, 51, 'TECHNO SYNTH', 'XP-D 180'),
  MIDIVoice('NewAcid Line', 93, 5, 52, 'TECHNO SYNTH', 'XP-D 181'),
  MIDIVoice('Raver Saws', 93, 5, 53, 'TECHNO SYNTH', 'XP-D 182'),
  MIDIVoice('Dist Saws', 93, 5, 54, 'TECHNO SYNTH', 'XP-D 183'),
  MIDIVoice('BoosterBips2', 93, 5, 55, 'TECHNO SYNTH', 'XP-D 184'),
  MIDIVoice('Auto 101', 93, 5, 56, 'TECHNO SYNTH', 'XP-D 185'),
  MIDIVoice('BPF Sweep', 93, 5, 57, 'TECHNO SYNTH', 'XP-D 186'),
  MIDIVoice('Elektrico', 93, 5, 58, 'TECHNO SYNTH', 'XP-D 187'),
  MIDIVoice('What The ??', 93, 5, 59, 'TECHNO SYNTH', 'XP-D 188'),
  MIDIVoice('PlayEuroRiff', 93, 5, 60, 'TECHNO SYNTH', 'XP-D 189'),
  MIDIVoice('MayhemAppegi', 93, 5, 61, 'TECHNO SYNTH', 'XP-D 190'),
  MIDIVoice('AmbientTranz', 93, 5, 62, 'TECHNO SYNTH', 'XP-D 191'),
  MIDIVoice('DanceStrSect', 93, 5, 63, 'TECHNO SYNTH', 'XP-D 192'),
  MIDIVoice('5thIn4th Tri', 93, 5, 64, 'TECHNO SYNTH', 'XP-D 193'),
  MIDIVoice('5th Vox', 93, 5, 65, 'TECHNO SYNTH', 'XP-D 194'),
  MIDIVoice('Kompakt Voic', 93, 5, 66, 'TECHNO SYNTH', 'XP-D 195'),
  MIDIVoice('Resound', 93, 5, 67, 'TECHNO SYNTH', 'XP-D 196'),
  MIDIVoice('StrikeWhstle', 93, 5, 68, 'TECHNO SYNTH', 'XP-D 197'),
  MIDIVoice('Rocket Blast', 93, 5, 69, 'TECHNO SYNTH', 'XP-D 198'),
  MIDIVoice('Future Drain', 93, 5, 70, 'BRIGHT PAD', 'XP-D 199'),
  MIDIVoice('Foilage', 93, 5, 71, 'BRIGHT PAD', 'XP-D 200'),
  MIDIVoice('JP-8000 Pad', 93, 5, 72, 'BRIGHT PAD', 'XP-D 201'),
  MIDIVoice('SynthChord01', 93, 5, 73, 'BRIGHT PAD', 'XP-D 202'),
  MIDIVoice('PWM', 93, 5, 74, 'BRIGHT PAD', 'XP-D 203'),
  MIDIVoice('Introductory', 93, 5, 75, 'BRIGHT PAD', 'XP-D 204'),
  MIDIVoice('Miracle Pad', 93, 5, 76, 'BRIGHT PAD', 'XP-D 205'),
  MIDIVoice('5th Sweep 2', 93, 5, 77, 'BRIGHT PAD', 'XP-D 206'),
  MIDIVoice('Choir Sweep', 93, 5, 78, 'BRIGHT PAD', 'XP-D 207'),
  MIDIVoice('Retro Pad', 93, 5, 79, 'SOFT PAD', 'XP-D 208'),
  MIDIVoice('Beautiful:-]', 93, 5, 80, 'SOFT PAD', 'XP-D 209'),
  MIDIVoice('Steam Pad', 93, 5, 81, 'SOFT PAD', 'XP-D 210'),
  MIDIVoice('AggressiveLd', 93, 5, 82, 'HARD LEAD', 'XP-D 211'),
  MIDIVoice('I know Juno', 93, 5, 83, 'HARD LEAD', 'XP-D 212'),
  MIDIVoice('Def Lead 21', 93, 5, 84, 'HARD LEAD', 'XP-D 213'),
  MIDIVoice('HiPass', 93, 5, 85, 'HARD LEAD', 'XP-D 214'),
  MIDIVoice('DynaPulseLd', 93, 5, 86, 'HARD LEAD', 'XP-D 215'),
  MIDIVoice('Dist Lead', 93, 5, 87, 'HARD LEAD', 'XP-D 216'),
  MIDIVoice('80\'s Memory', 93, 5, 88, 'HARD LEAD', 'XP-D 217'),
  MIDIVoice('OD SyncLead', 93, 5, 89, 'HARD LEAD', 'XP-D 218'),
  MIDIVoice('80\'sTechLead', 93, 5, 90, 'HARD LEAD', 'XP-D 219'),
  MIDIVoice('3-SquareLead', 93, 5, 91, 'HARD LEAD', 'XP-D 220'),
  MIDIVoice('PortaSynLead', 93, 5, 92, 'SOFT LEAD', 'XP-D 221'),
  MIDIVoice('Tri Lead', 93, 5, 93, 'SOFT LEAD', 'XP-D 222'),
  MIDIVoice('Corrupt Sine', 93, 5, 94, 'SOFT LEAD', 'XP-D 223'),
  MIDIVoice('Neonlight', 93, 5, 95, 'SOFT LEAD', 'XP-D 224'),
  MIDIVoice('Higher&Highr', 93, 5, 96, 'SOFT LEAD', 'XP-D 225'),
  MIDIVoice('Waspy Solo1', 93, 5, 97, 'SOFT LEAD', 'XP-D 226'),
  MIDIVoice('Waspy Solo2', 93, 5, 98, 'SOFT LEAD', 'XP-D 227'),
  MIDIVoice('Vib Sine', 93, 5, 99, 'SOFT LEAD', 'XP-D 228'),
  MIDIVoice('Legato Saw', 93, 5, 100, 'SOFT LEAD', 'XP-D 229'),
  MIDIVoice('Wet Saw Ld', 93, 5, 101, 'SOFT LEAD', 'XP-D 230'),
  MIDIVoice('Dry BassLead', 93, 5, 102, 'SOFT LEAD', 'XP-D 231'),
  MIDIVoice('PluckLead', 93, 5, 103, 'SOFT LEAD', 'XP-D 232'),
  MIDIVoice('Comp Piano 2', 93, 5, 104, 'AC.PIANO', 'XP-D 233'),
  MIDIVoice('a Tack Piano', 93, 5, 105, 'AC.PIANO', 'XP-D 234'),
  MIDIVoice('Analog Piano', 93, 5, 106, 'AC.PIANO', 'XP-D 235'),
  MIDIVoice('Tri EP', 93, 5, 107, 'EL.PIANO', 'XP-D 236'),
  MIDIVoice('Pulsing EP', 93, 5, 108, 'EL.PIANO', 'XP-D 237'),
  MIDIVoice('Cool EP 2', 93, 5, 109, 'EL.PIANO', 'XP-D 238'),
  MIDIVoice('EP Chd Menu', 93, 5, 110, 'EL.PIANO', 'XP-D 239'),
  MIDIVoice('EP Maj 9th', 93, 5, 111, 'EL.PIANO', 'XP-D 240'),
  MIDIVoice('EP Maj 11th', 93, 5, 112, 'EL.PIANO', 'XP-D 241'),
  MIDIVoice('EP Min 11th', 93, 5, 113, 'EL.PIANO', 'XP-D 242'),
  MIDIVoice('NoisySynthEP', 93, 5, 114, 'EL.PIANO', 'XP-D 243'),
  MIDIVoice('CompClav/Rls', 93, 5, 115, 'KEYBOARDS', 'XP-D 244'),
  MIDIVoice('Comp Clavi', 93, 5, 116, 'KEYBOARDS', 'XP-D 245'),
  MIDIVoice('HarmoOrg/Mod', 93, 5, 117, 'ORGAN', 'XP-D 246'),
  MIDIVoice('ZigZag Organ', 93, 5, 118, 'ORGAN', 'XP-D 247'),
  MIDIVoice('Notre Organ', 93, 5, 119, 'ORGAN', 'XP-D 248'),
  MIDIVoice('SpectrumBell', 93, 5, 120, 'BELL', 'XP-D 249'),
  MIDIVoice('Square Bell1', 93, 5, 121, 'BELL', 'XP-D 250'),
  MIDIVoice('Square Bell2', 93, 5, 122, 'BELL', 'XP-D 251'),
  MIDIVoice('ClnGtr Slide', 93, 5, 123, 'EL.GUITAR', 'XP-D 252'),
  MIDIVoice('Gtr TrmDown', 93, 5, 124, 'EL.GUITAR', 'XP-D 253'),
  MIDIVoice('Waw Chord', 93, 5, 125, 'EL.GUITAR', 'XP-D 254'),
  MIDIVoice('Wha Wha Wha', 93, 5, 126, 'EL.GUITAR', 'XP-D 255'),
  MIDIVoice('Wha De Da', 93, 5, 127, 'EL.GUITAR', 'XP-D 256'),
  MIDIVoice('Fuzz Phaze', 93, 6, 0, 'DIST.GUITAR', 'XP-D 257'),
  MIDIVoice('Ringmod Ting', 93, 6, 1, 'DIST.GUITAR', 'XP-D 258'),
  MIDIVoice('BPF Strings', 93, 6, 2, 'STRINGS', 'XP-D 259'),
  MIDIVoice('LoFiStringz', 93, 6, 3, 'STRINGS', 'XP-D 260'),
  MIDIVoice('LightStrings', 93, 6, 4, 'STRINGS', 'XP-D 261'),
  MIDIVoice('Flange Str', 93, 6, 5, 'STRINGS', 'XP-D 262'),
  MIDIVoice('4th-LayerStr', 93, 6, 6, 'STRINGS', 'XP-D 263'),
  MIDIVoice('LA Pizz', 93, 6, 7, 'STRINGS', 'XP-D 264'),
  MIDIVoice('DanceClustor', 93, 6, 8, 'STRINGS', 'XP-D 265'),
  MIDIVoice('CaveStrHit', 93, 6, 9, 'STRINGS', 'XP-D 266'),
  MIDIVoice('StrChd Menu', 93, 6, 10, 'STRINGS', 'XP-D 267'),
  MIDIVoice('StrScaleMaj', 93, 6, 11, 'STRINGS', 'XP-D 268'),
  MIDIVoice('StrSpread', 93, 6, 12, 'STRINGS', 'XP-D 269'),
  MIDIVoice('EuroBeat Brs', 93, 6, 13, 'SYNTH BRASS', 'XP-D 270'),
  MIDIVoice('OB Brass 2', 93, 6, 14, 'SYNTH BRASS', 'XP-D 271'),
  MIDIVoice('Funny Brass', 93, 6, 15, 'SYNTH BRASS', 'XP-D 272'),
  MIDIVoice('Saws Brass', 93, 6, 16, 'SYNTH BRASS', 'XP-D 273'),
  MIDIVoice('AnalogMaster', 93, 6, 17, 'SYNTH BRASS', 'XP-D 274'),
  MIDIVoice('OneKeyMajor', 93, 6, 18, 'AC.BRASS', 'XP-D 275'),
  MIDIVoice('Danz Braz', 93, 6, 19, 'AC.BRASS', 'XP-D 276'),
  MIDIVoice('WindFX Menu', 93, 6, 20, 'WIND', 'XP-D 277'),
  MIDIVoice('Flute FX 1', 93, 6, 21, 'WIND', 'XP-D 278'),
  MIDIVoice('Flute FX 2', 93, 6, 22, 'WIND', 'XP-D 279'),
  MIDIVoice('Flute FX 3', 93, 6, 23, 'WIND', 'XP-D 280'),
  MIDIVoice('Sax FX 1', 93, 6, 24, 'WIND', 'XP-D 281'),
  MIDIVoice('Sax FX 2', 93, 6, 25, 'WIND', 'XP-D 282'),
  MIDIVoice('Sax FX 3', 93, 6, 26, 'WIND', 'XP-D 283'),
  MIDIVoice('VINYL VOX', 93, 6, 27, 'VOX', 'XP-D 284'),
  MIDIVoice('PsycheVocals', 93, 6, 28, 'VOX', 'XP-D 285'),
  MIDIVoice('Vox Menu', 93, 6, 29, 'VOX', 'XP-D 286'),
  MIDIVoice('Yeah F', 93, 6, 30, 'VOX', 'XP-D 287'),
  MIDIVoice('Ho F', 93, 6, 31, 'VOX', 'XP-D 288'),
  MIDIVoice('Oh F', 93, 6, 32, 'VOX', 'XP-D 289'),
  MIDIVoice('Wow Yeah F', 93, 6, 33, 'VOX', 'XP-D 290'),
  MIDIVoice('Ring Mod', 93, 6, 34, 'SYNTH FX', 'XP-D 291'),
  MIDIVoice('Hydrolyze', 93, 6, 35, 'SYNTH FX', 'XP-D 292'),
  MIDIVoice('Hydrolyze 2', 93, 6, 36, 'SYNTH FX', 'XP-D 293'),
  MIDIVoice('Danger Zone', 93, 6, 37, 'SYNTH FX', 'XP-D 294'),
  MIDIVoice('Danger Zone2', 93, 6, 38, 'SYNTH FX', 'XP-D 295'),
  MIDIVoice('Horror', 93, 6, 39, 'SYNTH FX', 'XP-D 296'),
  MIDIVoice('Space Scrach', 93, 6, 40, 'SYNTH FX', 'XP-D 297'),
  MIDIVoice('OldSkool FX', 93, 6, 41, 'SYNTH FX', 'XP-D 298'),
  MIDIVoice('Snare Bomb', 93, 6, 42, 'SYNTH FX', 'XP-D 299'),
  MIDIVoice('CymbalMusic', 93, 6, 43, 'SYNTH FX', 'XP-D 300'),
  MIDIVoice('Recollection', 93, 6, 44, 'SYNTH FX', 'XP-D 301'),
  MIDIVoice('Dive Start !', 93, 6, 45, 'SOUND FX', 'XP-D 302'),
  MIDIVoice('DJ Mayhem', 93, 6, 46, 'SOUND FX', 'XP-D 303'),
  MIDIVoice('TurnOff>Rev', 93, 6, 47, 'SOUND FX', 'XP-D 304'),
  MIDIVoice('Scratch 4', 93, 6, 48, 'SOUND FX', 'XP-D 305'),
  MIDIVoice('Scratch 5', 93, 6, 49, 'SOUND FX', 'XP-D 306'),
  MIDIVoice('Scratch 6', 93, 6, 50, 'SOUND FX', 'XP-D 307'),
  MIDIVoice('Scratch 7', 93, 6, 51, 'SOUND FX', 'XP-D 308'),
  MIDIVoice('Scratch 8', 93, 6, 52, 'SOUND FX', 'XP-D 309'),
  MIDIVoice('Scratch 9', 93, 6, 53, 'SOUND FX', 'XP-D 310'),
  MIDIVoice('Scratch 10', 93, 6, 54, 'SOUND FX', 'XP-D 311'),
  MIDIVoice('Vinyl Nz', 93, 6, 55, 'SOUND FX', 'XP-D 312'),
]
