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

#Towers = [
#    ["Turn"            ,  10 ,  40  ,   60  ],
#    ["Drive"           ,  0  ,  30  ,  100  ],
#]
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

# Flips the elevator and lowers two beams on the safety factor.
East = [
    #Does treehouse
    ["Drive"            ,  0  ,  20  ,  67  ],
    ["Drive"            ,  0  , -20  , -20  ],
    #Turns towrds safety factor
    ["Turn"             ,  0  , -40  , -135 ],
    #Does safety factor and elevator
    ["Drive"            , -145 , -20  , -100 ],
    ["Turn"             ,  0  ,  35  ,  45  ],
    #Does swing
    ["Drive"            ,  45 ,  20  ,  2   ],
    ["MotorOn"          ,  0  , -2          ],
    ["Wait"             ,  2.5              ],
    ["Drive"            ,  45  , 25  ,  5   ],
    ["MotorOn"          ,  0  , 3           ],  
    ["Wait"             ,  1                ],
    ["MotorOff"         ,  0                ],
    ["DriveUltrasonic"  ,  45 , -20  ,   5  ],
    ["Turn"             ,  10 , -40  ,   0  ],
]



# Places the tan tower.

Towers = [
    ["DriveUltrasonic"  ,   0  , 20  ,  30  ],
    ["Turn"             ,   0  , 40  ,  90  ],
    ["DriveUltrasonic"  ,   90 , 20  ,  100 ],
    ["Turn"             ,   0  , 40  ,  45  ],
    ["LineFollow"       ,         5         ],
    ["Drive"            ,  45  , 20  ,  17  ],
    ["Drive"            ,  90  ,-20  , -30  ],
    ["MotorOn"          ,   0  ,  4         ],
    ["MotorOn"          ,   1  , -4         ],
    ["Wait"             ,               1   ],
]


TanTower = Tower(110, 50)

RedTower = Tower(55, 50)
# Does all aspects of the crane mission.
Crane = [
    ["DriveUltrasonic" ,  0  ,  10  ,  10  ],
    ["Turn"            ,  0  ,  40  ,  90  ],
    ["DriveUltrasonic" ,  90 ,  10  ,  59  ],
    ["Turn"            ,  0  , -40  ,  0   ],
    ["DriveUltrasonic" ,  0  ,  20  ,  60  ],
    ["Drive"           ,  0  ,  3   ,  8   ],
    ["Wait"            ,  1                ],
    ["DriveUltrasonic" ,  0  , -30  ,  30  ],
    ["Turn"            ,  0  ,  30  ,  90  ],
    ["DriveUltrasonic" ,  90 , -20  ,  10  ],
    ["Turn"            ,  5  , -30  ,  0   ],
]

# Places the blue and white towers in the black circle.
MixedTower = Tower(55, 90)



# Raises the traffic jam and starts the swing.
South = [
    ["Turn"            ,  12 ,  30  ,  90  ],   
    ["Drive"           ,  90 ,  10  ,  105 ],
    ["Wait"            ,               1   ],
    ["DriveUltrasonic" ,  90 , -30  ,  10  ],
    ["Turn"            ,  5  , -30  ,  0   ],
]

Launches = [East, Towers, TanTower, RedTower, Crane, MixedTower, South]
