from screeninfo import get_monitors
import pygame


class Config:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self._initialized = True
            
            # debug
            self.__debug_mode = True
            
            # monitor
            self.__user_screen = get_monitors()[0]
            self.__monitor_width = self.__user_screen.width
            self.__monitor_height = self.__user_screen.height
            
            # fps
            self.__clock = pygame.time.Clock()
            self.__max_fps = 60

            # wallpaper
            self.__wallpaper_sprite = pygame.image.load('./sprites/scenario/background.bmp')
            self.__scaled_wallper_sprite = pygame.transform.scale(
                self.__wallpaper_sprite,
                (
                    self.__monitor_height,
                    self.__monitor_width,
                )
            )
            
            # ground
            self.__ground_sprite = pygame.image.load('./sprites/scenario/ground.bmp')
            self.__ground_sprite_rect = self.__ground_sprite.get_rect()
            
            # pipe
            self.__pipe_sprite = pygame.image.load('./sprites/pipe/pipe.png')
            self.__pipe_sprite_rect = self.__pipe_sprite.get_rect()

            # bird
            self.__bird_downflap_sprite = pygame.image.load('./sprites/bird/downflap.bmp')
            self.__bird_midflap_sprite = pygame.image.load('./sprites/bird/midflap.bmp')
            self.__bird_upflap_sprite = pygame.image.load('./sprites/bird/upflap.bmp')
            self.__bird_rect = self.__bird_midflap_sprite.get_rect()
            
            # GAME screen
            self.__game_screen = None

    def get_monitor(self):
        return {
            "width": self.__monitor_width,
            "height": self.__monitor_height,
        }

    def get_wallpaper(self):
        return {
            "sprite": {
                "default": self.__wallpaper_sprite,
                "scaled": self.__scaled_wallper_sprite,
            },
        }        

    def get_ground(self): 
        return {
            "sprite": self.__ground_sprite,
            "width": self.__ground_sprite_rect.width,
            "height": self.__ground_sprite_rect.height,
        }
        
    def get_pipe(self):
        return {
            "sprite": {
                "default": self.__pipe_sprite,
                "rotated": pygame.transform.rotate(
                    self.__pipe_sprite,
                    180,
                ),
            },
            "width": self.__pipe_sprite_rect.width,
            "height": self.__pipe_sprite_rect.height,
        }
    
    def get_bird(self):
        return {
            "sprites": {
                "downflap": self.__bird_downflap_sprite,
                "midflap": self.__bird_midflap_sprite,
                "upflap": self.__bird_upflap_sprite,
            },
            "width": self.__bird_rect.width,
            "height": self.__bird_rect.height
        }

    def start_screen(self):
        self.__game_screen = pygame.display.set_mode((
            self.__monitor_width,
            self.__monitor_height,
        ))
        
    def get_screen(self):
        return {
            "surface": self.__game_screen,
            "width": self.__game_screen.get_width(),
            "height": self.__game_screen.get_height()
        }
    
    def clock_tick(self, framerate):
        return self.__clock.tick(framerate)

    def get_max_fps(self):
        return self.__max_fps
    
    def get_fps(self):
        return self.__clock.get_fps()
    
    def get_is_debugging(self):
        return self.__debug_mode
    
    def toggle_debug(self):
        print("me ativou")
        self.__debug_mode = not self.__debug_mode
