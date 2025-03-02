import pygame
from pygame.locals import *
import sys
import random

# Pygameの初期化
pygame.init()

# 定数の定義
WIDTH = 800  # 画面の幅
HEIGHT = 600  # 画面の高さ
FPS = 60  # フレームレート
PLAYER_SPEED = 5  # プレイヤーの移動速度
ENEMY_SPEED = 3  # 敵の移動速度
ENEMY_SPAWN_INTERVAL = 1000  # 敵の出現間隔（ミリ秒）

# 画面とクロックの設定
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")
clock = pygame.time.Clock()

# プレイヤーのクラス
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # 50x50の四角形
        self.image.fill((0, 255, 0))  # 緑色
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)  # 画面中央に配置
        self.direction = pygame.math.Vector2(0, 0)  # 移動方向

    def update(self):
        # 移動方向に基づいて位置を更新
        self.rect.x += self.direction.x * PLAYER_SPEED
        self.rect.y += self.direction.y * PLAYER_SPEED
        # 画面外に出ないように制限
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# 敵のクラス
class Enemy(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((30, 30))  # 30x30の四角形
        self.image.fill((255, 0, 0))  # 赤色
        self.rect = self.image.get_rect()
        # ランダムな出現位置（画面外）
        side = random.choice(["left", "right", "top", "bottom"])
        if side == "left":
            self.rect.x = -50
            self.rect.y = random.randint(0, HEIGHT)
        elif side == "right":
            self.rect.x = WIDTH + 50
            self.rect.y = random.randint(0, HEIGHT)
        elif side == "top":
            self.rect.x = random.randint(0, WIDTH)
            self.rect.y = -50
        else:  # bottom
            self.rect.x = random.randint(0, WIDTH)
            self.rect.y = HEIGHT + 50
        self.player = player  # プレイヤーの参照を保持

    def update(self):
        # プレイヤー方向に移動
        direction = self.player.rect.center - self.rect.center
        if direction.length() > 0:  # ゼロ除算を防ぐ
            direction = direction.normalize()
        self.rect.x += direction.x * ENEMY_SPEED
        self.rect.y += direction.y * ENEMY_SPEED

# スプライトグループの作成
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# プレイヤーのインスタンス作成
player = Player()
all_sprites.add(player)

# 敵の出現タイマー
enemy_timer = 0

# ゲームループ
running = True
while running:
    # イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            # キーが押されたら移動方向を更新
            if event.key == K_LEFT:
                player.direction.x = -1
            elif event.key == K_RIGHT:
                player.direction.x = 1
            elif event.key == K_UP:
                player.direction.y = -1
            elif event.key == K_DOWN:
                player.direction.y = 1
        elif event.type == KEYUP:
            # キーが離されたら移動を停止
            if event.key in (K_LEFT, K_RIGHT):
                player.direction.x = 0
            if event.key in (K_UP, K_DOWN):
                player.direction.y = 0

    # 状態更新
    all_sprites.update()

    # 敵の出現
    current_time = pygame.time.get_ticks()
    if current_time - enemy_timer > ENEMY_SPAWN_INTERVAL:
        enemy = Enemy(player)
        all_sprites.add(enemy)
        enemies.add(enemy)
        enemy_timer = current_time

    # 衝突検出
    if pygame.sprite.spritecollideany(player, enemies):
        running = False  # 衝突したらゲーム終了

    # 描画
    screen.fill((0, 0, 0))  # 背景を黒で塗りつぶし
    all_sprites.draw(screen)  # すべてのスプライトを描画
    pygame.display.flip()  # 画面を更新

    # フレームレートの制御
    clock.tick(FPS)

# ゲーム終了処理
pygame.quit()
sys.exit()