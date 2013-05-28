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



NAME = 'XP-C - SRX-07 - Ultimate Keys'

PATCHES = [
  MIDIVoice('Stereo Piano', 93, 11, 0, 'AC.PIANO', 'XP-C 001'),
  MIDIVoice('Gran\'Piano', 93, 11, 1, 'AC.PIANO', 'XP-C 002'),
  MIDIVoice('Easy Rocker', 93, 11, 2, 'AC.PIANO', 'XP-C 003'),
  MIDIVoice('Stage Grand', 93, 11, 3, 'AC.PIANO', 'XP-C 004'),
  MIDIVoice('SA Rocker', 93, 11, 4, 'AC.PIANO', 'XP-C 005'),
  MIDIVoice('Padded Pno', 93, 11, 5, 'AC.PIANO', 'XP-C 006'),
  MIDIVoice('Suitcase EP', 93, 11, 6, 'EL.PIANO', 'XP-C 007'),
  MIDIVoice('Real Thing', 93, 11, 7, 'EL.PIANO', 'XP-C 008'),
  MIDIVoice('Fusiontastic', 93, 11, 8, 'EL.PIANO', 'XP-C 009'),
  MIDIVoice('Inspiration', 93, 11, 9, 'EL.PIANO', 'XP-C 010'),
  MIDIVoice('Touch EP SRX', 93, 11, 10, 'EL.PIANO', 'XP-C 011'),
  MIDIVoice('Stage73 SRX', 93, 11, 11, 'EL.PIANO', 'XP-C 012'),
  MIDIVoice('Stage EP 2', 93, 11, 12, 'EL.PIANO', 'XP-C 013'),
  MIDIVoice('BalladPanner', 93, 11, 13, 'EL.PIANO', 'XP-C 014'),
  MIDIVoice('80\'s EP', 93, 11, 14, 'EL.PIANO', 'XP-C 015'),
  MIDIVoice('SweetStagePN', 93, 11, 15, 'EL.PIANO', 'XP-C 016'),
  MIDIVoice('Padded EP', 93, 11, 16, 'EL.PIANO', 'XP-C 017'),
  MIDIVoice('Nursery Tine', 93, 11, 17, 'EL.PIANO', 'XP-C 018'),
  MIDIVoice('Sine EP', 93, 11, 18, 'EL.PIANO', 'XP-C 019'),
  MIDIVoice('70s Ballad', 93, 11, 19, 'EL.PIANO', 'XP-C 020'),
  MIDIVoice('Church Mouse', 93, 11, 20, 'EL.PIANO', 'XP-C 021'),
  MIDIVoice('ClaviQ EP', 93, 11, 21, 'EL.PIANO', 'XP-C 022'),
  MIDIVoice('FlaredTrouzr', 93, 11, 22, 'EL.PIANO', 'XP-C 023'),
  MIDIVoice('70\'EP Bs', 93, 11, 23, 'EL.PIANO', 'XP-C 024'),
  MIDIVoice('Swurly', 93, 11, 24, 'EL.PIANO', 'XP-C 025'),
  MIDIVoice('Dyno-Wurli', 93, 11, 25, 'EL.PIANO', 'XP-C 026'),
  MIDIVoice('60s Bros', 93, 11, 26, 'EL.PIANO', 'XP-C 027'),
  MIDIVoice('Pianohner', 93, 11, 27, 'EL.PIANO', 'XP-C 028'),
  MIDIVoice('Pianette 2K', 93, 11, 28, 'EL.PIANO', 'XP-C 029'),
  MIDIVoice('Cheapy Ep1', 93, 11, 29, 'EL.PIANO', 'XP-C 030'),
  MIDIVoice('Rox 668 St', 93, 11, 30, 'EL.PIANO', 'XP-C 031'),
  MIDIVoice('80\'s FM', 93, 11, 31, 'EL.PIANO', 'XP-C 032'),
  MIDIVoice('The 70\'EP', 93, 11, 32, 'EL.PIANO', 'XP-C 033'),
  MIDIVoice('Heavens Tine', 93, 11, 33, 'EL.PIANO', 'XP-C 034'),
  MIDIVoice('Sparkle EPno', 93, 11, 34, 'EL.PIANO', 'XP-C 035'),
  MIDIVoice('FirstDigital', 93, 11, 35, 'EL.PIANO', 'XP-C 036'),
  MIDIVoice('Vox Harpsi', 93, 11, 36, 'KEYBOARDS', 'XP-C 037'),
  MIDIVoice('Harpsiclav', 93, 11, 37, 'KEYBOARDS', 'XP-C 038'),
  MIDIVoice('E.Harpsi', 93, 11, 38, 'KEYBOARDS', 'XP-C 039'),
  MIDIVoice('Clav 1 SRX', 93, 11, 39, 'KEYBOARDS', 'XP-C 040'),
  MIDIVoice('Clav 2 SRX', 93, 11, 40, 'KEYBOARDS', 'XP-C 041'),
  MIDIVoice('VeloClav SRX', 93, 11, 41, 'KEYBOARDS', 'XP-C 042'),
  MIDIVoice('Clav 3 SRX', 93, 11, 42, 'KEYBOARDS', 'XP-C 043'),
  MIDIVoice('Generic Clav', 93, 11, 43, 'KEYBOARDS', 'XP-C 044'),
  MIDIVoice('Clav Pluck', 93, 11, 44, 'KEYBOARDS', 'XP-C 045'),
  MIDIVoice('Vintage Clav', 93, 11, 45, 'KEYBOARDS', 'XP-C 046'),
  MIDIVoice('Dyno Clav', 93, 11, 46, 'KEYBOARDS', 'XP-C 047'),
  MIDIVoice('PhaserClavi', 93, 11, 47, 'KEYBOARDS', 'XP-C 048'),
  MIDIVoice('CompClav SRX', 93, 11, 48, 'KEYBOARDS', 'XP-C 049'),
  MIDIVoice('MuteClv1 SRX', 93, 11, 49, 'KEYBOARDS', 'XP-C 050'),
  MIDIVoice('MuteClv2 SRX', 93, 11, 50, 'KEYBOARDS', 'XP-C 051'),
  MIDIVoice('Clav Supremo', 93, 11, 51, 'KEYBOARDS', 'XP-C 052'),
  MIDIVoice('Clav By III', 93, 11, 52, 'KEYBOARDS', 'XP-C 053'),
  MIDIVoice('Funk Synclav', 93, 11, 53, 'KEYBOARDS', 'XP-C 054'),
  MIDIVoice('Quacky Clav', 93, 11, 54, 'KEYBOARDS', 'XP-C 055'),
  MIDIVoice('GuitClav SRX', 93, 11, 55, 'KEYBOARDS', 'XP-C 056'),
  MIDIVoice('Juno Clavi', 93, 11, 56, 'KEYBOARDS', 'XP-C 057'),
  MIDIVoice('PhazynClvSRX', 93, 11, 57, 'KEYBOARDS', 'XP-C 058'),
  MIDIVoice('Moogy Pulse', 93, 11, 58, 'KEYBOARDS', 'XP-C 059'),
  MIDIVoice('JP8 Clav SRX', 93, 11, 59, 'KEYBOARDS', 'XP-C 060'),
  MIDIVoice('HyperClv SRX', 93, 11, 60, 'KEYBOARDS', 'XP-C 061'),
  MIDIVoice('Twinkle Bell', 93, 11, 61, 'BELL', 'XP-C 062'),
  MIDIVoice('Troika Ride', 93, 11, 62, 'BELL', 'XP-C 063'),
  MIDIVoice('Analog Bell', 93, 11, 63, 'BELL', 'XP-C 064'),
  MIDIVoice('Goodnite SRX', 93, 11, 64, 'BELL', 'XP-C 065'),
  MIDIVoice('2.2 SEQ SRX', 93, 11, 65, 'BELL', 'XP-C 066'),
  MIDIVoice('Vibraphone!', 93, 11, 66, 'MALLET', 'XP-C 067'),
  MIDIVoice('SA Vibe SRX', 93, 11, 67, 'MALLET', 'XP-C 068'),
  MIDIVoice('Blue B SRX', 93, 11, 68, 'ORGAN', 'XP-C 069'),
  MIDIVoice('FullPerc SRX', 93, 11, 69, 'ORGAN', 'XP-C 070'),
  MIDIVoice('NiceFeel SRX', 93, 11, 70, 'ORGAN', 'XP-C 071'),
  MIDIVoice('GreenB /Pdl', 93, 11, 71, 'ORGAN', 'XP-C 072'),
  MIDIVoice('Mello', 93, 11, 72, 'ORGAN', 'XP-C 073'),
  MIDIVoice('LA Blues SRX', 93, 11, 73, 'ORGAN', 'XP-C 074'),
  MIDIVoice('2BorNot2B3 2', 93, 11, 74, 'ORGAN', 'XP-C 075'),
  MIDIVoice('Gospel B SRX', 93, 11, 75, 'ORGAN', 'XP-C 076'),
  MIDIVoice('Bookin\'B SRX', 93, 11, 76, 'ORGAN', 'XP-C 077'),
  MIDIVoice('Hush B3 SRX', 93, 11, 77, 'ORGAN', 'XP-C 078'),
  MIDIVoice('Real Organ', 93, 11, 78, 'ORGAN', 'XP-C 079'),
  MIDIVoice('Tenamos L100', 93, 11, 79, 'ORGAN', 'XP-C 080'),
  MIDIVoice('Harm.Organ', 93, 11, 80, 'ORGAN', 'XP-C 081'),
  MIDIVoice('Harm.Organ2', 93, 11, 81, 'ORGAN', 'XP-C 082'),
  MIDIVoice('Power B SRX', 93, 11, 82, 'ORGAN', 'XP-C 083'),
  MIDIVoice('AllStarB3SRX', 93, 11, 83, 'ORGAN', 'XP-C 084'),
  MIDIVoice('GoodLord/Mod', 93, 11, 84, 'ORGAN', 'XP-C 085'),
  MIDIVoice('CabnetSeries', 93, 11, 85, 'ORGAN', 'XP-C 086'),
  MIDIVoice('Absolute B3', 93, 11, 86, 'ORGAN', 'XP-C 087'),
  MIDIVoice('Rox368-B/Mod', 93, 11, 87, 'ORGAN', 'XP-C 088'),
  MIDIVoice('Suitcase B3', 93, 11, 88, 'ORGAN', 'XP-C 089'),
  MIDIVoice('BalladB /Mod', 93, 11, 89, 'ORGAN', 'XP-C 090'),
  MIDIVoice('70\'sKeysMix', 93, 11, 90, 'ORGAN', 'XP-C 091'),
  MIDIVoice('Leslied B3', 93, 11, 91, 'ORGAN', 'XP-C 092'),
  MIDIVoice('Dyna Hammnd', 93, 11, 92, 'ORGAN', 'XP-C 093'),
  MIDIVoice('SaltyDog SRX', 93, 11, 93, 'ORGAN', 'XP-C 094'),
  MIDIVoice('Swt&Mllw SRX', 93, 11, 94, 'ORGAN', 'XP-C 095'),
  MIDIVoice('Mellow 4\'SRX', 93, 11, 95, 'ORGAN', 'XP-C 096'),
  MIDIVoice('ZomBee SRX', 93, 11, 96, 'ORGAN', 'XP-C 097'),
  MIDIVoice('Perky Twin B', 93, 11, 97, 'ORGAN', 'XP-C 098'),
  MIDIVoice('BluesPercSRX', 93, 11, 98, 'ORGAN', 'XP-C 099'),
  MIDIVoice('Club Organ', 93, 11, 99, 'ORGAN', 'XP-C 100'),
  MIDIVoice('888 +3rd SRX', 93, 11, 100, 'ORGAN', 'XP-C 101'),
  MIDIVoice('8888+3rd SRX', 93, 11, 101, 'ORGAN', 'XP-C 102'),
  MIDIVoice('Velo Perc', 93, 11, 102, 'ORGAN', 'XP-C 103'),
  MIDIVoice('Jazzy B', 93, 11, 103, 'ORGAN', 'XP-C 104'),
  MIDIVoice('Gutsy C3', 93, 11, 104, 'ORGAN', 'XP-C 105'),
  MIDIVoice('B3 888000004', 93, 11, 105, 'ORGAN', 'XP-C 106'),
  MIDIVoice('60s Brothers', 93, 11, 106, 'ORGAN', 'XP-C 107'),
  MIDIVoice('FirePerc SRX', 93, 11, 107, 'ORGAN', 'XP-C 108'),
  MIDIVoice('PercNorm3rd', 93, 11, 108, 'ORGAN', 'XP-C 109'),
  MIDIVoice('PercSoft3rd', 93, 11, 109, 'ORGAN', 'XP-C 110'),
  MIDIVoice('858808880SRX', 93, 11, 110, 'ORGAN', 'XP-C 111'),
  MIDIVoice('Mad Organ', 93, 11, 111, 'ORGAN', 'XP-C 112'),
  MIDIVoice('Touchy B Fst', 93, 11, 112, 'ORGAN', 'XP-C 113'),
  MIDIVoice('Souvenirs', 93, 11, 113, 'ORGAN', 'XP-C 114'),
  MIDIVoice('R&R B3 SRX', 93, 11, 114, 'ORGAN', 'XP-C 115'),
  MIDIVoice('B3Sermon SRX', 93, 11, 115, 'ORGAN', 'XP-C 116'),
  MIDIVoice('AllSkate!SRX', 93, 11, 116, 'ORGAN', 'XP-C 117'),
  MIDIVoice('BalladB3 SRX', 93, 11, 117, 'ORGAN', 'XP-C 118'),
  MIDIVoice('Ultimate B 4', 93, 11, 118, 'ORGAN', 'XP-C 119'),
  MIDIVoice('Purple SRX', 93, 11, 119, 'ORGAN', 'XP-C 120'),
  MIDIVoice('GimmeSomeSRX', 93, 11, 120, 'ORGAN', 'XP-C 121'),
  MIDIVoice('Smoked Water', 93, 11, 121, 'ORGAN', 'XP-C 122'),
  MIDIVoice('HardPerc3rd', 93, 11, 122, 'ORGAN', 'XP-C 123'),
  MIDIVoice('FuzzheadSRX', 93, 11, 123, 'ORGAN', 'XP-C 124'),
  MIDIVoice('Tron B', 93, 11, 124, 'ORGAN', 'XP-C 125'),
  MIDIVoice('ShimmerOrgan', 93, 11, 125, 'ORGAN', 'XP-C 126'),
  MIDIVoice('AnimalModSRX', 93, 11, 126, 'ORGAN', 'XP-C 127'),
  MIDIVoice('SurfMnkysSRX', 93, 11, 127, 'ORGAN', 'XP-C 128'),
  MIDIVoice('TelstarOrgan', 93, 12, 0, 'ORGAN', 'XP-C 129'),
  MIDIVoice('Continental', 93, 12, 1, 'ORGAN', 'XP-C 130'),
  MIDIVoice('Organfest\'66', 93, 12, 2, 'ORGAN', 'XP-C 131'),
  MIDIVoice('PalisadesSRX', 93, 12, 3, 'ORGAN', 'XP-C 132'),
  MIDIVoice('New Riders', 93, 12, 4, 'COMBINATION', 'XP-C 133'),
  MIDIVoice('The Sham SRX', 93, 12, 5, 'ORGAN', 'XP-C 134'),
  MIDIVoice('CrummyOrgSRX', 93, 12, 6, 'ORGAN', 'XP-C 135'),
  MIDIVoice('IronFarf SRX', 93, 12, 7, 'ORGAN', 'XP-C 136'),
  MIDIVoice('FarfComboSRX', 93, 12, 8, 'ORGAN', 'XP-C 137'),
  MIDIVoice('Farfisorium', 93, 12, 9, 'ORGAN', 'XP-C 138'),
  MIDIVoice('Farf 8\' + 2\'', 93, 12, 10, 'ORGAN', 'XP-C 139'),
  MIDIVoice('RoxOrgan SRX', 93, 12, 11, 'ORGAN', 'XP-C 140'),
  MIDIVoice('DittyDoo SRX', 93, 12, 12, 'ORGAN', 'XP-C 141'),
  MIDIVoice('Tranny Organ', 93, 12, 13, 'ORGAN', 'XP-C 142'),
  MIDIVoice('2.2 Organ', 93, 12, 14, 'ORGAN', 'XP-C 143'),
  MIDIVoice('VS Organ SRX', 93, 12, 15, 'ORGAN', 'XP-C 144'),
  MIDIVoice('D50 OrganSRX', 93, 12, 16, 'ORGAN', 'XP-C 145'),
  MIDIVoice('OrganbellSRX', 93, 12, 17, 'ORGAN', 'XP-C 146'),
  MIDIVoice('PhazedOrgSRX', 93, 12, 18, 'ORGAN', 'XP-C 147'),
  MIDIVoice('Das Limpet', 93, 12, 19, 'ORGAN', 'XP-C 148'),
  MIDIVoice('Spanish Gtr', 93, 12, 20, 'AC.GUITAR', 'XP-C 149'),
  MIDIVoice('Nylon SoSoft', 93, 12, 21, 'AC.GUITAR', 'XP-C 150'),
  MIDIVoice('Nylon on Pad', 93, 12, 22, 'AC.GUITAR', 'XP-C 151'),
  MIDIVoice('Moody Nylon', 93, 12, 23, 'AC.GUITAR', 'XP-C 152'),
  MIDIVoice('Conquest', 93, 12, 24, 'AC.GUITAR', 'XP-C 153'),
  MIDIVoice('Heaven Nylon', 93, 12, 25, 'AC.GUITAR', 'XP-C 154'),
  MIDIVoice('In Peace', 93, 12, 26, 'AC.GUITAR', 'XP-C 155'),
  MIDIVoice('NashvilleSRX', 93, 12, 27, 'EL.GUITAR', 'XP-C 156'),
  MIDIVoice('Caster Delay', 93, 12, 28, 'EL.GUITAR', 'XP-C 157'),
  MIDIVoice('Ricken12stGT', 93, 12, 29, 'EL.GUITAR', 'XP-C 158'),
  MIDIVoice('Narnia', 93, 12, 30, 'EL.GUITAR', 'XP-C 159'),
  MIDIVoice('Gtr PopArps', 93, 12, 31, 'EL.GUITAR', 'XP-C 160'),
  MIDIVoice('Touchy Mutes', 93, 12, 32, 'DIST.GUITAR', 'XP-C 161'),
  MIDIVoice('Disto-Chunky', 93, 12, 33, 'DIST.GUITAR', 'XP-C 162'),
  MIDIVoice('Rock Mute', 93, 12, 34, 'DIST.GUITAR', 'XP-C 163'),
  MIDIVoice('Telemaster', 93, 12, 35, 'DIST.GUITAR', 'XP-C 164'),
  MIDIVoice('Plugged!', 93, 12, 36, 'DIST.GUITAR', 'XP-C 165'),
  MIDIVoice('MutedDsBlief', 93, 12, 37, 'DIST.GUITAR', 'XP-C 166'),
  MIDIVoice('MM Bass /', 93, 12, 38, 'BASS', 'XP-C 167'),
  MIDIVoice('MMFatSlapSRX', 93, 12, 39, 'BASS', 'XP-C 168'),
  MIDIVoice('HyperFunkSRX', 93, 12, 40, 'BASS', 'XP-C 169'),
  MIDIVoice('MillerPopSRX', 93, 12, 41, 'BASS', 'XP-C 170'),
  MIDIVoice('Funk Bass', 93, 12, 42, 'BASS', 'XP-C 171'),
  MIDIVoice('Abe 4way SRX', 93, 12, 43, 'BASS', 'XP-C 172'),
  MIDIVoice('AL3way/NzSRX', 93, 12, 44, 'BASS', 'XP-C 173'),
  MIDIVoice('ALDarkSlpSRX', 93, 12, 45, 'BASS', 'XP-C 174'),
  MIDIVoice('John 4waySRX', 93, 12, 46, 'BASS', 'XP-C 175'),
  MIDIVoice('JPBritSlpSRX', 93, 12, 47, 'BASS', 'XP-C 176'),
  MIDIVoice('John w/NzSRX', 93, 12, 48, 'BASS', 'XP-C 177'),
  MIDIVoice('6strngBASS +', 93, 12, 49, 'BASS', 'XP-C 178'),
  MIDIVoice('Big Bad AL', 93, 12, 50, 'BASS', 'XP-C 179'),
  MIDIVoice('Comp 6tr Bas', 93, 12, 51, 'BASS', 'XP-C 180'),
  MIDIVoice('AbeLimitrSRX', 93, 12, 52, 'BASS', 'XP-C 181'),
  MIDIVoice('JP P.Bs 1SRX', 93, 12, 53, 'BASS', 'XP-C 182'),
  MIDIVoice('JP P.Bs 2SRX', 93, 12, 54, 'BASS', 'XP-C 183'),
  MIDIVoice('Abe\'sP.BsSRX', 93, 12, 55, 'BASS', 'XP-C 184'),
  MIDIVoice('AL Solid SRX', 93, 12, 56, 'BASS', 'XP-C 185'),
  MIDIVoice('AL2wayFngSRX', 93, 12, 57, 'BASS', 'XP-C 186'),
  MIDIVoice('AL SoftBs/Nz', 93, 12, 58, 'BASS', 'XP-C 187'),
  MIDIVoice('MarcusJB SRX', 93, 12, 59, 'BASS', 'XP-C 188'),
  MIDIVoice('MM JB SRX', 93, 12, 60, 'BASS', 'XP-C 189'),
  MIDIVoice('Pick UP SRX', 93, 12, 61, 'BASS', 'XP-C 190'),
  MIDIVoice('JP Rock SRX', 93, 12, 62, 'BASS', 'XP-C 191'),
  MIDIVoice('PickedJzBass', 93, 12, 63, 'BASS', 'XP-C 192'),
  MIDIVoice('BritePickSRX', 93, 12, 64, 'BASS', 'XP-C 193'),
  MIDIVoice('PhsrMute SRX', 93, 12, 65, 'BASS', 'XP-C 194'),
  MIDIVoice('DarkPick SRX', 93, 12, 66, 'BASS', 'XP-C 195'),
  MIDIVoice('Country Mute', 93, 12, 67, 'BASS', 'XP-C 196'),
  MIDIVoice('FretlessBASS', 93, 12, 68, 'BASS', 'XP-C 197'),
  MIDIVoice('SoloFls SRX', 93, 12, 69, 'BASS', 'XP-C 198'),
  MIDIVoice('JP6StrFlsSRX', 93, 12, 70, 'BASS', 'XP-C 199'),
  MIDIVoice('MM OctFlsSRX', 93, 12, 71, 'BASS', 'XP-C 200'),
  MIDIVoice('MMSmthFlsSRX', 93, 12, 72, 'BASS', 'XP-C 201'),
  MIDIVoice('ALFlsSoloSRX', 93, 12, 73, 'BASS', 'XP-C 202'),
  MIDIVoice('JPSoloFlsSRX', 93, 12, 74, 'BASS', 'XP-C 203'),
  MIDIVoice('Contrabbasso', 93, 12, 75, 'BASS', 'XP-C 204'),
  MIDIVoice('InYerFaceBas', 93, 12, 76, 'BASS', 'XP-C 205'),
  MIDIVoice('BriteUpright', 93, 12, 77, 'BASS', 'XP-C 206'),
  MIDIVoice('Uplectric', 93, 12, 78, 'BASS', 'XP-C 207'),
  MIDIVoice('JPSoftAB SRX', 93, 12, 79, 'BASS', 'XP-C 208'),
  MIDIVoice('JPHardAB SRX', 93, 12, 80, 'BASS', 'XP-C 209'),
  MIDIVoice('Dry AcB SRX', 93, 12, 81, 'BASS', 'XP-C 210'),
  MIDIVoice('WildThangSRX', 93, 12, 82, 'BASS', 'XP-C 211'),
  MIDIVoice('Dist Bs SRX', 93, 12, 83, 'BASS', 'XP-C 212'),
  MIDIVoice('StickyBs SRX', 93, 12, 84, 'BASS', 'XP-C 213'),
  MIDIVoice('FunkinWahSRX', 93, 12, 85, 'BASS', 'XP-C 214'),
  MIDIVoice('Harm A#9 SRX', 93, 12, 86, 'BASS', 'XP-C 215'),
  MIDIVoice('Harm E69 SRX', 93, 12, 87, 'BASS', 'XP-C 216'),
  MIDIVoice('SlidesNz SRX', 93, 12, 88, 'BASS', 'XP-C 217'),
  MIDIVoice('AllSlidesSRX', 93, 12, 89, 'BASS', 'XP-C 218'),
  MIDIVoice('AllNoisesSRX', 93, 12, 90, 'BASS', 'XP-C 219'),
  MIDIVoice('Ac.Bs Nz SRX', 93, 12, 91, 'BASS', 'XP-C 220'),
  MIDIVoice('WildSynth101', 93, 12, 92, 'SYNTH BASS', 'XP-C 221'),
  MIDIVoice('SH Dullbass', 93, 12, 93, 'SYNTH BASS', 'XP-C 222'),
  MIDIVoice('101 Bass', 93, 12, 94, 'SYNTH BASS', 'XP-C 223'),
  MIDIVoice('SH101 Bass', 93, 12, 95, 'SYNTH BASS', 'XP-C 224'),
  MIDIVoice('SH-2 Bs SRX', 93, 12, 96, 'SYNTH BASS', 'XP-C 225'),
  MIDIVoice('Bassic101SRX', 93, 12, 97, 'SYNTH BASS', 'XP-C 226'),
  MIDIVoice('Fat Butt', 93, 12, 98, 'SYNTH BASS', 'XP-C 227'),
  MIDIVoice('JP-4 Bs SRX', 93, 12, 99, 'SYNTH BASS', 'XP-C 228'),
  MIDIVoice('Systm700 SRX', 93, 12, 100, 'SYNTH BASS', 'XP-C 229'),
  MIDIVoice('BigSubBs SRX', 93, 12, 101, 'SYNTH BASS', 'XP-C 230'),
  MIDIVoice('TickerBs SRX', 93, 12, 102, 'SYNTH BASS', 'XP-C 231'),
  MIDIVoice('202 Bass', 93, 12, 103, 'SYNTH BASS', 'XP-C 232'),
  MIDIVoice('101ZapBs SRX', 93, 12, 104, 'SYNTH BASS', 'XP-C 233'),
  MIDIVoice('Housy Bass', 93, 12, 105, 'SYNTH BASS', 'XP-C 234'),
  MIDIVoice('HousineBsSRX', 93, 12, 106, 'SYNTH BASS', 'XP-C 235'),
  MIDIVoice('WooferBs SRX', 93, 12, 107, 'SYNTH BASS', 'XP-C 236'),
  MIDIVoice('System100SRX', 93, 12, 108, 'SYNTH BASS', 'XP-C 237'),
  MIDIVoice('Low Bass SRX', 93, 12, 109, 'SYNTH BASS', 'XP-C 238'),
  MIDIVoice('TB3O3 Reso', 93, 12, 110, 'SYNTH BASS', 'XP-C 239'),
  MIDIVoice('MeanderingBs', 93, 12, 111, 'SYNTH BASS', 'XP-C 240'),
  MIDIVoice('Acid TB Bs', 93, 12, 112, 'SYNTH BASS', 'XP-C 241'),
  MIDIVoice('MonsterMGSRX', 93, 12, 113, 'SYNTH BASS', 'XP-C 242'),
  MIDIVoice('Rogue Bs SRX', 93, 12, 114, 'SYNTH BASS', 'XP-C 243'),
  MIDIVoice('Classic Bs', 93, 12, 115, 'SYNTH BASS', 'XP-C 244'),
  MIDIVoice('Fat Bass', 93, 12, 116, 'SYNTH BASS', 'XP-C 245'),
  MIDIVoice('ResoMG BsSRX', 93, 12, 117, 'SYNTH BASS', 'XP-C 246'),
  MIDIVoice('MG Punchbass', 93, 12, 118, 'SYNTH BASS', 'XP-C 247'),
  MIDIVoice('Spike Bs SRX', 93, 12, 119, 'SYNTH BASS', 'XP-C 248'),
  MIDIVoice('WetMG Bs SRX', 93, 12, 120, 'SYNTH BASS', 'XP-C 249'),
  MIDIVoice('2-way Bass', 93, 12, 121, 'SYNTH BASS', 'XP-C 250'),
  MIDIVoice('Oct stinger', 93, 12, 122, 'SYNTH BASS', 'XP-C 251'),
  MIDIVoice('BsPedals SRX', 93, 12, 123, 'SYNTH BASS', 'XP-C 252'),
  MIDIVoice('MG PedalsSRX', 93, 12, 124, 'SYNTH BASS', 'XP-C 253'),
  MIDIVoice('OB Bass SRX', 93, 12, 125, 'SYNTH BASS', 'XP-C 254'),
  MIDIVoice('8VCO Mono', 93, 12, 126, 'SYNTH BASS', 'XP-C 255'),
  MIDIVoice('Thick OBass', 93, 12, 127, 'SYNTH BASS', 'XP-C 256'),
  MIDIVoice('The Synbass', 93, 13, 0, 'SYNTH BASS', 'XP-C 257'),
  MIDIVoice('Dark~~~~BASS', 93, 13, 1, 'SYNTH BASS', 'XP-C 258'),
  MIDIVoice('Valve5thBass', 93, 13, 2, 'SYNTH BASS', 'XP-C 259'),
  MIDIVoice('Rezidence', 93, 13, 3, 'SYNTH BASS', 'XP-C 260'),
  MIDIVoice('OrganSawBass', 93, 13, 4, 'SYNTH BASS', 'XP-C 261'),
  MIDIVoice('Organ Bass', 93, 13, 5, 'SYNTH BASS', 'XP-C 262'),
  MIDIVoice('SquareBs SRX', 93, 13, 6, 'SYNTH BASS', 'XP-C 263'),
  MIDIVoice('SlobbryBsSRX', 93, 13, 7, 'SYNTH BASS', 'XP-C 264'),
  MIDIVoice('Super Bs SRX', 93, 13, 8, 'SYNTH BASS', 'XP-C 265'),
  MIDIVoice('STronSTringz', 93, 13, 9, 'STRINGS', 'XP-C 266'),
  MIDIVoice('TrnStrDrySRX', 93, 13, 10, 'STRINGS', 'XP-C 267'),
  MIDIVoice('Tron Vls SRX', 93, 13, 11, 'STRINGS', 'XP-C 268'),
  MIDIVoice('MelloVlnsSRX', 93, 13, 12, 'STRINGS', 'XP-C 269'),
  MIDIVoice('JP8 Str1 SRX', 93, 13, 13, 'STRINGS', 'XP-C 270'),
  MIDIVoice('JP8 Str2 SRX', 93, 13, 14, 'STRINGS', 'XP-C 271'),
  MIDIVoice('JP+OB StrSRX', 93, 13, 15, 'STRINGS', 'XP-C 272'),
  MIDIVoice('M12 Strings', 93, 13, 16, 'STRINGS', 'XP-C 273'),
  MIDIVoice('Wavestr SRX', 93, 13, 17, 'STRINGS', 'XP-C 274'),
  MIDIVoice('MemoryMG SRX', 93, 13, 18, 'STRINGS', 'XP-C 275'),
  MIDIVoice('Solina SRX', 93, 13, 19, 'STRINGS', 'XP-C 276'),
  MIDIVoice('Omni Strings', 93, 13, 20, 'STRINGS', 'XP-C 277'),
  MIDIVoice('Big Str SRX', 93, 13, 21, 'STRINGS', 'XP-C 278'),
  MIDIVoice('Solo Flute', 93, 13, 22, 'FLUTE', 'XP-C 279'),
  MIDIVoice('TouchFlt SRX', 93, 13, 23, 'FLUTE', 'XP-C 280'),
  MIDIVoice('StrawberTRON', 93, 13, 24, 'FLUTE', 'XP-C 281'),
  MIDIVoice('Flute School', 93, 13, 25, 'FLUTE', 'XP-C 282'),
  MIDIVoice('Calli SRX', 93, 13, 26, 'FLUTE', 'XP-C 283'),
  MIDIVoice('TpSoloistSRX', 93, 13, 27, 'AC.BRASS', 'XP-C 284'),
  MIDIVoice('Pop Fanfare', 93, 13, 28, 'AC.BRASS', 'XP-C 285'),
  MIDIVoice('Oct Brass', 93, 13, 29, 'AC.BRASS', 'XP-C 286'),
  MIDIVoice('SessnBrs SRX', 93, 13, 30, 'AC.BRASS', 'XP-C 287'),
  MIDIVoice('R&R Bras SRX', 93, 13, 31, 'AC.BRASS', 'XP-C 288'),
  MIDIVoice('SuperTnr SRX', 93, 13, 32, 'SAX', 'XP-C 289'),
  MIDIVoice('T.Sax f SRX', 93, 13, 33, 'SAX', 'XP-C 290'),
  MIDIVoice('Cool Sax', 93, 13, 34, 'SAX', 'XP-C 291'),
  MIDIVoice('Duelin\' Saxs', 93, 13, 35, 'SAX', 'XP-C 292'),
  MIDIVoice('SoftSaxesSRX', 93, 13, 36, 'SAX', 'XP-C 293'),
  MIDIVoice('AmazngEchSRX', 93, 13, 37, 'SAX', 'XP-C 294'),
  MIDIVoice('FlaxOstinato', 93, 13, 38, 'WIND', 'XP-C 295'),
  MIDIVoice('2voiceLd SRX', 93, 13, 39, 'SOFT LEAD', 'XP-C 296'),
  MIDIVoice('Hollo Lead', 93, 13, 40, 'SOFT LEAD', 'XP-C 297'),
  MIDIVoice('Sinusolo SRX', 93, 13, 41, 'SOFT LEAD', 'XP-C 298'),
  MIDIVoice('Shmoog SRX', 93, 13, 42, 'SOFT LEAD', 'XP-C 299'),
  MIDIVoice('Sine', 93, 13, 43, 'SOFT LEAD', 'XP-C 300'),
  MIDIVoice('SH2000VoxSRX', 93, 13, 44, 'SOFT LEAD', 'XP-C 301'),
  MIDIVoice('FM Lead SRX', 93, 13, 45, 'SOFT LEAD', 'XP-C 302'),
  MIDIVoice('TrickTailEnd', 93, 13, 46, 'SOFT LEAD', 'XP-C 303'),
  MIDIVoice('4 Old Saws', 93, 13, 47, 'SOFT LEAD', 'XP-C 304'),
  MIDIVoice('Saw Bowed', 93, 13, 48, 'SOFT LEAD', 'XP-C 305'),
  MIDIVoice('VoxSaws Lead', 93, 13, 49, 'SOFT LEAD', 'XP-C 306'),
  MIDIVoice('GR500 Ld SRX', 93, 13, 50, 'SOFT LEAD', 'XP-C 307'),
  MIDIVoice('LimonaireSRX', 93, 13, 51, 'SOFT LEAD', 'XP-C 308'),
  MIDIVoice('NakdCheseSRX', 93, 13, 52, 'HARD LEAD', 'XP-C 309'),
  MIDIVoice('PromarsLdSRX', 93, 13, 53, 'HARD LEAD', 'XP-C 310'),
  MIDIVoice('Sweeze Lead', 93, 13, 54, 'HARD LEAD', 'XP-C 311'),
  MIDIVoice('Homey Lead', 93, 13, 55, 'HARD LEAD', 'XP-C 312'),
  MIDIVoice('MG Lead SRX', 93, 13, 56, 'HARD LEAD', 'XP-C 313'),
  MIDIVoice('Dreams Saw', 93, 13, 57, 'HARD LEAD', 'XP-C 314'),
  MIDIVoice('The Real Pat', 93, 13, 58, 'HARD LEAD', 'XP-C 315'),
  MIDIVoice('H 2 O', 93, 13, 59, 'HARD LEAD', 'XP-C 316'),
  MIDIVoice('PulseLd SRX', 93, 13, 60, 'HARD LEAD', 'XP-C 317'),
  MIDIVoice('Mono FM Lead', 93, 13, 61, 'HARD LEAD', 'XP-C 318'),
  MIDIVoice('VCO OctLdSRX', 93, 13, 62, 'HARD LEAD', 'XP-C 319'),
  MIDIVoice('Saws Lead', 93, 13, 63, 'HARD LEAD', 'XP-C 320'),
  MIDIVoice('Changes', 93, 13, 64, 'HARD LEAD', 'XP-C 321'),
  MIDIVoice('P5 Lead', 93, 13, 65, 'HARD LEAD', 'XP-C 322'),
  MIDIVoice('SH-2&5 Sqr', 93, 13, 66, 'HARD LEAD', 'XP-C 323'),
  MIDIVoice('Cutting Solo', 93, 13, 67, 'HARD LEAD', 'XP-C 324'),
  MIDIVoice('Racy Lead', 93, 13, 68, 'HARD LEAD', 'XP-C 325'),
  MIDIVoice('Speedometer', 93, 13, 69, 'HARD LEAD', 'XP-C 326'),
  MIDIVoice('Rotary Lead', 93, 13, 70, 'HARD LEAD', 'XP-C 327'),
  MIDIVoice('BuzzzzzzzSRX', 93, 13, 71, 'HARD LEAD', 'XP-C 328'),
  MIDIVoice('Telstar Lead', 93, 13, 72, 'HARD LEAD', 'XP-C 329'),
  MIDIVoice('Pattern It', 93, 13, 73, 'TECHNO SYNTH', 'XP-C 330'),
  MIDIVoice('Carbonite', 93, 13, 74, 'TECHNO SYNTH', 'XP-C 331'),
  MIDIVoice('The Pipe 5th', 93, 13, 75, 'TECHNO SYNTH', 'XP-C 332'),
  MIDIVoice('Buzzy Beez', 93, 13, 76, 'TECHNO SYNTH', 'XP-C 333'),
  MIDIVoice('Look Back', 93, 13, 77, 'TECHNO SYNTH', 'XP-C 334'),
  MIDIVoice('Razzert', 93, 13, 78, 'TECHNO SYNTH', 'XP-C 335'),
  MIDIVoice('Raveferenz', 93, 13, 79, 'TECHNO SYNTH', 'XP-C 336'),
  MIDIVoice('SupremeCheez', 93, 13, 80, 'TECHNO SYNTH', 'XP-C 337'),
  MIDIVoice('Exit', 93, 13, 81, 'TECHNO SYNTH', 'XP-C 338'),
  MIDIVoice('MousBoxesCat', 93, 13, 82, 'TECHNO SYNTH', 'XP-C 339'),
  MIDIVoice('Riff the 5th', 93, 13, 83, 'TECHNO SYNTH', 'XP-C 340'),
  MIDIVoice('Ice Man', 93, 13, 84, 'TECHNO SYNTH', 'XP-C 341'),
  MIDIVoice('DncStack1SRX', 93, 13, 85, 'TECHNO SYNTH', 'XP-C 342'),
  MIDIVoice('DncStack2SRX', 93, 13, 86, 'TECHNO SYNTH', 'XP-C 343'),
  MIDIVoice('DncStack3SRX', 93, 13, 87, 'TECHNO SYNTH', 'XP-C 344'),
  MIDIVoice('DncStack4SRX', 93, 13, 88, 'TECHNO SYNTH', 'XP-C 345'),
  MIDIVoice('DncStack5SRX', 93, 13, 89, 'TECHNO SYNTH', 'XP-C 346'),
  MIDIVoice('Euro BrsSRX', 93, 13, 90, 'TECHNO SYNTH', 'XP-C 347'),
  MIDIVoice('ThipsBlipSRX', 93, 13, 91, 'TECHNO SYNTH', 'XP-C 348'),
  MIDIVoice('FaveoravoSRX', 93, 13, 92, 'TECHNO SYNTH', 'XP-C 349'),
  MIDIVoice('Cleanse', 93, 13, 93, 'PULSATING', 'XP-C 350'),
  MIDIVoice('Mer', 93, 13, 94, 'PULSATING', 'XP-C 351'),
  MIDIVoice('B-lieve', 93, 13, 95, 'PULSATING', 'XP-C 352'),
  MIDIVoice('Blue Light', 93, 13, 96, 'PULSATING', 'XP-C 353'),
  MIDIVoice('Progress', 93, 13, 97, 'PULSATING', 'XP-C 354'),
  MIDIVoice('Modularswirl', 93, 13, 98, 'PULSATING', 'XP-C 355'),
  MIDIVoice('Sparkly', 93, 13, 99, 'PULSATING', 'XP-C 356'),
  MIDIVoice('Undertones', 93, 13, 100, 'PULSATING', 'XP-C 357'),
  MIDIVoice('HappyLFOsSRX', 93, 13, 101, 'PULSATING', 'XP-C 358'),
  MIDIVoice('AeroInsctSRX', 93, 13, 102, 'PULSATING', 'XP-C 359'),
  MIDIVoice('MC8 Seq SRX', 93, 13, 103, 'PULSATING', 'XP-C 360'),
  MIDIVoice('Legato Rip', 93, 13, 104, 'SYNTH FX', 'XP-C 361'),
  MIDIVoice('Steam Valve', 93, 13, 105, 'SYNTH FX', 'XP-C 362'),
  MIDIVoice('Scanner7', 93, 13, 106, 'SYNTH FX', 'XP-C 363'),
  MIDIVoice('Haunted Tron', 93, 13, 107, 'SYNTH FX', 'XP-C 364'),
  MIDIVoice('Experimental', 93, 13, 108, 'SYNTH FX', 'XP-C 365'),
  MIDIVoice('Megatron', 93, 13, 109, 'SYNTH FX', 'XP-C 366'),
  MIDIVoice('Outer Spaces', 93, 13, 110, 'SYNTH FX', 'XP-C 367'),
  MIDIVoice('Martian Bell', 93, 13, 111, 'SYNTH FX', 'XP-C 368'),
  MIDIVoice('Ethereal SRX', 93, 13, 112, 'SYNTH FX', 'XP-C 369'),
  MIDIVoice('Meow 5thsSRX', 93, 13, 113, 'SYNTH FX', 'XP-C 370'),
  MIDIVoice('MantrawavSRX', 93, 13, 114, 'SYNTH FX', 'XP-C 371'),
  MIDIVoice('RSS SpinnerS', 93, 13, 115, 'SYNTH FX', 'XP-C 372'),
  MIDIVoice('Comp Net SRX', 93, 13, 116, 'SYNTH FX', 'XP-C 373'),
  MIDIVoice('SpitBrs SRX', 93, 13, 117, 'SYNTH BRASS', 'XP-C 374'),
  MIDIVoice('Pro-10BrsSRX', 93, 13, 118, 'SYNTH BRASS', 'XP-C 375'),
  MIDIVoice('OBStabBrsSRX', 93, 13, 119, 'SYNTH BRASS', 'XP-C 376'),
  MIDIVoice('Pro-5 BrsSRX', 93, 13, 120, 'SYNTH BRASS', 'XP-C 377'),
  MIDIVoice('Quack BrsSRX', 93, 13, 121, 'SYNTH BRASS', 'XP-C 378'),
  MIDIVoice('M.MG Brs SRX', 93, 13, 122, 'SYNTH BRASS', 'XP-C 379'),
  MIDIVoice('FM Brs SRX', 93, 13, 123, 'SYNTH BRASS', 'XP-C 380'),
  MIDIVoice('D50Belpd1SRX', 93, 13, 124, 'OTHER SYNTH', 'XP-C 381'),
  MIDIVoice('D50Belpd2SRX', 93, 13, 125, 'OTHER SYNTH', 'XP-C 382'),
  MIDIVoice('D50Belpd3SRX', 93, 13, 126, 'OTHER SYNTH', 'XP-C 383'),
  MIDIVoice('KlmbSynthSRX', 93, 13, 127, 'OTHER SYNTH', 'XP-C 384'),
  MIDIVoice('B Higher', 93, 14, 0, 'OTHER SYNTH', 'XP-C 385'),
  MIDIVoice('Reflections', 93, 14, 1, 'OTHER SYNTH', 'XP-C 386'),
  MIDIVoice('VintagLayers', 93, 14, 2, 'OTHER SYNTH', 'XP-C 387'),
  MIDIVoice('HandleW/Care', 93, 14, 3, 'OTHER SYNTH', 'XP-C 388'),
  MIDIVoice('StaccHvn SRX', 93, 14, 4, 'OTHER SYNTH', 'XP-C 389'),
  MIDIVoice('TimefliesSRX', 93, 14, 5, 'OTHER SYNTH', 'XP-C 390'),
  MIDIVoice('JP6SqKeySRX', 93, 14, 6, 'OTHER SYNTH', 'XP-C 391'),
  MIDIVoice('CS Squared', 93, 14, 7, 'OTHER SYNTH', 'XP-C 392'),
  MIDIVoice('MawnlowerMan', 93, 14, 8, 'OTHER SYNTH', 'XP-C 393'),
  MIDIVoice('Glidiator', 93, 14, 9, 'OTHER SYNTH', 'XP-C 394'),
  MIDIVoice('Spit Synthie', 93, 14, 10, 'OTHER SYNTH', 'XP-C 395'),
  MIDIVoice('Raver One', 93, 14, 11, 'OTHER SYNTH', 'XP-C 396'),
  MIDIVoice('Slop-a-ramaS', 93, 14, 12, 'OTHER SYNTH', 'XP-C 397'),
  MIDIVoice('Big PWM SRX', 93, 14, 13, 'OTHER SYNTH', 'XP-C 398'),
  MIDIVoice('WavesyncSRX', 93, 14, 14, 'OTHER SYNTH', 'XP-C 399'),
  MIDIVoice('T8 Sync SRX', 93, 14, 15, 'OTHER SYNTH', 'XP-C 400'),
  MIDIVoice('SyncRush SRX', 93, 14, 16, 'OTHER SYNTH', 'XP-C 401'),
  MIDIVoice('DreaminOfJMJ', 93, 14, 17, 'OTHER SYNTH', 'XP-C 402'),
  MIDIVoice('Arp Saws SRX', 93, 14, 18, 'OTHER SYNTH', 'XP-C 403'),
  MIDIVoice('QuixelateSRX', 93, 14, 19, 'OTHER SYNTH', 'XP-C 404'),
  MIDIVoice('SpikedChzSRX', 93, 14, 20, 'OTHER SYNTH', 'XP-C 405'),
  MIDIVoice('Planet-S SRX', 93, 14, 21, 'OTHER SYNTH', 'XP-C 406'),
  MIDIVoice('Iceburg', 93, 14, 22, 'OTHER SYNTH', 'XP-C 407'),
  MIDIVoice('Old,Warm OBX', 93, 14, 23, 'OTHER SYNTH', 'XP-C 408'),
  MIDIVoice('Poly 3osc SH', 93, 14, 24, 'OTHER SYNTH', 'XP-C 409'),
  MIDIVoice('PortaSyn SRX', 93, 14, 25, 'OTHER SYNTH', 'XP-C 410'),
  MIDIVoice('RazrVCOs SRX', 93, 14, 26, 'OTHER SYNTH', 'XP-C 411'),
  MIDIVoice('Medusa SRX', 93, 14, 27, 'OTHER SYNTH', 'XP-C 412'),
  MIDIVoice('PhazeNRG SRX', 93, 14, 28, 'OTHER SYNTH', 'XP-C 413'),
  MIDIVoice('Build-Up SRX', 93, 14, 29, 'OTHER SYNTH', 'XP-C 414'),
  MIDIVoice('WavetableSRX', 93, 14, 30, 'OTHER SYNTH', 'XP-C 415'),
  MIDIVoice('DigiChoirSRX', 93, 14, 31, 'OTHER SYNTH', 'XP-C 416'),
  MIDIVoice('Rezidue SRX', 93, 14, 32, 'OTHER SYNTH', 'XP-C 417'),
  MIDIVoice('Combing SRX', 93, 14, 33, 'BRIGHT PAD', 'XP-C 418'),
  MIDIVoice('PhzslopadSRX', 93, 14, 34, 'BRIGHT PAD', 'XP-C 419'),
  MIDIVoice('OBThickPdSRX', 93, 14, 35, 'BRIGHT PAD', 'XP-C 420'),
  MIDIVoice('OBSftPad SRX', 93, 14, 36, 'SOFT PAD', 'XP-C 421'),
  MIDIVoice('RealStrSynth', 93, 14, 37, 'BRIGHT PAD', 'XP-C 422'),
  MIDIVoice('Rezonant Ens', 93, 14, 38, 'BRIGHT PAD', 'XP-C 423'),
  MIDIVoice('PG Phaser', 93, 14, 39, 'BRIGHT PAD', 'XP-C 424'),
  MIDIVoice('SynthOdyssey', 93, 14, 40, 'BRIGHT PAD', 'XP-C 425'),
  MIDIVoice('Liquid Lunch', 93, 14, 41, 'BRIGHT PAD', 'XP-C 426'),
  MIDIVoice('JP SquPadSRX', 93, 14, 42, 'SOFT PAD', 'XP-C 427'),
  MIDIVoice('Chewy Pad', 93, 14, 43, 'BRIGHT PAD', 'XP-C 428'),
  MIDIVoice('Hollow SRX', 93, 14, 44, 'SOFT PAD', 'XP-C 429'),
  MIDIVoice('Too Heaven', 93, 14, 45, 'SOFT PAD', 'XP-C 430'),
  MIDIVoice('Slow 3D Vox', 93, 14, 46, 'SOFT PAD', 'XP-C 431'),
  MIDIVoice('JP Spirit', 93, 14, 47, 'SOFT PAD', 'XP-C 432'),
  MIDIVoice('Classic OB', 93, 14, 48, 'SOFT PAD', 'XP-C 433'),
  MIDIVoice('Aulophony', 93, 14, 49, 'SOFT PAD', 'XP-C 434'),
  MIDIVoice('Dark Shadow', 93, 14, 50, 'SOFT PAD', 'XP-C 435'),
  MIDIVoice('Drawning Pad', 93, 14, 51, 'SOFT PAD', 'XP-C 436'),
  MIDIVoice('Sawed String', 93, 14, 52, 'SOFT PAD', 'XP-C 437'),
  MIDIVoice('R.I.P.', 93, 14, 53, 'SOFT PAD', 'XP-C 438'),
  MIDIVoice('K World', 93, 14, 54, 'SOFT PAD', 'XP-C 439'),
  MIDIVoice('CanyonDreams', 93, 14, 55, 'SOFT PAD', 'XP-C 440'),
  MIDIVoice('Mysterioso', 93, 14, 56, 'SOFT PAD', 'XP-C 441'),
  MIDIVoice('S/HTexturSRX', 93, 14, 57, 'SOFT PAD', 'XP-C 442'),
  MIDIVoice('VP-330ChrSRX', 93, 14, 58, 'VOX', 'XP-C 443'),
  MIDIVoice('Mellorkestra', 93, 14, 59, 'VOX', 'XP-C 444'),
  MIDIVoice('Tron Mass', 93, 14, 60, 'VOX', 'XP-C 445'),
  MIDIVoice('PreSampleVox', 93, 14, 61, 'VOX', 'XP-C 446'),
  MIDIVoice('Gamma Girls', 93, 14, 62, 'VOX', 'XP-C 447'),
  MIDIVoice('Lo-Tek Choir', 93, 14, 63, 'VOX', 'XP-C 448'),
  MIDIVoice('Tron Vox SRX', 93, 14, 64, 'VOX', 'XP-C 449'),
  MIDIVoice('Vox JX8P SRX', 93, 14, 65, 'VOX', 'XP-C 450'),
  MIDIVoice('VP303 Arpeg', 93, 14, 66, 'VOX', 'XP-C 451'),
  MIDIVoice('DrumLP DemoS', 93, 14, 67, 'COMBINATION', 'XP-C 452'),
  MIDIVoice('Pursuit 90 (90)', 93, 14, 68, 'BEAT&GROOVE', 'XP-C 453'),
  MIDIVoice('Arcade 132 (132)', 93, 14, 69, 'BEAT&GROOVE', 'XP-C 454'),
  MIDIVoice('SeventhHeavn (90)', 93, 14, 70, 'BEAT&GROOVE', 'XP-C 455'),
  MIDIVoice('TrollDrummin (60)', 93, 14, 71, 'BEAT&GROOVE', 'XP-C 456'),
  MIDIVoice('Chem Burn120 (120)', 93, 14, 72, 'BEAT&GROOVE', 'XP-C 457'),
  MIDIVoice('Rockshow 126 (126)', 93, 14, 73, 'BEAT&GROOVE', 'XP-C 458'),
  MIDIVoice('T-Pop 132 (132)', 93, 14, 74, 'BEAT&GROOVE', 'XP-C 459'),
  MIDIVoice('Valentine 76 (76)', 93, 14, 75, 'BEAT&GROOVE', 'XP-C 460'),
  MIDIVoice('Nocturne (112)', 93, 14, 76, 'BEAT&GROOVE', 'XP-C 461'),
  MIDIVoice('Cool At 102 (102)', 93, 14, 77, 'BEAT&GROOVE', 'XP-C 462'),
  MIDIVoice('Circuit 112 (112)', 93, 14, 78, 'BEAT&GROOVE', 'XP-C 463'),
  MIDIVoice('Hurt 90 (90)', 93, 14, 79, 'BEAT&GROOVE', 'XP-C 464'),
  MIDIVoice('Orleans 90 (90)', 93, 14, 80, 'BEAT&GROOVE', 'XP-C 465'),
  MIDIVoice('FunkyDrummer (120)', 93, 14, 81, 'BEAT&GROOVE', 'XP-C 466'),
  MIDIVoice('Circuit 90 (90)', 93, 14, 82, 'BEAT&GROOVE', 'XP-C 467'),
  MIDIVoice('SweepingLP S', 93, 14, 83, 'BEAT&GROOVE', 'XP-C 468'),
  MIDIVoice('Kick Menu', 93, 14, 84, 'DRUMS', 'XP-C 469'),
  MIDIVoice('Snare Menu 1', 93, 14, 85, 'DRUMS', 'XP-C 470'),
  MIDIVoice('Snare Menu 2', 93, 14, 86, 'DRUMS', 'XP-C 471'),
  MIDIVoice('Snare Menu 3', 93, 14, 87, 'DRUMS', 'XP-C 472'),
  MIDIVoice('Hi-Hat Menu', 93, 14, 88, 'DRUMS', 'XP-C 473'),
  MIDIVoice('Tom-Tom Menu', 93, 14, 89, 'DRUMS', 'XP-C 474'),
  MIDIVoice('Cymbals Menu', 93, 14, 90, 'DRUMS', 'XP-C 475'),
]
