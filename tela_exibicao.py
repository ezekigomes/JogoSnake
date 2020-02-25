import pygame

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
posicao_x = largura/2
posicao_y = altura/2
tamanho = 10

fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

sair = True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
    fundo.fill(branco)
    pygame.draw.rect(fundo, preto, [posicao_x, posicao_y, tamanho, tamanho])

    # print(event)
    """/impressao dos eventos que acontece
        no jogo"""

    pygame.display.update()

# pygame.quit()
# quit()
