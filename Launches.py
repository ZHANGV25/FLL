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



# Places both tower
TanTower = Tower(110, 50)
RedTower = Tower(58, 50)
MixedTower = Tower(55, 90)

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
    ["Turn"            ,  12 ,  30  ,  90  ],   
    ["Drive"           ,  90 ,  10  ,  50  ],
    ["DriveUltrasonic" ,  90 , -30  ,  10  ],
    ["Turn"            ,  5  , -30  ,  0   ],
]

Launches = [East, TanTower, RedTower, Crane, MixedTower, South]
