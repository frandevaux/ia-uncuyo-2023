import random
from action import Action
from environment import Environment
from color import Color


class Agent:
    def __init__(self, env: Environment):
        self.env = env
        self.posX = env.initial_position.posX
        self.posY = env.initial_position.posY
        self.points = 0
        self.remaining_actions = 1000
        self.path = []


    
    def perform_action(self, action: Action):
        if (self.env.is_valid_action(self, action)):
            
        
            match action:
                case Action.DOWN:
                    self.posY += 1
                case Action.UP:
                    self.posY -= 1
                case Action.RIGHT:
                    self.posX += 1
                case Action.LEFT:
                    self.posX -= 1
                
            
            self.remaining_actions -= 1
            

    def is_slot_obstacle(self):
        return self.env.matrix[self.posX][self.posY].isObstacle



    def bfs(self):
        currentSlot = self.env.initial_position
        queue = []
        queue.append(currentSlot)
        currentSlot.color = Color.GREY

        while (len(queue) > 0):
            currentSlot = queue.pop(0)

            if (currentSlot == self.env.goal_position):
                print("Goal found")
                return True

            for slot in currentSlot.adjacentSlots:
                if (slot.color == Color.WHITE):
                    slot.color = Color.GREY
                    queue.append(slot)
            currentSlot.color = Color.BLACK