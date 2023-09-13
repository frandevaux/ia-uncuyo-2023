from color import Color

class Slot:
    def __init__(self, posX: int, posY: int, color= Color.WHITE, isObstacle= False, adjacentSlots = []):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.isObstacle = isObstacle
        self.adjacentSlots = adjacentSlots



