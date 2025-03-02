class Enemy(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.rect = self.image.get_rect()
        self.rect.x = -50  # 画面外から出現
        self.rect.y = random.randint(0, HEIGHT)
        self.entered_screen = False  # 画面内に入ったかどうかのフラグ

    def update(self):
        # プレイヤー方向に移動
        direction = pygame.math.Vector2(self.player.rect.center) - pygame.math.Vector2(self.rect.center)
        if direction.length() > 0:
            direction = direction.normalize()
        self.rect.x += direction.x * ENEMY_SPEED
        self.rect.y += direction.y * ENEMY_SPEED

        # 画面内に入ったか確認
        if not self.entered_screen:
            if 0 <= self.rect.left and self.rect.right <= WIDTH and 0 <= self.rect.top and self.rect.bottom <= HEIGHT:
                self.entered_screen = True

        # 画面内に入った後で画面外に出たら消滅
        if self.entered_screen:
            if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.bottom < 0 or self.rect.top > HEIGHT:
                self.kill()