import arcade
from models import World
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()

class SnakeSprite:
    def __init__(self, snake):
        self.snake = snake
        self.block_sprite = arcade.Sprite('images/block.png')
        
 
    def draw(self):
        for x,y in self.snake.body:
            self.block_sprite.set_position(x,y)
            self.block_sprite.draw()
                
            
        
class SnakeWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.AMAZON)
 
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.t1 = arcade.create_text("Game over", arcade.color.BLACK, 50)
        self.snake_sprite = SnakeSprite(self.world.snake)
        self.heart_sprite = ModelSprite('images/Heart.png',model = self.world.heart)
        
         
    def update(self, delta):
        self.world.update(delta)
 
 
    def on_draw(self):
        arcade.start_render()
        if self.snake_sprite.snake.gg == 0:
            self.snake_sprite.draw()
            self.heart_sprite.draw()
        else:
            start_x = 150
            start_y = SCREEN_HEIGHT//2
            arcade.render_text(self.t1,start_x,start_y)
            arcade.set_background_color(arcade.color.CHARCOAL)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
 
     
def main():
        window = SnakeWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
        arcade.set_window(window)
        arcade.run()
        

if __name__ == '__main__':
    main()
