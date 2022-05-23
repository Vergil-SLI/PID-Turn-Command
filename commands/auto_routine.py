import commands2
from drivestraight import DriveStraight
from turn import Turn


class Auto_Routine(commands2.SequentialCommandGroup):
    def __init__(self):
        super.__init__()
        self.addCommands(
            DriveStraight(),
            Turn(),
            DriveStraight(),
            Turn()
        )
    
    def isFinished(self) -> bool:
        return super().isFinished()