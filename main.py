from ursina import *

app = Ursina()

from models import *

sky=Sky(texture='sky_sunset')


map = Map()
#map.new_map(size = 60)
map.load()




app.run()