import arcade.key
from random import randint
import math
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4

DIR_OFFSET = {DIR_UP:(0,1), DIR_RIGHT:(1,0), DIR_DOWN:(0,-1), DIR_LEFT:(-1,0)}

class Heart:
    def __init__(self,world):
        self.world = world
        self.x = 0
        self.y = 0

    def randompos(self):
        centerX = self.world.width//2
        centerY = self.world.height//2
        self.x = centerX + randint(-15,15)*Snake.BLOCK_SIZE
        self.y = centerY + randint(-15,15)*Snake.BLOCK_SIZE


    
        

        
class Snake:
    MOVE_WAIT = 0.09
    BLOCK_SIZE = 16
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = DIR_RIGHT
        self.wait_time = 0
        self.body = [(x,y),(x-Snake.BLOCK_SIZE, y),(x-2*Snake.BLOCK_SIZE, y)]
        self.has_eaten = False
        self.length = 3

    def out_of_range(self):
        if self.x > self.world.width:
            self.x = Snake.BLOCK_SIZE
        elif self.y > self.world.height:
            self.y = Snake.BLOCK_SIZE
        elif self.y < 0:
            self.y = self.world.height - Snake.BLOCK_SIZE
        elif self.x < 0:
            self.x = self.world.width - Snake.BLOCK_SIZE

    def addlength(self):
        if(self.has_eaten):
            self.length += 1
            self.body.insert(0,(self.x,self.y))
            self.has_eaten = False

    def eat(self,Heart):
        if(self.x == Heart.x and self.y == Heart.y):
            return True
    def eat_tail(self):
        for sbody in self.body[1:]:
            if sbody == self.body[0]:
                self.length -= 1
                return True

    def update(self,delta):
        self.wait_time += delta
        if self.wait_time<Snake.MOVE_WAIT:
            return
        self.x += self.BLOCK_SIZE*DIR_OFFSET[self.direction][0]
        self.y += self.BLOCK_SIZE*DIR_OFFSET[self.direction][1]
        
        self.out_of_range()
        self.body.insert(0,(self.x,self.y))
        self.body.pop()
       

        if(self.eat_tail()):
            self.body.pop()
            print(self.length)
       
        self.wait_time = 0

class World:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.heart = Heart(self)
        self.heart.randompos()
        self.snake = Snake(self,width//2,height//2)
        

    def update(self,delta):
        self.snake.update(delta)
        if(self.snake.eat(self.heart)):
            self.snake.has_eaten = True
            self.heart.randompos()
            self.snake.addlength()

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.snake.direction = DIR_UP
        elif key == arcade.key.DOWN:
            self.snake.direction = DIR_DOWN
        elif key == arcade.key.LEFT:
            self.snake.direction = DIR_LEFT
        elif key == arcade.key.RIGHT:
            self.snake.direction = DIR_RIGHT
