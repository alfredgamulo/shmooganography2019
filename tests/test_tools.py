#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Stéganô - Stéganô is a basic Python Steganography module.
# Copyright (C) 2010-2017  Cédric Bonhomme - https://www.cedricbonhomme.org
#
# For more information : https://github.com/cedricbonhomme/Stegano
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2017/02/22 $"
__revision__ = "$Date: 2017/02/22 $"
__license__ = "GPLv3"

import os
import unittest
import io

from stegano import tools

class TestTools(unittest.TestCase):

    def test_a2bits(self):
        bits = tools.a2bits("Hello World!")
        self.assertEqual(bits, '010010000110010101101100011011000110111100100000010101110110111101110010011011000110010000100001')

    def test_a2bits_list(self):
        list_of_bits = tools.a2bits_list("Hello World!")
        self.assertEqual(list_of_bits, ['01001000',
                                        '01100101',
                                        '01101100',
                                        '01101100',
                                        '01101111',
                                        '00100000',
                                        '01010111',
                                        '01101111',
                                        '01110010',
                                        '01101100',
                                        '01100100',
                                        '00100001'])

    def test_n_at_a_time(self):
        result = tools.n_at_a_time([1, 2, 3, 4, 5], 2, 'X')
        self.assertEqual(list(result), [(1, 2), (3, 4), (5, 'X')])

  		    