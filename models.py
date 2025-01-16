from ursina import *
from perlin_noise import PerlinNoise 
from ursina.shaders import basic_lighting_shader
from numpy import floor

class Block(Entity):
    def __init__(self, block_type, pos,**kwargs):
            super().__init__(
            model='cube',
            texture='grass',
            position=pos,
            scale=1,
            collider='box',
            origin_y=-0.5,
            color=color.color(0,0, random.uniform(0.9, 1)),
            shader=basic_lighting_shader,
            **kwargs
        )



class Map(Entity):
    def __init__(self, **kwargs):
            super().__init__(model=None, Collider=None, **kwargs)
            self.bedrock = Entity(model='plane', collider='box', scale=1000, texture='grass', texture_scale=(4,4),position=(0,-2,0))
            self.blocks = {}
            self.noise = PerlinNoise(octaves = 3, seed=4522)

    def new_map(self):
        for x in range(50):
            for z in range(50):
                y = floor(self.noise([x/24, z/24])*6)
                block = Block(0, (x,y,z))

