import pygame
from random import randrange

branco = (255, 255, 255)
cinza = (205, 193, 197)
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

temporizador = pygame.time.Clock()
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake")
fonte = pygame.font.SysFont(None, 25, bold=True)


def texo(mensagem, cordotexto):
    texto1 = fonte.render(mensagem, True, cordotexto)
    fundo.blit(texto1, [largura/10, altura/2])


def cobra(cobraXY):
    for XY in cobraXY:
        pygame.draw.rect(fundo, preto, [XY[0], XY[1], tamanho, tamanho])


def aple(posicaocobra_x, posicaocobra_y):
    pygame.draw.rect(fundo, vermelho, [
                     posicaocobra_x, posicaocobra_y, tamanho, tamanho])


def jogo():
    sair = True
    fimdejogo = False
    posicaocobra_x = randrange(0, largura - tamanho, 10)
    posicaocobra_y = randrange(0, altura - tamanho, 10)
    posicaoaple_x = randrange(0, altura - tamanho, 10)
    posicaoaple_y = randrange(0, altura - tamanho, 10)
    velocidade_x = 0
    velocidade_y = 0
    correr_x = +1
    correr_y = +1
    cobraXY = []
    comprimenrodacobra = 1

    while sair:
        while fimdejogo:
            fundo.fill(branco)
            texo("Game Over, Tecle C para continuar ou Tecle S para sair", verde)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        jogo()
                        sair = True
                        fimdejogo = False
                        posicaocobra_x = randrange(0, largura - tamanho, 10)
                        posicaocobra_y = randrange(0, altura - tamanho, 10)
                        posicaoaple_x = randrange(0, altura - tamanho, 10)
                        posicaoaple_y = randrange(0, altura - tamanho, 10)
                        velocidade_x = 0
                        velocidade_y = 0
                        cobraXY = []
                        comprimenrodacobra = 1
                    if event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = - tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = - tamanho
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho
            #   if event.key == pygame.K_SPACE:
                #    posicaocobra_x += correr_x
                #    posicaocobra_y += correr_y

        if sair:
            fundo.fill(cinza)
            posicaocobra_x += velocidade_x
            posicaocobra_y += velocidade_y

            """/aqui é quando a cobra come a maçan, no caso quando os dois objetos
            se cruzam o objeto maçan some e outro aparece em outra posição"""
            if posicaocobra_x == posicaoaple_x and posicaocobra_y == posicaoaple_y:
                posicaoaple_x = randrange(0, altura - tamanho, 10)
                posicaoaple_y = randrange(0, altura - tamanho, 10)
                comprimenrodacobra += 1

            if posicaocobra_x > largura:
                posicaocobra_x = 0
            if posicaocobra_x < 0:
                posicaocobra_x = largura - tamanho
            if posicaocobra_y > altura:
                posicaocobra_y = 0
            if posicaocobra_y < 0:
                posicaocobra_y = altura - tamanho

        #    if posicaocobra_x > largura:
        #        sair = False
        #    if posicaocobra_x < 0:
        #        sair = False
        #    if posicaocobra_y > altura:
        #        sair = False
        #    if posicaocobra_y < 0:
        #        sair = False

        """/ Caso queira que o jogo finalize au inves de atravessar
        a tela de um lado para o outro quando o personagem tocar
        uma das bordas utilise os IF comentados acima, usando essa opção
        troque sair = False por fimdejogo = True para finalizar"""

        cobrainicio = []
        cobrainicio.append(posicaocobra_x)
        cobrainicio.append(posicaocobra_y)
        cobraXY.append(cobrainicio)
        if len(cobraXY) > comprimenrodacobra:
            del cobraXY[0]
        if any(Bloco == cobrainicio for Bloco in cobraXY[:-1]):
            fimdejogo = True

        cobra(cobraXY)

        aple(posicaoaple_x, posicaoaple_y)
        #   print(event)
        #   impressao dos eventos que acontece no jogo
        pygame.display.update()
        temporizador.tick(15)


jogo()
pygame.quit()
# quit()
