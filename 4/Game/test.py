from game import move
from map import rooms
move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
