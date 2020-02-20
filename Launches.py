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

Towers = [
    ["Turn"            ,  10 ,  40  ,   60  ],
    ["Drive"           ,  0  ,  30  ,  100  ],
]
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

TanTower = Tower(50, 120)

RedTower = Tower(50, 55)
# Does all aspects of the crane mission.
Crane = [
    ["DriveUltrasonic" ,  0  ,  20  ,  10  ],
    ["Turn"            ,  0  ,  40  ,  90  ],
    ["DriveUltrasonic" ,  90 ,  20  ,  57  ],
    ["Turn"            ,  0  , -40  ,  0   ],
    ["DriveUltrasonic" ,  0  ,  30  ,  60  ],
    ["Drive"           ,  0  ,  1   ,  8   ],
    ["Wait"            ,  1                ],
    ["DriveUltrasonic" ,  0  , -30  ,  30  ],
    ["Turn"            ,  0  ,  30  ,  90  ],
    ["DriveUltrasonic" ,  90 , -20  ,  10  ],
    ["Turn"            ,  5  , -30  ,  0   ],
]

# Places the blue and white towers in the black circle.
MixedTower = Tower(55, 90)

# Flips the elevator and lowers two beams on the safety factor.
East = [
    #Does treehouse
    ["Drive"            ,  0  ,  20  ,  67  ],
    ["Drive"            ,  0  , -20  , -20  ],
    #Turns towrds safety factor
    ["Turn"             ,  0  , -40  , -140 ],
    #Does safety factor and elevator
    ["Drive"            , -135, -20  , -100 ],
    ["Turn"             ,  0  ,  35  ,  45  ],
    #Does swing
    ["MotorOn"          ,  0  , -3          ],
    ["Wait"             ,  2                ],
    ["MotorOff"         ,  0                ],
    ["Drive"            ,-100 ,  20  , 153  ],
    ["Turn"             ,  10 ,  90  ,   0  ],
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
