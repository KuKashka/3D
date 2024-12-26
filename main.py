from ursina import *

app = Ursina()

block = Entity(model='cube', texture='grass', position=(0,0,0), rotation=(45,0,0), skale=2.7)
block2 = Entity(model='cube', texture='grass', position=(2,0,0), rotation=(0,40,0))
block3 = Entity(model='cube', texture='grass', position=(2,2,-6), rotation=(0,0,46))
block.x = 3.4
EditorCamera()


app.run()