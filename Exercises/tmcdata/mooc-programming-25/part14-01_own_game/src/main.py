import pygame
from random import randint

class HumbleBot(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, coin_group, door_group, game):
        super().__init__()
        #Define image
        self.base_image = pygame.image.load("robot.png").convert_alpha()
        self.image = self.base_image
        #Get our rectangle
        self.rect = self.image.get_rect()
        # Position the Robot
        self.rect.topleft = (x,y)
        # Other variables
        self.velocity = 10
        self.wallet = 1
        self.lives = 2
        self.is_spinning = False
        #Control variables
        self.target_x = 0
        self.target_y = 0
        self.coin_group = coin_group
        self.door_group = door_group
        self.game = game
        self.can_retire = False
    
    def update(self):
        # self.adjust_velocity()
        self.move()
        self.check_retirement_elegible()
        self.check_collisions()
        

    def adjust_velocity(self):
        self.velocity = self.velocity - (self.wallet%10)
    
    def move(self, to_left, to_right, to_up, to_down):
        v = self.velocity - (self.wallet//10)
        if to_left:  self.rect.x -= v
        if to_right: self.rect.x += v
        if to_up:    self.rect.y -= v
        if to_down:  self.rect.y += v

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.right > self.game.screen.get_width():
            self.rect.right = self.game.screen.get_width()
        if self.rect.bottom > self.game.screen.get_height():
            self.rect.bottom = self.game.screen.get_height()
    
    def check_collisions(self):
        if pygame.sprite.spritecollide(self, self.coin_group, True):
            self.wallet += 1
            self.rescale(1+(self.wallet/70))
        if pygame.sprite.spritecollide(self, self.door_group, False):
            if self.can_retire:
                self.velocity = 0
                self.kill()  
                self.game.retire_timer = 90

    def check_retirement_elegible(self):
        if self.wallet >= 67:
            self.can_retire = True
    
    def rescale(self, scale):
        w, h = self.base_image.get_size()
        new_w = max(1, int(w * scale))
        new_h = max(1, int(h * scale))
        self.image = pygame.transform.smoothscale(self.base_image, (new_w, new_h))
        center = self.rect.center
        self.rect = self.image.get_rect(center=center)

    def wallet_to_scale(wallet, min_w=1, max_w=100, min_s=0.5, max_s=2.0):
        t = max(0.0, min(1.0, (wallet - min_w) / (max_w - min_w)))
        return min_s + (max_s - min_s) * t


class Monster(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, target: HumbleBot, player_group, game):
        super().__init__()
        #Define image
        self.image = pygame.image.load("monster.png")
        #Get our rectangle
        self.rect = self.image.get_rect()
        # Position the Monster
        self.rect.topleft = (x,y)
        # Other variables
        self.velocity = randint(1,2)
        # self.y_velocity = randint(1,3)
        # Robot target
        self.target = target
        self.player_group = player_group
        self.game = game
    
    def update(self):
        self.move()
        self.check_collisions()

    def move(self):
        if self.rect.x < self.target.rect.x:
            self.rect.x += self.velocity 
        if self.rect.x > self.target.rect.x:
            self.rect.x -= self.velocity

        if self.rect.y < self.target.rect.y:
            self.rect.y += self.velocity
        if self.rect.y > self.target.rect.y:
            self.rect.y -= self.velocity


    def check_collisions(self):
        if pygame.sprite.spritecollide(self, self.player_group, True):
            self.game.game_over_flag = True

class Coin(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        #Define image
        self.image = pygame.image.load("coin.png")
        #Get our rectangle
        self.rect = self.image.get_rect()
        # Position the Coin
        self.rect.topleft = (x,y)
        # Other variables
        self.velocity = 0      
    
    def update(self):
        self.rect.x += randint(-5,5)
        self.rect.y += randint(-5,5)

class Door(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        #Define image
        self.image = pygame.image.load("door.png")
        #Get our rectangle
        self.rect = self.image.get_rect()
        # Position the Door
        self.rect.topleft = (x,y)

class Game:
    def __init__(self):
        pygame.init()
        pygame.FULLSCREEN
        self.screen_width = 0
        self.screen_height = 0
        self.screen=pygame.display.set_mode([self.screen_width, self.screen_height])
        self.window_w = self.screen.get_width()
        self.window_h = self.screen.get_height()
        pygame.display.set_caption("HumbleBot Wants To Retire Alive")
        self.font = pygame.font.SysFont(None, 36)
        self.big_font = pygame.font.SysFont(None, 72)
        self.game_font = pygame.font.SysFont("Arial", 24)
        self.clock = pygame.time.Clock()
        self.running = True
        self.debug = True
        self.reset()
        self.main_loop()

    def reset(self):
        self.game_over_flag = False
        self.retired_flag = False
        self.retire_timer = 0
        # Create monster group
        self.monster_group = pygame.sprite.Group()
        # Create door group
        self.door_group = pygame.sprite.Group()
        #Create Player Group
        self.player_group = pygame.sprite.Group()
        #Create Player Group
        self.coin_group = pygame.sprite.Group()
        # Create MC and add to group
        self.player = HumbleBot(0,0,self.coin_group, self.door_group, self)
        self.player_group.add(self.player)
        # Create retirement Door and add to group
        self.door = Door(self.window_w//2,self.window_h//2)
        self.door_group.add(self.door)
        # Create several monsters and add to group
        for i in range (5):
            monster = Monster(randint(100,self.screen.get_width()-50), randint(100,self.screen.get_height()-50), self.player, self.player_group, self)
            self.monster_group.add(monster)
        # Create several coins and add to group
        for i in range (100):
            coin = Coin(randint(0,self.screen.get_width()-50), randint(0,self.screen.get_height()-50))
            self.coin_group.add(coin)
        self.to_right = self.to_left = self.to_up = self.to_down = False

    def main_loop(self):
        while self.running:
            self.clock.tick(60)
            self.check_events()
            self.player.check_retirement_elegible()
            self.player.move(self.to_left, self.to_right, self.to_up, self.to_down) 
            self.player.check_collisions()
            self.update_monsters()
            self.update_coins()
            self.draw_window()
            if self.game_over_flag:
                self.game_over()
            if self.retire_timer > 0:       
                self.retire_timer -= 1
                if self.retire_timer == 0:
                    self.retire()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:   self.to_left = True
                if event.key == pygame.K_RIGHT:  self.to_right = True
                if event.key == pygame.K_UP:     self.to_up = True
                if event.key == pygame.K_DOWN:   self.to_down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:   self.to_left = False
                if event.key == pygame.K_RIGHT:  self.to_right = False
                if event.key == pygame.K_UP:     self.to_up = False
                if event.key == pygame.K_DOWN:   self.to_down = False
            if event.type == pygame.QUIT:
                exit()
    
    def game_over(self):
        self.screen.fill((255, 160, 122))
        text = self.big_font.render("MONSTERS ATE YOU BEFORE RETIREMENT :(", True, (200, 0, 0))
        restart_text = self.font.render("Press R to restart or Q to quit", True, (255, 255, 255))
        self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2,
                                self.screen.get_height() // 2 - text.get_height() // 2))
        self.screen.blit(restart_text, (self.screen.get_width() // 2 - restart_text.get_width() // 2,
                                        self.screen.get_height() // 2 + 50))
        pygame.display.flip()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset()
                        return
                    if event.key == pygame.K_q:
                        exit()
                if event.type == pygame.QUIT:
                    exit()

    def retire(self):
        self.screen.fill('green')
        text = self.big_font.render("CONGRATS YOU RETIRED!!!!! ALIVE!!", True, (200, 0, 0))
        restart_text = self.font.render("Press R to restart or Q to quit", True, (255, 255, 255))
        self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2,
                                self.screen.get_height() // 2 - text.get_height() // 2))
        self.screen.blit(restart_text, (self.screen.get_width() // 2 - restart_text.get_width() // 2,
                                        self.screen.get_height() // 2 + 50))
        pygame.display.flip()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset()
                        return
                    if event.key == pygame.K_q:
                        exit()
                if event.type == pygame.QUIT:
                    exit()

    def update_monsters(self):
        self.monster_group.update()

    def update_coins(self):
        self.coin_group.update()

    def draw_hud(self):
        text = self.game_font.render(f"Wallet: {self.player.wallet}", True, (255, 0, 0))
        self.screen.blit(text, (self.screen.get_width()-400, 30))

        if self.debug:
            speed = self.game_font.render(f"Player Speed: {self.player.velocity - (self.player.wallet//10)} km/h", True, (255, 0, 0))
            self.screen.blit(speed, (self.screen.get_width()-400, 60))
            max_monster_speed = self.game_font.render(f"Max Monster Speed: {max(self.monster_group.sprites(),key=lambda m: m.velocity).velocity} km/h", True, (255, 0, 0))
            self.screen.blit(max_monster_speed, (self.screen.get_width()-400, 90))


    def draw_window(self):
        #Screen color
        self.screen.fill("silver")

        #Draw Player, Monsters and Coins
        self.monster_group.draw(self.screen)
        self.door_group.draw(self.screen)
        self.player_group.draw(self.screen)
        self.coin_group.draw(self.screen)
        
        self.draw_hud()
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()