import tcod as libtcod

def handle_keys(key):
   # Movement
   key_char = chr(key.c)
   
   # Up down left right
   if key.vk == libtcod.KEY_UP or key_char == 'k' or key_char == '8': # TODO make this numpads
      return {'move': (0, -1)}
   elif key.vk == libtcod.KEY_DOWN or key_char == 'j' or key_char == '2':
      return {'move': (0, 1)}
   elif key.vk == libtcod.KEY_LEFT or key_char == 'h':
      return {'move': (-1, 0)}
   elif key.vk == libtcod.KEY_RIGHT or key_char == 'l':
      return {'move': (1, 0)}
   # Diagonal movement
   elif key_char == 'y':
      return {'move': (-1, -1)}
   elif key_char == 'u':
      return {'move': (1, -1)}
   elif key_char == 'b':
      return {'move': (-1, 1)}
   elif key_char == 'n':
      return {'move': (1, 1)}
      
   if key.vk == libtcod.KEY_ENTER and key.lalt:
      # Alt + Enter toggles fullscreen
      return {'fullscreen': True}
      
   elif key.vk == libtcod.KEY_ESCAPE:
      # Exit the game
      return {'exit': True}
      
   # No key pressed
   return {}