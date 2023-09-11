import random
from action import Action
from environment import Environment



class Agent:
    def __init__(self, env: Environment):
        self.env = env
        self.posX = env.initial_position[0]
        self.posY = env.initial_position[1]
        self.points = 0
        self.remaining_actions = 1000
        self.path = []

        while (self.posX != env.goal_position[0] and self.posY != env.goal_position[1] and  self.remaining_actions > 0):
            self.think()
    
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
        return self.env.is_obstacle(self.posX, self.posY)

    def think(self):
        if (self.is_random_agent):
            self.perform_action(random.choice(list(Action)))
        else: 
            if(self.is_slot_obstacle()):
                self.perform_action(Action.CLEAN)
            else:
                directions = [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT]
                self.perform_action(random.choice(directions))