import commands2
from wpimath.controller import PIDController
from constants import turn_K_p, turn_K_I, turn_K_D
from subsytems.drivetrain import Drivetrain


class Turn(commands2.PIDCommand):
    def __init__(self, distSetPt: float, drivetrain: Drivetrain):
        super().__init__(
            PIDController(turn_K_p, turn_K_I, turn_K_D),

            drivetrain.gyro.getYaw,

            distSetPt,

            drivetrain.turn,
            [drivetrain]
        )

    def isFinished(self) -> bool:
        print("turn status", self.getController().atSetpoint())
        return self.getController().atSetpoint()