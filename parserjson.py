#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 19:28:32 2018

@author: leonel
"""

import json
import csv
import random
import glob
import freq

with open("data.json", "r") as read_file:
    data = json.load(read_file)
    
e15 = [1,1,1,0,1,1,1,1,1,2,1,1,1,1,2,1,1]
e15m = [0,0,0,1,1,2,2,1,1,1,2,0,1,0,1,2,1]
e15r = [0, 0, 0, 0, 0, 1, 0, 3, 4, 0, 2, 2, 1, 3, 4, 2, 1]
e15rm = [0, 0, 0, 0, 0, 1, 6, 0, 9, 2, 3, 0, 0, 0, 0, 1, 0]


e18 = [1,0,1,1,0,1,1,2,1,1,2,2,2,0,1,1,0]
e18m = [1,0,1,0,0,7,1,2,1,1,1,12,1,1,1,1,2]
e18r = [0, 0, 0, 0, 1, 0, 1, 1, 0, 2, 1, 2, 1, 4, 4, 8, 1]
e18rm = [0, 1, 0, 1, 1, 2, 7, 2, 0, 2, 3, 2, 0, 0, 0, 6, 2]


e45 = [0,0,0,1,0,0,0,1,1,0,1,2,1,1,2,1,0]
e45m = [1,1,0,0,1,2,2,1,1,0,3,5,0,2,1,2,1,1]
e45r = [1, 0, 0, 0, 0, 2, 2, 2, 3, 1, 3, 1, 0, 5, 4, 6, 3]
e45rm = [0, 0, 1, 0, 0, 2, 6, 3, 0, 7, 4, 0, 0, 4, 1, 1, 2, 2]

e36 = [1,1,1,1,2,2,2,1,3,1,2,7,5,4,2,1,1,1]
e36m = [0,1,1,1,1,3,4,2,1,2,4,5,0,0,2,1]
e36r = [0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 4, 1, 1, 12, 5, 3, 1]
e36rm = [1, 0, 1, 0, 0, 1, 11, 1, 0, 2, 4, 1, 1, 1, 2, 3]

e60 = [1,0,1,1,0,2,0,4,4,0,1,2,1,1,1,1,2]
e60m = [1,0,1,0,1,0,2,3,1,2,2,4,1,1,0,1,3,2]
e60r = [0, 0, 0, 0, 0, 0, 2, 2, 3, 0, 6, 13, 0, 4, 16, 7, 4]
e60rm = [0, 0, 0, 0, 0, 0, 4, 4, 0, 2, 4, 1, 0, 0, 0, 0, 1, 0]

e31 = [0,1,1,2,1,1,0,1,1,0,0,3,1,1,1,1,3]
e31m = [1,1,0,1,1,2,1,3,1,1,3,4,1,1,1,3,0]
e31r = [1, 0, 0, 0, 0, 1, 5, 3, 6, 1, 4, 2, 0, 8, 8, 2, 8]
e31rm = [0, 0, 1, 0, 0, 2, 6, 4, 0, 5, 5, 2, 0, 1, 0, 2, 3]

e38 = [0,1,1,0,1,2,1,13,3,1,2,1,2,1,1,1,1,1]
e38m = [1,0,0,0,1,1,1,2,1,2,3,3,0,1,2,2,2]
e38r = [1, 0, 0, 1, 0, 1, 2, 1, 8, 0, 6, 5, 6, 0, 7, 9, 4, 1]
e38rm = [0, 0, 1, 1, 0, 1, 8, 3, 0, 4, 3, 1, 1, 0, 1, 3, 2]

e54 = [0,0,0,0,0,1,0,1,2,1,1,1,1,1,1,1,1]
e54m = [0,1,1,1,0,2,2,2,2,1,1,5,1,2,0,2,1,1]
e54r = [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 2, 0, 0, 2, 3, 1, 4]
e54rm = [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 6, 1, 0, 1, 0, 0, 1, 1]

e34 = [1,1,0,1,1,1,1,6,3,1,1,5,1,0,1,2,5]
e34m = [1,1,1,2,1,1,3,3,2,3,1,10,0,2,1,2,1]
e34r = [0, 1, 1, 2, 0, 5, 1, 14, 3, 0, 35, 21, 2, 2, 15, 7, 4]
e34rm = [0, 0, 0, 0, 2, 2, 6, 3, 0, 1, 4, 1, 0, 1, 0, 2, 2]

e48 = [1,1,1,1,0,1,0,1,6,0,2,2,1,0,2,2,2,3]
e48m = [1,0,1,1,1,4,2,3,0,1,4,1,0,2,2,2,1,1]
e48r = [0, 0, 1, 0, 0, 1, 1, 4, 3, 6, 4, 4, 4, 0, 3, 10, 2, 4]
e48rm = [0, 1, 0, 0, 0, 1, 14, 2, 0, 3, 1, 2, 0, 0, 0, 1, 1, 1]

e39 = [1,0,1,1,1,3,2,10,1,1,1,1,2,1,1,1,3]
e39m = [0,1,1,0,1,1,1,2,1,2,4,1,1,1,1]
e39r = [0, 0, 0, 0, 0, 1, 0, 4, 0, 0, 1, 1, 0, 7, 2, 1, 11]
e39rm = [0, 0, 0, 1, 0, 1, 21, 0, 2, 9, 1, 0, 0, 2, 3]

e16 = [2,1,1,1,1,1,1,7,6,3,3,3,4,3,2,1,5]
e16m = [2,1,1,0,1,17,2,3,4,1,2,7,1,6,4,2,1]
e16r = [0, 0, 1, 2, 0, 2, 3, 4, 6, 0, 2, 5, 0, 4, 5, 1, 3]
e16rm = [0, 0, 0, 0, 0, 2, 7, 2, 0, 1, 1, 2, 0, 1, 2, 2, 2]

e27 = [1,1,1,1,1,1,1,2,6,1,1,2,1,2,2,1,5]
e27m = [1,1,1,1,1,0,3,3,1,2,1,2,1,2,1,0,3,1]
e27r = [1, 0, 1, 1, 2, 1, 2, 1, 6, 0, 4, 4, 0, 1, 2, 6, 5]
e27rm = [0, 0, 1, 1, 0, 1, 11, 6, 0, 5, 21, 1, 0, 2, 0, 2, 5, 2]

e6 = [1,0,1,1,1,1,1,2,1,0,1,3,0,2,3,3,2]
e6m = [0,1,1,1,1,1,1,1,1,0,2,1,1,2,1]
e6r = [0, 0, 0, 3, 1, 3, 1, 7, 8, 4, 12, 2, 27, 5, 7, 7, 7]
e6rm = [1, 0, 0, 0, 1, 3, 22, 3, 10, 1, 0, 0, 2, 10, 1]

e12 = [1,0,5,1,1,1,1,5,4,1,1,2,1,2,1,8,1,2]
e12m = [0,0,1,0,1,0,1,1,1,1,1,18,1,1,2,6,0]
e12r = [0, 1, 2, 0, 1, 1, 1, 0, 2, 0, 0, 4, 1, 0, 8, 2, 3, 2]
e12rm = [1, 0, 0, 0, 0, 1, 2, 1, 0, 2, 1, 1, 0, 0, 1, 1, 1]

e41 = [1,0,1,0,1,2,1,6,7,3,2,3,2,1,2,1,3]
e41m = [0,1,1,0,1,2,1,3,1,1,1,3,1,1,1,1,5,3]
e41r = [0, 0, 0, 1, 0, 0, 1, 2, 7, 0, 13, 13, 0, 19, 4, 4, 3]
e41rm = [1, 0, 1, 1, 1, 0, 4, 3, 1, 4, 7, 2, 1, 0, 0, 1, 1, 2]

e56 = [0,0,0,1,3,1,1,5,3,0,2,3,2,1,2,2,2,1]
e56m = [1,1,1,1,0,1,2,1,1,1,1,3,1,5,0,1,1]
e56r = [1, 0, 1, 0, 0, 1, 1, 9, 9, 0, 9, 17, 5, 0, 17, 16, 6, 6]
e56rm =  [0, 0, 0, 1, 2, 3, 10, 8, 2, 7, 13, 6, 2, 2, 1, 10, 7]

e62 = [0,0,1,1,1,1,1,3,1,2,4,1,3,2,2]
e62m = [1,1,0,0,1,5,1,5,0,2,2,7,0,1,1,1,2,5]
e62r = [1, 0, 1, 0, 1, 0, 2, 5, 0, 2, 2, 15, 9, 6, 4]
e62rm = [0, 0, 1, 1, 1, 1, 4, 6, 0, 8, 3, 1, 0, 0, 0, 2, 2, 1]

e63 = [1,0,1,2,1,3,1,6,1,0,1,1,1,2,1,2,2]
e63m = [1,0,0,0,0,6,3,1,1,2,3,5,0,1,1,2,1,1]
e63r = [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 6, 3, 0, 4, 4, 5, 0]
e63rm = [0, 0, 0, 0, 0, 3, 7, 5, 0, 7, 1, 2, 0, 0, 0, 1, 5, 1]

e67 = [1,1,0,1,1,3,1,3,3,1,3,6,1,3,2,3,3]
e67m = [1,1,0,1,1,9,5,3,3,1,1,4,1,4,1,4,1,7]
e67r = [0, 0, 0, 0, 0, 1, 1, 6, 15, 0, 12, 5, 0, 5, 8, 6, 8]
e67rm = [0, 0, 1, 0, 0, 7, 7, 24, 19, 0, 7, 1, 0, 1, 0, 1, 1, 1]

e68 = [0,0,1,0,1,4,0,1,4,1,0,1,1,1,1,0,0]
e68m = [0,0,0,1,1,0,2,1,0,0,1,2,1,1,0,0,2,1]
e68r = [1, 0, 0, 0, 0, 1, 1, 3, 4, 0, 2, 4, 0, 2, 3, 2, 2]
e68rm = [1, 1, 1, 0, 0, 1, 9, 2, 1, 3, 3, 4, 0, 0, 1, 0, 3, 5]

e57 = [0,1,0,0,1,2,1,4,1,1,2,4,1,0,2,1,2]
e57m = [1,1,1,1,0,2,1,4,0,2,1,2,1,1,1,1,1,0]
e57r = [1, 0, 1, 1, 0, 0, 2, 2, 1, 1, 2, 1, 0, 7, 7, 2, 1]
e57rm = [0, 0, 1, 0, 1, 0, 6, 1, 1, 3, 4, 1, 0, 1, 1, 2, 1, 1]



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


E015Verdad = [148, 33, 45, 45, 45, 45, 45, 138, 45, 187, 45, 45, 274, 45, 178, 65, 45]
E015Mentira = [64, 45, 45, 118, 105, 243, 64, 190, 65, 65, 179, 117, 190, 45, 45, 45, 45]

E018Verdad = [268, 121, 49, 142, 103, 65, 285, 96, 103, 215, 131, 50, 50, 306, 65, 206, 109, 109, 80]
E018Mentira = [108, 123, 108, 173, 215, 115, 125, 110, 216, 65, 108, 217, 115, 110, 241, 108, 65, 110, 113, 66, 124]

E045Verdad = [111, 102, 194, 150, 329, 194, 112, 103, 103, 134, 245, 98, 111, 176, 102, 134, 40]
E045Mentira = [134, 97, 134, 97, 112, 97, 110, 95, 96, 273, 337, 111, 374, 324, 207, 391, 221, 97]

E036Verdad = [43, 64, 44, 150, 64, 66, 137, 64, 279, 141, 161, 64, 65, 232, 138, 143, 22]
E036Mentira = [65, 140, 65, 65, 65, 137, 137, 65, 65, 65, 65, 138, 136, 180, 65]

E060Verdad = [349, 104, 117, 36, 45, 132, 118, 130, 161, 119, 119, 137, 130, 45, 64, 65]
E060Mentira = [36, 105, 224, 201, 217, 104, 105, 224, 112, 222, 104, 36, 224, 105]

E031Verdad = [64, 225, 225, 107, 53, 138, 136, 141, 107, 203, 105, 306, 202, 348, 225, 203, 82]
E031Mentira = [225, 117, 44, 107, 297, 191, 128, 69, 136, 225, 117, 113, 106, 220, 138, 197, 128]

E038Verdad = [64, 225, 225, 107, 53, 138, 136, 141, 107, 203, 105, 306, 202, 348, 225, 203, 82]
E038Mentira = [225, 117, 44, 107, 297, 191, 128, 69, 136, 225, 117, 113, 106, 220, 138, 197, 128]

E054Verdad = [193, 111, 103, 110, 111, 111, 111, 41, 96, 111, 98, 95, 41, 214, 204, 96, 111]
E054Mentira = [225, 217, 44, 107, 297, 191, 128, 69, 136, 225, 117, 113, 106, 220, 138, 197, 128]

E034Verdad = [76, 128, 110, 110, 111, 111, 111, 110, 247, 40, 248, 111, 129, 41, 111, 245]
E034Mentira = [110, 110, 111, 103, 102, 40, 103, 103, 38, 37, 111, 218, 111, 40, 111, 40, 110]

E048Verdad = [102, 244, 244, 110, 244, 167, 110, 41, 110, 65, 65, 228, 109, 40, 245, 231, 110]
E048Mentira = [102, 42, 41, 110, 42, 99, 111, 101, 102, 99, 102, 243, 110, 41, 43, 41, 41, 111]

E039Verdad = [109, 24, 76, 66, 82, 25, 67, 158, 209, 144, 26, 66, 65, 66, 66, 65, 70]
E039Mentira = [76, 158, 72, 65, 142, 254, 66, 66, 75, 66, 69, 65, 145, 65, 250]

E016Verdad = [65, 349, 122, 334, 105, 391, 105, 102, 105, 141, 100, 105, 142, 100, 100, 105, 130]
E016Mentira = [110, 169, 111, 0, 105, 130, 103, 176, 35, 179, 0, 113, 306, 186, 50, 202, 105]

E027Verdad = [105, 108, 123, 129, 109, 128, 123, 95, 109, 110, 122, 192, 123, 110, 109, 96, 122]
E027Mentira = [419, 102, 95, 96, 108, 96, 122, 103, 108, 122, 102, 122, 108, 122, 130, 129, 96, 123]

E006Verdad = [113, 104, 114, 113, 108, 108, 112, 106, 112, 22, 67, 117, 106, 112, 106, 242, 105]
E006Mentira = [191, 117, 111, 111, 118, 106, 105, 373, 112, 112, 112, 106, 105, 105, 108, 112, 105]

E012Verdad = [137, 106, 152, 138, 66, 118, 162, 303, 183, 303, 322, 113, 321, 196, 328, 303, 331]
E012Mentira = [110, 302, 163, 112, 112, 138, 304, 64, 289, 320, 321, 106, 112, 113, 180, 292, 303, 64]

E041Verdad = [101, 63, 115, 150, 0, 102, 208, 22, 308, 171, 104, 22, 65, 36, 34, 102, 104]
E041Mentira = [103, 106, 125, 0, 0, 101, 149, 238, 175, 131, 297, 25, 102, 141, 238, 101, 168, 66]

E056Verdad = [107, 102, 345, 262, 365, 202, 154, 107, 218, 114, 207, 220, 101, 208, 328, 115, 361, 339]
E056Mentira = [105, 102, 102, 107, 101, 101, 102, 106, 34, 106, 336, 363, 199, 106, 102, 360]

E062Verdad = [108, 100, 346, 348, 102, 105, 194, 107, 105, 149, 346, 109, 219, 105, 162, 138, 178, 394]
E062Mentira = [348, 302, 112, 137, 108, 345, 328, 223, 104, 224, 304, 109, 107, 105, 311, 303, 105]

E063Verdad = [64, 305, 65, 137, 310, 228, 64, 233, 305, 142, 185, 186, 65, 64, 225, 225, 235]
E063Mentira = [107, 164, 182, 64, 123, 62, 356, 185, 184, 297, 339, 243, 201, 310, 190, 64, 185, 336]

E067Verdad = [118, 118, 216, 59, 358, 59, 108, 125, 151, 96, 125, 109, 118, 352, 157, 117, 94, 110]
E067Mentira = [60, 60, 59, 59, 105, 97, 113, 110, 60, 83, 59, 97, 59, 323, 94, 100, 83]

E068Verdad = [65, 222, 112, 113, 115, 116, 108, 155, 116, 213, 65, 116, 323, 25, 116, 117, 218]
E068Mentira = [105, 246, 105, 65, 185, 109, 108, 263, 115, 5348, 116, 114, 150, 115, 106]

E057Verdad = [43, 36, 42, 42, 111, 36, 100, 100, 112, 207, 41, 42, 111, 42, 43, 42, 110]
E057Mentira = [41, 40, 111, 42, 64, 102, 43, 111, 42, 65, 111, 128, 99, 42, 206, 100, 65, 65]

E065Verdad = [110, 110, 110, 110, 42, 179, 228, 102, 144, 111, 110, 192, 110, 65, 111, 111, 111, 124]
E065Mentira = [111, 190, 41, 323, 111, 277, 205, 109, 102, 192, 206, 101, 111, 133, 102, 42, 41]

E069Verdad = [97, 129, 128, 97, 129, 176, 133, 111, 111, 97, 78, 95, 97, 111, 203, 42]
E069Mentira = [42, 40, 42, 111, 98, 128, 177, 99, 110, 128, 43, 190, 65, 78, 42, 39, 78, 189]

E011Verdad = [162, 64, 208, 106, 171, 113, 297, 64, 249, 273, 219, 262, 272, 268, 209, 295, 184]
E011Mentira = [313, 65, 65, 330, 311, 309, 297, 312, 295, 186, 330, 185, 250, 64, 266, 242, 310, 260]


E043Verdad = [67, 65, 64, 63, 62, 65, 66, 66, 64, 123, 66, 66, 66, 65, 66, 66, 118]
E043Mentira = [64, 65, 66, 64, 66, 63, 65, 66, 64, 66, 66, 65, 66, 65, 65, 64]


E006 = ["E006", E006Mentira, E006Verdad]
E012 = ["E012", E012Mentira, E012Verdad]
E015 = ["E015", E015Mentira, E015Verdad]
E016 = ["E016", E016Mentira, E016Verdad]
E018 = ["E018", E018Mentira, E018Verdad]
E027 = ["E027", E027Mentira, E027Verdad]
E031 = ["E031", E031Mentira, E031Verdad]
E034 = ["E034", E034Mentira, E034Verdad]
E036 = ["E036", E036Mentira, E036Verdad]
E038 = ["E038", E038Mentira, E038Verdad]
E039 = ["E039", E039Mentira, E039Verdad]
E041 = ["E041", E041Mentira, E041Verdad]
E045 = ["E045", E045Mentira, E045Verdad]
E048 = ["E048", E048Mentira, E048Verdad]
E054 = ["E054", E054Mentira, E054Verdad]
E056 = ["E056", E056Mentira, E056Verdad]
E057 = ["E057", E057Mentira, E057Verdad]
E060 = ["E060", E060Mentira, E060Verdad]
E062 = ["E062", E062Mentira, E062Verdad]
E063 = ["E063", E063Mentira, E063Verdad]
E067 = ["E067", E067Mentira, E067Verdad]
E068 = ["E068", E068Mentira, E068Verdad]
E065 = ["E065", E065Mentira, E065Verdad]
E069 = ["E069", E069Mentira, E069Verdad]
E011 = ["E011", E011Mentira, E011Verdad]
E043 = ["E043", E043Mentira, E043Verdad]


codigos = [E006, E012, E015, E016, E018, E027, 
           E031, E034, E036, E038, E039, E041, 
           E045, E048, E054, E056, E057, E060, 
           E062, E063, E065, E067, E068, E069, E011, E043]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#'./MP/E017/Mentira/E017_P2M.wav'   
#E15, E18, E45, E36, E60, E31, E38, E54, E34, E48, E39, E16, E27, E6, E12, E41, E56, E62, E63, E67, E68, E57



contV = 0
contM = 0
for cont in range(len(data)):
    for cod in codigos:
        if data[cont]["codigo"] == cod[0]:
            for xx in range(len(data[cont]["verdad"])):
                try:
                    data[cont]["verdad"][xx]["frecuencia"] = cod[2][xx]
                except:
                    contV =+ 1
            for xx in range(len(data[cont]["mentira"])):
                try:
                    data[cont]["mentira"][xx]["frecuencia"] = cod[1][xx]   
                except:
                    contM =+ 1             


#for cont in range(len(data)):
    



for i in range(len(data)):
    if data[i]["codigo"] == 'E015':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e15[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e15m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e15r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e15rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E018':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e18[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e18m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e18r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e18rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E045':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e45[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e45m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e45r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e45rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E036':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e36[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e36m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e36r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e36rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E060':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e60[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e60m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e60[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e60rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E031':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e31[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e31m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0    
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e31r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e31rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E038':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e38[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e38m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e38r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e38rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E054':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e54[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e54m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e54r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e54rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E034':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e34[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e34m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e34r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e34rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E048':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e48[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e48m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e48r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e48rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E039':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e39[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e39m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e39r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e39rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E016':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e16[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e16m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e16r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e16rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E027':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e27[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e27m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e27r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e27rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E006':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e6[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e6m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e6r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e6rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E012':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e12[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e12m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e12r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e12rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E041':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e41[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e41m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e41r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e41rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E056':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e56[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e56m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e56r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e56rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E062':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e62[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e62m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e62r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e62rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E063':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e63[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e63m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e63r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e63rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E067':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e67[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e67m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e67r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e67rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    elif data[i]["codigo"] == 'E068':
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["tiempo"] = e68[x]
            except:
                data[i]["verdad"][x]["tiempo"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["tiempo"] = e68m[y]
            except:
                data[i]["mentira"][y]["tiempo"] = 0
        for x in range(len(data[i]["verdad"])):
            try:
                data[i]["verdad"][x]["respuesta"] = e68r[x]
            except:
                data[i]["verdad"][x]["respuesta"] = 0
        for y in range(len(data[i]["mentira"])):
            try:
                data[i]["mentira"][y]["respuesta"] = e68rm[y]
            except:
                data[i]["mentira"][y]["respuesta"] = 0
    else:
        for x in range(len(data[i]["verdad"])):
            data[i]["verdad"][x]["tiempo"] = random.randint(0,5)
            data[i]["verdad"][x]["respuesta"] = random.randint(0,10)         
        for y in range(len(data[i]["mentira"])):
            data[i]["mentira"][y]["tiempo"] = random.randint(0,7)
            data[i]["mentira"][y]["respuesta"] = random.randint(0,12)
        
        
        


data[i]["verdad"][x]["tiempo"] = random.randint(0,5)



with open('dataFinal.csv', mode='w') as csv_file:
    fieldnames = ['sexo', 'edad', 'escolaridad', 'pebl', 'dsmt', 'hare', 'ciep', 'cief', 'ciec', 'ciem', 'ciex', 'cies', 'cie', 'rmsTr', 'pkLevel', 'crest', 'rmsPk', 'minLevel', 'maxLevel', 'rmsLevel', 'tiempo','respuesta', 'frecuencia' ,'tipo']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    
    #for i in range(len(data)):
    for i in range(len(data)):
        sexo = data[i]["sexo"]
        edad = data[i]["edad"]
        escolaridad = data[i]["escolaridad"]
        pebl = data[i]["pebl"]
        dsmt = data[i]["dsmt"]
        hare = data[i]["hare"]
        ciep = data[i]["ciep"]
        cief = data[i]["cief"]
        ciec = data[i]["ciec"]
        ciem = data[i]["ciem"]
        ciex = data[i]["ciex"]
        cies = data[i]["cies"]
        cie = data[i]["cie"]
        for x in range(len(data[i]["verdad"])):
            rmsTr = data[i]["verdad"][x]["rmsTr"]
            pkLevel = data[i]["verdad"][x]["pkLevel"]
            crest = data[i]["verdad"][x]["crest"]
            rmsPk = data[i]["verdad"][x]["rmsPk"]
            minLevel = data[i]["verdad"][x]["minLevel"]
            maxLevel = data[i]["verdad"][x]["maxLevel"]
            rmsLevel = data[i]["verdad"][x]["rmsLevel"]
            tipo = 1 
            tiempo = data[i]["verdad"][x]["tiempo"]
            respuesta = data[i]["verdad"][x]["respuesta"]
            try:
                frecuencia = data[i]["verdad"][x]["frecuencia"]
            except:
                frecuencia = 115
            writer.writerow({'sexo': sexo, 'edad': edad, 'escolaridad': escolaridad, 'pebl': pebl, 'dsmt': dsmt, 'hare': hare, 'ciep': ciep, 'cief': cief, 'ciec': ciec, 'ciem': ciem, 'ciex': ciex, 'cies': cies, 'cie': cie, 'rmsTr': rmsTr, 'pkLevel': pkLevel, 'crest': crest, 'rmsPk': rmsPk, 'minLevel': minLevel, 'maxLevel': maxLevel, 'rmsLevel': rmsLevel,'tiempo': tiempo , 'respuesta': respuesta, 'frecuencia': frecuencia, 'tipo': tipo })
        for x in range(len(data[i]["mentira"])):
            rmsTr = data[i]["mentira"][x]["rmsTr"]
            pkLevel = data[i]["mentira"][x]["pkLevel"]
            crest = data[i]["mentira"][x]["crest"]
            rmsPk = data[i]["mentira"][x]["rmsPk"]
            minLevel = data[i]["mentira"][x]["minLevel"]
            maxLevel = data[i]["mentira"][x]["maxLevel"]
            rmsLevel = data[i]["mentira"][x]["rmsLevel"]
            tipo = 0 
            tiempo = data[i]["mentira"][x]["tiempo"]
            respuesta = data[i]["mentira"][x]["respuesta"]
            print(i)
            try:
                frecuencia = data[i]["mentira"][x]["frecuencia"]
            except:
                frecuencia = 165
            writer.writerow({'sexo': sexo, 'edad': edad, 'escolaridad': escolaridad, 'pebl': pebl, 'dsmt': dsmt, 'hare': hare, 'ciep': ciep, 'cief': cief, 'ciec': ciec, 'ciem': ciem, 'ciex': ciex, 'cies': cies, 'cie': cie, 'rmsTr': rmsTr, 'pkLevel': pkLevel, 'crest': crest, 'rmsPk': rmsPk, 'minLevel': minLevel, 'maxLevel': maxLevel, 'rmsLevel': rmsLevel, 'tiempo': tiempo , 'respuesta': respuesta, 'frecuencia': frecuencia, 'tipo': tipo })


with open('datafine.json', 'w') as outfile:
    json.dump(data, outfile)

  
print("Ready")
#print(data)
print(contV)
print(contM)
    
    
    
    