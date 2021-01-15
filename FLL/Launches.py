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
    #Does Bench
    ["DriveUltrasonic"  ,  0  ,  20  ,  40  ],
    ["Turn"             ,  0  , -15  , -15  ],
    ["Turn"             ,  0  ,  15  ,  15  ],
    ["Drive"            ,  10 ,   5  ,  10  ],
    #Backs out of bench
    ["Drive"            ,  10 , -20  , -15  ],
    #Turns and drives towrds swing
    ["Turn"             ,   0 ,  30  ,  90  ],
    ["DriveUltrasonic"  ,  90 ,  20  ,  80  ],
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

South = [
    
]

Launches = [Bench, Mid, South]
