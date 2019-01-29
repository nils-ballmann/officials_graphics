#!/usr/bin/env python3
# encoding: utf-8

# pylint: disable=C0111

__updated__ = '2019-01-29 22:26:25'

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.collections as mcollections

import officials_lib as ol

plt.rcParams['svg.fonttype'] = 'none'
# DIN A4 in inches
plt.rcParams['figure.figsize'] = (11.69, 8.27)

__version_info__ = [0, 0, 1]
__version__ = '.'.join([str(digit) for digit in __version_info__])


def main():
    patches = []
    f = ol.Field()
    patches.extend(f.render())

    fig, ax = plt.subplots(nrows=1, ncols=1)
    for patch in patches:
        print(patch)
        ax.add_patch(patch)

    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

    # plt.savefig(
    #    'network_adapter_outage.svg',
    #    bbox_inches='tight'
    # )


if __name__ == "__main__":
    main()
