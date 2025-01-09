from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

sky=Sky(texture='sky_sunset')

ground=Entity(model='plane', collider='box', scale=1000, texture='grass', texture_scale=(4,4),position=(0,-2,0))

player = FirstPersonController()

block = Entity(model='cube', texture='grass', position=(0,0,0), rotation=(0,0,0), skale=2.7)




app.run()