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
    ["Turn"             ,  0  , -40  , -133 ],
    #Does safety factor and elevator
    ["Drive"            , -133, -20  , -100 ],
    ["Turn"             ,  0  ,  35  ,  45  ],
    #Does swing
    ["Turn"             ,  0  , -40  , -60  ],
    ["Drive"            , -60 , -30  , -10  ],
    ["Turn"             ,  10 , -40  , -90  ],
    ["Drive"            , -90 ,  30  ,  15  ],
    ["Turn"             ,  0  , -40  , -135 ],
    ["Drive"            , -135,  30  ,  150 ],
    ["Turn"             ,  10 ,  40  , -50  ],
]



#Places other towers
MixedTower = Tower(55, 90)

#Places Innovative
InnovativeAndOther = Tower(60, 45)

# Does all aspects of the crane mission.
Crane = [
    ["DriveUltrasonic" ,  0  ,  10  ,  10  ],
    ["Turn"            ,  0  ,  40  ,  90  ],
    ["DriveUltrasonic" ,  90 ,  10  ,  59  ],
    ["Turn"            ,  0  , -40  ,  0   ],
    ["DriveUltrasonic" ,  0  ,  20  ,  60  ],
    ["Drive"           ,  0  ,  2   ,  12  ],
    ["DriveUltrasonic" ,  0  , -30  ,  30  ],
    ["Turn"            ,  0  ,  30  ,  90  ],
    ["DriveUltrasonic" ,  90 , -20  ,  10  ],
    ["Turn"            ,  5  , -30  ,  0   ],
]

# Raises the traffic jam and starts the swing.
South = [
    #Starts turning the motors to lock the towers in place
    ["MotorOn"         ,  0  , -4          ],
    ["Wait"            , 0.80              ],
    ["MotorOff"        ,  0                ],
    ["MotorOn"         ,  1  ,  4          ],
    ["Wait"            , 0.17              ],
    ["MotorOff"        ,  1                ],
    #Turns towrds traffic jam
    ["Turn"            , 11  ,  30  ,  90  ],
    #Drives until it has wedged under the traffic jam
    ["DriveUltrasonic" ,  90 ,  20  ,  120 ],
    #Fully lifts up traffic jam
    ["Turn"            , 10  , -30  ,   0  ],
    #Goes forward and turns towrds tan towers
    ["Drive"           ,  0  ,  20  ,  10  ],
    ["Turn"            ,  0  ,  30  ,  90  ],
    ["DriveUltrasonic" ,  90 ,  20  ,  149 ],
    ["Turn"            ,  0.9, -30  ,  0   ],
    ["DriveUltrasonic" ,  0  ,  20  ,  50  ],
    #Drops of tan towers
    ["MotorOn"         ,  0  ,  4          ],
    ["Wait"            , 0.80              ],
    ["MotorOff"        ,  0                ],
    #Backs up and turns towrds red towers
    ["DriveUltrasonic" ,  0  , -20  ,  15  ],
    ["Turn"            ,  0  ,  30  ,  90  ],
    ["Drive"           , 90  , -20  , -30  ],
    #Drops of red towers
    ["MotorOn"         ,  1  , -4          ],
    ["Wait"            , 0.17              ],
    ["MotorOff"        ,  1                ],
    ["Wait"            ,  1                ],
    #Comes back home
    ["Drive"           ,  90 , -20  , -50  ],
    #Closes the door to fit in base
    ["MotorOn"         ,  1  ,  0.01       ],
    ["Drive"           ,  90 , -20  , -65  ],
]

Launches = [East, South, Crane, MixedTower, InnovativeAndOther]
