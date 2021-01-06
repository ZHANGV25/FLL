#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Key a (path):
#
#  1 - angle
#  2 - turn radius
#  3 - motor id

# Key b (speed):
#
#  1 - cm/sec
#  2 - deg/sec
#  3 - rot/sec

# Key c (target):
#
#  1 - drive centimeters
#  2 - target centimeters
#  3 - target degrees
#  4 - seconds

#   ["MoveType"        ,  a  ,  b  ,  c  ],
#
# LaunchName = [
#   ["Drive"           ,  1  ,  1  ,  1  ],
#   ["DriveUltrasonic" ,  1  ,  1  ,  2  ],
#   ["Turn"            ,  2  ,  2  ,  3  ],
#   ["LineFollow"      ,        1        ],
#   ["MotorOn"         ,  3  ,  3        ],
#   ["MotorOff"        ,  3              ],
#   ["Wait"            ,              4  ],
# ]

# Run #1- Bench and Slide
Bench = [
    # Does Bench 
    ["Drive"            ,  0  ,  40  ,  45  ],
    ["MotorOn"          ,  0  , -8          ],
    ["MotorOff"         ,  0                ],
    # Turns and faces Slide
    ["Drive"            ,  0  , -25   , -45 ],
    ["Turn"             ,  0  ,  45   ,  90 ],
    ["Drive"            ,  0  ,  40   ,  45 ],
    # Code if we are NOT using a passive attachment:
    # ["MotorOn"       ,   0  ,  -4    ], 
    # ["MotorOff"      ,   0           ],
    ["Wait"             ,                 4 ],
    ["Drive"            ,  0  , -40   , -40 ],
    # Comes back to home
    ["Turn"             ,  0  , -30   ,  30 ],
    ["Drive"            ,  0  , -40   , -40 ],
   
]

# NOT UPDATED YET 
# Does all aspects of the middle mission.
Mid = [
    # Drives foward and turnes out of base
    ["Drive"            , 0 ,  20 ,  20  ],
    ["Turn"             , 0 ,  30 ,  90  ],
    ["Drive"            , 0 ,  30 ,  40  ],
    ["Drive"            , 0 ,  10 ,  20  ],
    ["Drive"            , 0 , -10 ,  -10 ],
    ["Turn"             , 0 , -30 , -90  ],
    ["Drive"            , 0 ,  20 ,  29  ],
    ["Drive"            , 0 , -10 , -10  ],
    ["Turn"             , 0 , -30 , -90  ],
    ["LineFollow"       ,      30        ], 
    ["Drive"            , 0 ,  30 ,   3  ],         

]

# Raises the traffic jam and starts the swing.
South = [
    
]

Launches = [Bench, Mid, Crane, MixedTower, InnovativeAndOther]
