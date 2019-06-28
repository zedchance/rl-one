import tcod as libtcod
from input_handlers import handle_keys
from entity import Entity
from render_functions import clear_all, render_all
from map_objects.game_map import GameMap

def main():
   # Screen size
   screen_width = 80
   screen_height = 50
   
   # Map and rooms
   map_width = 80
   map_heigth = 45
   room_max_size = 10
   room_min_size = 6
   max_rooms = 30
   
   # Color dictinoary
   colors = {
      'dark_wall': libtcod.Color(0, 0, 100),
      'dark_ground': libtcod.Color(50, 50, 150)
   }
   
   # Draw player and other entities
   player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libtcod.white)
   npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), 'R', libtcod.red)
   entities = [npc, player]
   
   # Setup libtcod console
   libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
   libtcod.console_init_root(screen_width, screen_height, 'RL-ONE', False)
   con = libtcod.console_new(screen_width, screen_height)
   
   # Draw map
   game_map = GameMap(map_width, map_heigth)
   game_map.make_map(max_rooms, room_min_size, room_max_size, map_width, map_heigth, player)
   
   # Input controls
   key = libtcod.Key()
   mouse = libtcod.Mouse()
   
   # Game loop
   while not libtcod.console_is_window_closed():
      libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
      
      render_all(con, entities, game_map, screen_width, screen_height, colors)
      libtcod.console_flush()
      
      clear_all(con, entities)
      
      action = handle_keys(key)
      
      move = action.get('move')
      exit = action.get('exit')
      fullscreen = action.get('fullscreen')
      
      if move:
         dx, dy = move
         if not game_map.is_blocked(player.x + dx, player.y + dy):
            player.move(dx, dy)
      
      if exit:
         return True
         
      if fullscreen:
         libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
   
if __name__ == '__main__':
   main()
