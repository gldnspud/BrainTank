#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
# Python AI Battle
#
# Copyright 2011 Matthew Thompson
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################

class Facing:
    '''Handles 4 way facing and conversion to vectors'''
    
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    
    facing_to_str = {
        0: 'UP',
        1: 'DOWN',
        2: 'LEFT',
        3: 'RIGHT'
    }

    def __init__(self, facing=0):
        self.value = facing
        
    def to_vector(self):
        if self.value == self.UP:
            return (0,-1)
        if self.value == self.DOWN:
            return (0,1)
        if self.value == self.LEFT:
            return (-1,0)            
        if self.value == self.RIGHT:
            return (1,0)
            

class Animation:
    '''Handle a linear animation of a given value.'''
    
    def __init__(self, start, stop, speed):
        self.start = start
        self.value = start
        self.stop = stop
        self.speed = speed
        self.done = False
        
    def unit(self):
        return self.value / (self.stop - self.start)
        
    def update(self, dt):
        if not self.done:
            self.value += self.speed * dt
            if self.value >= self.stop:
                self.done = True
                
    def __str__(self):
        return "Animation at %.2f of %.2f (+%.2f)" % (self.value, self.stop, self.speed)            
