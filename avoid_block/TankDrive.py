from ev3dev2.motor import MoveTank

class TankDrive(MoveTank):
    def drive_backward_by_rotations(self, rotations):
        MoveTank.on_for_rotations(self, -20, -20, rotations)

    def drive_turn_left(self):
        self.drive_backward_by_rotations(1)
        MoveTank.on_for_rotations(self, -20, 20, 0.5)