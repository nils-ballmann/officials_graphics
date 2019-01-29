#!/usr/bin/env python3
# encoding: utf-8

# pylint: disable=C0111

__updated__ = '2019-01-29 21:31:26'

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.collections as mcollections

plt.rcParams['svg.fonttype'] = 'none'
# DIN A4 in inches
plt.rcParams['figure.figsize'] = (11.69, 8.27)

__version_info__ = [0, 0, 1]
__version__ = '.'.join([str(digit) for digit in __version_info__])


def main():
    patches = []
    # definitions
    field_width = 11.69
    team_a_ec = '#2d31a8'
    team_a_fc = '#4248f4'
    team_a_alpha = 0.5
    ball_width = 0.125
    ball_height = 0.2
    player_size = 0.275
    player_lw = 1

    # tacklebox
    patches.append(
        mpatches.Rectangle(
            (3.5*player_size, 3*player_size), -7*player_size, -15*player_size, fc='lightgrey', lw=2, alpha=0.75
        )
    )

    # neutrale zone
    patches.append(
        mpatches.Rectangle(
            (-(field_width/2), -(ball_height/2)), field_width, ball_height, ec='none', fc='brown', alpha=0.2
        )
    )
    patches.append(mpatches.Ellipse((0, 0), ball_width, ball_height, ec='none', fc='brown'))

    # bad zones
    patches.append(
        mpatches.Rectangle(
            (-(field_width/2), -5*player_size), field_width, -8*player_size, fc='red', ec='darkred', lw=2, alpha=0.2
        )
    )
    patches.append(
        mpatches.Rectangle(
            (-(field_width/2), 5*player_size), field_width, 8 * player_size, fc='red', ec='darkred', lw=2, alpha=0.2
        )
    )

    patches.append(
        mpatches.Arrow(
            -player_size/2,
            -(ball_height/2 + 6*player_size),
            -2 * player_size,
            0,
            width=0.25,
            fc=team_a_fc,
            ec=team_a_ec,
            alpha=team_a_alpha
        )
    )

    patches.append(
        mpatches.Arc(
            (0, -(ball_height/2 + 6*player_size)),
            height=player_size*2,
            width=player_size*2,
            theta1=90,
            theta2=180,
            lw=player_lw,
            fc='green',
            ec='darkgreen'
        )
    )
    patches.append(
        mpatches.Circle(
            (0, -(ball_height/2 + 6*player_size)),
            radius=player_size/2,
            lw=player_lw,
            fc=team_a_fc,
            ec=team_a_ec,
            alpha=team_a_alpha
        )
    )
    patches.append(
        mpatches.Circle(
            (0, -(ball_height/2 + 3*player_size)),
            radius=player_size/2,
            lw=player_lw,
            fc=team_a_fc,
            ec=team_a_ec,
            alpha=team_a_alpha
        )
    )
    patches.append(
        mpatches.Circle(
            (3.75*player_size, -(ball_height/2 + 2*player_size)),
            radius=player_size/2,
            lw=player_lw,
            fc=team_a_fc,
            ec=team_a_ec,
            alpha=team_a_alpha
        )
    )
    patches.append(
        mpatches.Circle(
            (-14*player_size, -(ball_height/2 + 2*player_size)),
            radius=player_size/2,
            lw=player_lw,
            fc=team_a_fc,
            ec=team_a_ec,
            alpha=team_a_alpha
        )
    )
    patches.append(
        mpatches.Circle(
            (14*player_size, -(ball_height/2 + player_size/2*1.5)),
            radius=player_size/2,
            lw=player_lw,
            fc=team_a_fc,
            ec=team_a_ec,
            alpha=team_a_alpha
        )
    )
    patches.append(
        mpatches.Circle(
            (-4.5*player_size, -(ball_height/2 + player_size/2*1.5)),
            radius=player_size/2,
            lw=player_lw,
            fc=team_a_fc,
            ec=team_a_ec,
            alpha=team_a_alpha
        )
    )
    patches.append(
        mpatches.Circle(
            (3*player_size, -(ball_height/2 + player_size/2*1.5)),
            radius=player_size/2,
            lw=player_lw,
            fc=team_a_fc,
            ec=team_a_ec,
            alpha=team_a_alpha
        )
    )
    patches.append(
        mpatches.Circle(
            (1.5*player_size, -(ball_height/2 + player_size/2*1.5)),
            radius=player_size/2,
            lw=player_lw,
            fc=team_a_fc,
            ec=team_a_ec,
            alpha=team_a_alpha
        )
    )
    patches.append(
        mpatches.Circle(
            (-3*player_size, -(ball_height/2 + player_size/2*1.5)),
            radius=player_size/2,
            lw=player_lw,
            fc=team_a_fc,
            ec=team_a_ec,
            alpha=team_a_alpha
        )
    )
    patches.append(
        mpatches.Circle(
            (-1.5*player_size, -(ball_height/2 + player_size/2*1.5)),
            radius=player_size/2,
            lw=player_lw,
            fc=team_a_fc,
            ec=team_a_ec,
            alpha=team_a_alpha
        )
    )
    patches.append(
        mpatches.Circle(
            (0, -(ball_height/2 + player_size/2)),
            radius=player_size/2,
            lw=player_lw,
            fc=team_a_fc,
            ec=team_a_ec,
            alpha=team_a_alpha
        )
    )

    # paper
    patches.append(mpatches.Rectangle((-(field_width/2), -(HEIGHT/2)), field_width, HEIGHT, fc='white'))

    fig, ax = plt.subplots(nrows=1, ncols=1)
    for patch in patches:
        ax.add_patch(patch)

    plt.title('Legal blocks below the waist (Tacklebox existent)')
    plt.axis('equal')
    # plt.axis('off')
    plt.tight_layout()
    plt.show()

    # plt.savefig(
    #    'network_adapter_outage.svg',
    #    bbox_inches='tight'
    # )


if __name__ == "__main__":
    main()
