import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEAD
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.backgrounds.background_manager import BackgroundManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components import text_utils

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = -70 #-70 #380
        self.x_pos_cl = 200
        self.y_pos_cl = 180
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.background_manager = BackgroundManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.death_counter = 0
        self.dead_check = 0
        self.max = 0
        self.bg_Music = pygame.mixer.Sound("dino_runner/assets/Ost/main_ost.mp3")
        self.end_bg_Music = pygame.mixer.Sound("dino_runner/assets/Ost/end_ost.mp3")

    def run(self):

        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False 
                pygame.quit()
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.end_bg_Music.stop()
                self.bg_Music.play()
                self.reset()

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input)
            self.obstacle_manager.update(self.game_speed, self.player)
            self.background_manager.update(self.game_speed, self.player)
            self.power_up_manager.update(self.game_speed, self.points, self.player)
            self.points += 1 
            if self.points % 200 == 0:
                self.game_speed += 1
            if self.player.allow_dead:
                self.bg_Music.stop()
                self.player.image = DEAD[self.dead_check]
                if self.player.death_sound == False:
                    self.player.death_sfx.play()
                    self.player.death_sound = True
                self.dead_check +=1
                self.points -=1
                pygame.time.delay(1000)
                if self.dead_check >=2:
                    self.death_counter +=1
                    self.playing = False
                    self.end_bg_Music.play()
                    self.player.dino_dead = True

    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            self.screen.fill((255, 255, 255))
            self.draw_background()
            self.player.draw(self.screen)
            self.draw_score()
            self.obstacle_manager.draw(self.screen)
            self.background_manager.draw(self.screen)
            self.power_up_manager.draw(self.screen)
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def draw_score (self):
        self.time = self.player.left+1
        score, score_rect = text_utils.get_message('Points: ' + str(self.points), 20, 1000, 40)
        power, power_rect = text_utils.get_message('Power Up Time Left: ' + str(self.player.left), 20, 130, 40)
        self.screen.blit(score, score_rect)
        if self.player.left > 0:
            self.screen.blit(power, power_rect)

    def draw_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_element()

    def print_menu_element(self):
        if self.death_counter == 0:    
            text, text_rect = text_utils.get_message("Press any key to start!", 30, )
            self.screen.blit(text,text_rect)
        else:
            if self.points > self.max:
                self.max = self.points
            text, text_rect = text_utils.get_message("Press any key to Restart!", 30, height = SCREEN_HEIGHT//2 - 50)
            score, score_rect = text_utils.get_message("Your score is " + str(self.points), 30, height = SCREEN_HEIGHT//2 - 5)
            deaths, deaths_rect = text_utils.get_message("Deaths = " + str(self.death_counter), 30, height = SCREEN_HEIGHT//2 + 40)
            max, max_rect = text_utils.get_message("Your max score is " + str(self.max), 30, height = SCREEN_HEIGHT//2 + 85)
            self.screen.blit(max,max_rect)
            self.screen.blit(text,text_rect)
            self.screen.blit(score,score_rect)
            self.screen.blit(deaths,deaths_rect)

    def reset(self):
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.background_manager = BackgroundManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.dead_check = 0
        self.death_sound = False