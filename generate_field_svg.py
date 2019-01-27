#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import math

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

__updated__ = '2017-07-17 14:29:23'

__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)


def main():
    fig = plt.figure(frameon=False, facecolor='white')
    ax = fig.add_axes([0, 0, 1.0, 1.0])
    ax.axis('off')

    fig.patch.set_facecolor('white')

    officiatingLineHome = 0.1
    officiatingLineAway = 0.9
    sidelineHome = 0.15
    sidelineAway = 0.85
    endlineA = 0.05
    goalineA = 0.125
    tenYardA = 0.2
    teamZoneA = 0.3125
    endlineB = 0.95
    goalineB = 0.875
    tenYardB = 0.8
    teamZoneB = 0.6875
    midfield = 0.5

    top = 1.0
    bottom = 0.0
    fieldSideHome = 0.0
    fieldSideAway = 1.0

    lw = 5.0
    numbersFontSize = 30

    fieldLength = endlineB - endlineA
    fieldWidth = sidelineAway - sidelineHome
    numbersLeft = sidelineHome + fieldWidth * 9.0 / 47.0
    hashLeft = numbersLeft + fieldWidth * 9.0 / 47.0
    hashRight = hashLeft + fieldWidth * 11.0 / 47.0
    numbersRight = hashRight + fieldWidth * 9.0 / 47.0

    rect = patches.Rectangle(
        (fieldSideHome, bottom), fieldSideAway, top, fc='white', ec='none'
    )
    ax.add_patch(rect)

    ax.plot(
        [sidelineHome, sidelineAway], [endlineA, endlineA],
        c='dimgray',
        lw=lw,
        zorder=15
    )
    ax.plot(
        [sidelineAway, sidelineHome], [endlineB, endlineB],
        c='dimgray',
        lw=lw,
        zorder=15
    )

    ax.plot(
        [officiatingLineHome, fieldSideHome], [teamZoneA, teamZoneA],
        c='dimgray',
        lw=lw,
        zorder=15
    )
    ax.plot(
        [officiatingLineHome, fieldSideHome], [teamZoneB, teamZoneB],
        c='dimgray',
        lw=lw,
        zorder=15
    )
    ax.plot(
        [officiatingLineAway, fieldSideAway], [teamZoneA, teamZoneA],
        c='dimgray',
        lw=lw,
        zorder=15
    )
    ax.plot(
        [officiatingLineAway, fieldSideAway], [teamZoneB, teamZoneB],
        c='dimgray',
        lw=lw,
        zorder=15
    )

    ax.plot(
        [sidelineHome, sidelineHome], [endlineA, endlineB],
        c='dimgray',
        lw=lw,
        zorder=15
    )
    ax.plot(
        [sidelineAway, sidelineAway], [endlineA, endlineB],
        c='dimgray',
        lw=lw,
        zorder=15
    )
    ax.plot(
        [officiatingLineHome, officiatingLineHome], [goalineA, goalineB],
        c='dimgray',
        lw=lw,
        zorder=15
    )
    ax.plot(
        [officiatingLineAway, officiatingLineAway], [goalineA, goalineB],
        c='dimgray',
        lw=lw,
        zorder=15
    )
    ax.plot(
        [fieldSideHome + 0.004, fieldSideHome + 0.004], [teamZoneA, teamZoneB],
        c='dimgray',
        lw=lw,
        zorder=15
    )
    ax.plot(
        [fieldSideAway - 0.004, fieldSideAway - 0.004], [teamZoneA, teamZoneB],
        c='dimgray',
        lw=lw,
        zorder=15
    )

    center = (sidelineHome + sidelineAway) / 2.0
    barB = (endlineB + top) / 2.0
    ax.plot(
        [center, center],
        [endlineB + 0.2 * (barB - endlineB), barB - 0.2 * (barB - endlineB)],
        c='dimgray',
        lw=2 * lw
    )
    barA = (endlineA + bottom) / 2.0
    ax.plot(
        [center, center],
        [endlineA + 0.2 * (barA - endlineA), barA - 0.2 * (barA - endlineA)],
        c='dimgray',
        lw=2 * lw
    )

    barLeft = center - 0.1 * center
    barRight = center + 0.1 * center
    ax.plot([barLeft, barRight], [barB, barB], c='dimgray', lw=lw, zorder=15)
    ax.plot([barLeft, barLeft], [barB, top], c='dimgray', lw=lw, zorder=15)
    ax.plot([barRight, barRight], [barB, top], c='dimgray', lw=lw, zorder=15)
    ax.plot([barLeft, barRight], [barA, barA], c='dimgray', lw=lw, zorder=15)
    ax.plot([barLeft, barLeft], [barA, bottom], c='dimgray', lw=lw, zorder=15)
    ax.plot(
        [barRight, barRight], [barA, bottom], c='dimgray', lw=lw, zorder=15
    )

    for i, y in enumerate(np.linspace(tenYardA, tenYardB, 9)):
        if i > 4:
            i = 8 - i
        ax.text(
            numbersLeft,
            y,
            '{}'.format(10 + i * 10),
            color='lightgray',
            fontweight='heavy',
            fontsize=numbersFontSize,
            ha='center',
            va='center',
            rotation=-90,
            zorder=5
        )
        ax.text(
            numbersRight,
            y,
            '{}'.format(10 + i * 10),
            color='lightgray',
            fontweight='heavy',
            fontsize=numbersFontSize,
            ha='center',
            va='center',
            rotation=90,
            zorder=5
        )
        ax.plot(
            [sidelineAway, sidelineHome], [y, y],
            c='dimgray',
            lw=lw,
            zorder=15
        )

    middleEndzoneA = (goalineA + endlineA) / 2
    middleEndzoneB = (goalineB + endlineB) / 2
    ax.text(
        center,
        middleEndzoneA,
        'Endzone A',
        color='lightgray',
        fontweight='heavy',
        fontsize=numbersFontSize,
        ha='center',
        va='center',
        zorder=5
    )
    ax.text(
        center,
        middleEndzoneB,
        'Endzone B',
        color='lightgray',
        fontweight='heavy',
        fontsize=numbersFontSize,
        ha='center',
        va='center',
        zorder=5
    )

    middleTeamzoneHome = (officiatingLineHome + fieldSideHome) / 2
    middleTeamzoneAway = (officiatingLineAway + fieldSideAway) / 2
    ax.text(
        middleTeamzoneHome,
        midfield,
        'Heim',
        color='lightgray',
        fontweight='heavy',
        fontsize=numbersFontSize,
        ha='center',
        va='center',
        rotation=-90,
        zorder=5
    )
    ax.text(
        middleTeamzoneAway,
        midfield,
        'Gast',
        color='lightgray',
        fontweight='heavy',
        fontsize=numbersFontSize,
        ha='center',
        va='center',
        rotation=90,
        zorder=5
    )

    for i in np.linspace(goalineA, goalineB, 101):
        ax.plot(
            [sidelineHome, sidelineHome + 0.06 * hashLeft], [i, i],
            c='lightgray',
            lw=0.2 * lw,
            zorder=10
        )
        ax.plot(
            [hashLeft - 0.03 * hashLeft, hashLeft + 0.03 * hashLeft], [i, i],
            c='lightgray',
            lw=0.2 * lw,
            zorder=10
        )
        ax.plot(
            [hashRight - 0.03 * hashLeft, hashRight + 0.03 * hashLeft], [i, i],
            c='lightgray',
            lw=0.2 * lw,
            zorder=10
        )
        ax.plot(
            [sidelineAway, sidelineAway - 0.06 * hashLeft], [i, i],
            c='lightgray',
            lw=0.2 * lw,
            zorder=10
        )

    for i in np.linspace(goalineA, goalineB, 21):
        ax.plot(
            [sidelineAway, sidelineHome], [i, i],
            c='gray',
            lw=0.5 * lw,
            zorder=10
        )

    ax.plot(
        [officiatingLineAway, officiatingLineHome], [goalineA, goalineA],
        c='dimgray',
        lw=lw,
        zorder=15
    )
    ax.plot(
        [officiatingLineAway, officiatingLineHome], [goalineB, goalineB],
        c='dimgray',
        lw=lw,
        zorder=15
    )

    pylonSize = 0.01
    rect = patches.Rectangle(
        (
            sidelineHome - 0.5 * math.sqrt(2) * pylonSize,
            goalineA - 0.5 * pylonSize
        ),
        pylonSize * math.sqrt(2),
        pylonSize,
        fc='orange',
        ec='none',
        zorder=25
    )
    ax.add_patch(rect)
    rect = patches.Rectangle(
        (
            sidelineAway - 0.5 * math.sqrt(2) * pylonSize,
            endlineA - 0.5 * pylonSize
        ),
        pylonSize * math.sqrt(2),
        pylonSize,
        fc='orange',
        ec='none',
        zorder=25
    )
    ax.add_patch(rect)
    rect = patches.Rectangle(
        (
            sidelineAway - 0.5 * math.sqrt(2) * pylonSize,
            goalineA - 0.5 * pylonSize
        ),
        pylonSize * math.sqrt(2),
        pylonSize,
        fc='orange',
        ec='none',
        zorder=25
    )
    ax.add_patch(rect)
    rect = patches.Rectangle(
        (
            sidelineHome - 0.5 * math.sqrt(2) * pylonSize,
            endlineA - 0.5 * pylonSize
        ),
        pylonSize * math.sqrt(2),
        pylonSize,
        fc='orange',
        ec='none',
        zorder=25
    )
    ax.add_patch(rect)
    rect = patches.Rectangle(
        (
            sidelineHome - 0.5 * math.sqrt(2) * pylonSize,
            goalineB - 0.5 * pylonSize
        ),
        pylonSize * math.sqrt(2),
        pylonSize,
        fc='orange',
        ec='none',
        zorder=25
    )
    ax.add_patch(rect)
    rect = patches.Rectangle(
        (
            sidelineAway - 0.5 * math.sqrt(2) * pylonSize,
            endlineB - 0.5 * pylonSize
        ),
        pylonSize * math.sqrt(2),
        pylonSize,
        fc='orange',
        ec='none',
        zorder=25
    )
    ax.add_patch(rect)
    rect = patches.Rectangle(
        (
            sidelineAway - 0.5 * math.sqrt(2) * pylonSize,
            goalineB - 0.5 * pylonSize
        ),
        pylonSize * math.sqrt(2),
        pylonSize,
        fc='orange',
        ec='none',
        zorder=25
    )
    ax.add_patch(rect)
    rect = patches.Rectangle(
        (
            sidelineHome - 0.5 * math.sqrt(2) * pylonSize,
            endlineB - 0.5 * pylonSize
        ),
        pylonSize * math.sqrt(2),
        pylonSize,
        fc='orange',
        ec='none',
        zorder=25
    )
    ax.add_patch(rect)
    rect = patches.Rectangle(
        (hashLeft - 0.5 * math.sqrt(2) * pylonSize, barA - 0.5 * pylonSize),
        pylonSize * math.sqrt(2),
        pylonSize,
        fc='orange',
        ec='none',
        zorder=25
    )
    ax.add_patch(rect)
    rect = patches.Rectangle(
        (hashLeft - 0.5 * math.sqrt(2) * pylonSize, barB - 0.5 * pylonSize),
        pylonSize * math.sqrt(2),
        pylonSize,
        fc='orange',
        ec='none',
        zorder=25
    )
    ax.add_patch(rect)
    rect = patches.Rectangle(
        (hashRight - 0.5 * math.sqrt(2) * pylonSize, barA - 0.5 * pylonSize),
        pylonSize * math.sqrt(2),
        pylonSize,
        fc='orange',
        ec='none',
        zorder=25
    )
    ax.add_patch(rect)
    rect = patches.Rectangle(
        (hashRight - 0.5 * math.sqrt(2) * pylonSize, barB - 0.5 * pylonSize),
        pylonSize * math.sqrt(2),
        pylonSize,
        fc='orange',
        ec='none',
        zorder=25
    )
    ax.add_patch(rect)

    fig.set_size_inches(8.3, 11.7)
    fig.savefig(u'field.svg', bbox_inches=u'tight')


if __name__ == '__main__':
    main()
