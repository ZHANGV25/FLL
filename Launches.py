#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Run #1- Bench (M04) and Slide (M03)
East = [
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


# Run #2- Step Counter (M02), Pull-up Bar (M06), Boccia (M08), Basketball (M05)
NorthEast = [
    ["Drive"           ,  0  ,  50  ,  25  ],
    ["Drive"           ,  0  ,  20  ,  10  ],
    ["Drive"           ,  0  ,  -20 ,  -10 ],
    ["Turn"            ,  25 ,  -30 ,  -30 ],
    ["Drive"           ,  0  ,  30  ,   15 ],
    ["Turn"            ,  25 ,  30  ,   15 ],
    ["Drive"           ,  0  ,  60  ,   35 ],
]

# Run #3- Treadmill (M11), Row machine (M12), Weight machine (M13), Cell phone (M10)
NorthWest = [
    ["Drive"           ,  0  ,  40  ,  100 ],
    # Spin Treadmill with attachment- ADD CODE for medium motor!
    ["Drive"           ,  0  ,  -40 ,  -20 ],
    ["Turn"            , 30  ,  20  ,  20  ],
    ["Drive"           ,  0  ,  15  ,  15  ],
    # Do the Row Machine- ADD CODE for motor!
    ["Drive"           ,  0  ,  -10 ,  -5  ],
    ["Turn"            , 30  ,   15 ,  10  ],
    ["Drive"           ,  0  ,   30 ,  70  ],
    # Do Weight Machine- ADD CODE for motor!
    ["Drive"           ,  0  ,  -20 ,  -40 ],
    ["Turn"            , 40  ,   30 ,   30 ],
    # Do Cell Phone- ADD CODE for motor!
    # Come back to Base- ADD CODE
]

#Run #4- Tire Flip (M09), Robot dance (M07)
RobotDance = [
    
]

Launches = [East, NorthEast, NorthWest, RobotDance]
