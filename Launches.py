#!/usr/bin/env python3

# Returns a list representing a launch that places a tower.
def Tower(distance, angle):
    return [
        ["Drive"           , 0     ,  20 ,  distance ],
        ["Drive"           , 0     , -30 , -distance ],
        ["Turn"            , 0     ,  30 ,  angle    ],
        ["DriveUltrasonic" , angle , -30 ,  5        ],
    ]

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

# Places the tan tower.
TanTower = Tower(110, 50)

# Places the red tower.
RedTower = Tower(65, 50)

# Does all aspects of the crane mission.
Crane = [
    ["DriveUltrasonic" ,  0  ,  10  ,  10  ],
    ["Turn"            ,  0  ,  30  ,  90  ],
    ["DriveUltrasonic" ,  90 ,  10  ,  57  ],
    ["Turn"            ,  0  , -30  ,  0   ],
    ["DriveUltrasonic" ,  0  ,  10  ,  60  ],
    ["Drive"           ,  0  ,  2   ,  10  ],
    ["Wait"            ,  1                ],
    ["DriveUltrasonic" ,  0  , -20  ,  50  ],
    ["Turn"            ,  0  ,  30  ,  90  ],
    ["DriveUltrasonic" ,  90 , -20  ,  10  ],
    ["Turn"            ,  5  , -30  ,  0   ],
]

# Places the blue and white towers in the black circle.
MixedTower = Tower(55, 90)

# Flips the elevator and lowers two beams on the safety factor.
East = [
    ["Drive"            ,  0  ,  20  ,  65  ],
    ["Drive"            ,  0  , -20  , -20  ],
    ["Turn"             ,  0  , -40  , -140 ],
    ["Drive"            , -137, -20  , -98  ],
    ["Turn"             ,  0  ,  35  ,  45  ],
    ["MotorOn"          ,  0  ,  3          ],
    ["Wait"             ,  1                ],
    ["MotorOff"         ,  0                ],
    ["MotorOn"          ,  0  , -3          ],
    ["Wait"             ,  1                ],
    ["MotorOff"         ,  0                ],
    ["MotorOn"          ,  0  ,  3          ],
    ["Wait"             ,  1                ],
    ["MotorOff"         ,  0                ],
    ["Drive"            ,  45 , -20  ,-153  ],
    ["Turn"             ,  10 , -90  , -45  ],
]

# Raises the traffic jam and starts the swing.
South = [
    ["Turn"            ,  12 ,  30  ,  90  ],
    ["Drive"           ,  90 ,  10  ,  105 ],
    ["Wait"            ,               1   ],
    ["DriveUltrasonic" ,  90 , -30  ,  10  ],
    ["Turn"            ,  5  , -30  ,  0   ],
]

Launches = [TanTower, RedTower, Crane, MixedTower, East, South]
