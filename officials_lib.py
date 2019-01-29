#!/usr/bin/env python3
# encoding: utf-8

# pylint: disable=C0111

__updated__ = '2019-01-29 22:42:44'

import enum

import matplotlib.patches as mpatches


class FieldOrient(enum.Enum):
    LANDSCAPE = enum.auto()
    PORTRAIT = enum.auto()


class Field(object):
    def __init__(self, x=0, y=0, orient=FieldOrient.LANDSCAPE):
        # all length units are in `m`

        self.x = float(x)
        self.y = float(y)
        self.orient = FieldOrient[orient] if isinstance(orient, str) else FieldOrient(orient)

        self.width = 109.7
        self.height = 48.8
        self.runout = 4
        self.teamzone_distance = 4.57
        self.hashmark_distance = 12.2
        self.hashmark_sideline = 18.3
        self.hashmark_length = 0.6
        self.try_distance = 2.75
        self.pylon_distance = 2.75
        self.numbers_sideline = 8.2
        self.numbers_height = 1.8
        self.numbers_width = 1.2
        self.numbers_arrows_height = 0.45
        self.numbers_arrows_width = 0.9
        self.officials_zone_height = 2.0
        self.coaching_zone_height = 2.0
        self.line = 0.1

    def render(self):
        patches = []

        full_width = self.width + 2*self.runout
        full_height = self.height + 2*self.runout + self.teamzone_distance

        # background
        patches.append(mpatches.Rectangle((-(full_width)/2, -(full_height)/2), full_width, full_height, fc='green'))

        # endlines
        patches.append(
            mpatches.Rectangle(
                (-(self.width+self.line)/2, -(self.height+self.line)/2), self.line, self.height + self.line, fc='black'
            )
        )
        patches.append(
            mpatches.Rectangle(
                ((self.width+self.line)/2, -(self.height+self.line)/2), self.line, self.height + self.line, fc='black'
            )
        )

        # sidelines
        patches.append(
            mpatches.Rectangle(
                (-(self.width+self.line)/2, -(self.height+self.line)/2), self.width + self.line, self.line, fc='black'
            )
        )
        patches.append(
            mpatches.Rectangle(
                (-(self.width+self.line)/2, (self.height+self.line)/2), self.width + self.line, self.line, fc='black'
            )
        )

        return patches
