import pygame
from random import randint

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

try:
    pygame.init()
except print:
    print("Não Iniciou")

largura = 640
altura = 480
tamanho = 10
posicao_x = randint(0, (largura - tamanho)/10)*10
posicao_y = randint(0, (altura - tamanho)/10)*10
velocidade_x = 0
velocidade_y = 0

fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

sair = True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocidade_y = 0
                velocidade_x = - 0.2
            if event.key == pygame.K_RIGHT:
                velocidade_y = 0
                velocidade_x = 0.2
            if event.key == pygame.K_UP:
                velocidade_x = 0
                velocidade_y = - 0.2
            if event.key == pygame.K_DOWN:
                velocidade_x = 0
                velocidade_y = 0.2
    fundo.fill(branco)
    pygame.draw.rect(fundo, preto, [posicao_x, posicao_y, tamanho, tamanho])
    posicao_x += velocidade_x
    posicao_y += velocidade_y
    # print(event)
    """/impressao dos eventos que acontece
        no jogo"""

    pygame.display.update()

# pygame.quit()
# quit()
