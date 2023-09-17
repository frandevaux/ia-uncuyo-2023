import random
from action import Action
from environment import Environment
from color import Color
from slot  import Slot


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
        if currentSlot == self.env.goal_position:
            return [currentSlot]
        queue = []
        queue.append(currentSlot)
        explored = []

        while queue:
            currentSlot = queue.pop(0)
            explored.append(currentSlot)
            self.env.print_environment(currentSlot)
            for action in Action:
                if self.env.is_valid_action(currentSlot, action):
                    slot = self.env.get_slot(currentSlot, action)
                    if slot not in explored and slot not in queue:
                        slot.parent = currentSlot
                        if slot == self.env.goal_position:
                            return self.findPath(slot, [])
                        queue.append(slot)



    def dfs(self, currentSlot:Slot):
        currentSlot.color = Color.GREY

        if (currentSlot == self.env.goal_position):
            print("Goal found")
            return self.findPath(currentSlot, [])
        for slot in currentSlot.adjacentSlots:
            if (slot.color == Color.WHITE):
                slot.parent = currentSlot
                return self.dfs(slot)
        currentSlot.color = Color.BLACK

    def findPath(self, slot: Slot, path):

        path.append(slot)
        while slot != None:
            slot.isPath=True

            return self.findPath(slot.parent, path)

        return path