from ursina import *

app = Ursina()

from models import *

sky=Sky(texture='sky_sunset')


map = Map()
map.new_map(size = 60)


player = Player(speed = 13, jump_height=3)


app.run()