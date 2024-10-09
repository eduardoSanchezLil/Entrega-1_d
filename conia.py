import pygame
import sys

# Funciones del programa
def calculoDeLaSuperficieALimpiar(listaDeZonas):
    superficieALimpiar = sum(zona['largo'] * zona['ancho'] for zona in listaDeZonas) / 10000  # m2
    return superficieALimpiar

def tiempoLimpiezaEnMinutos(superficieALimpiar, tiempoParaUnMetroCuadrado):
    return round(superficieALimpiar * tiempoParaUnMetroCuadrado)

def mostrar_texto(screen, texto, pos, color=(0, 0, 0)):
    font = pygame.font.SysFont(None, 36)
    texto_superficie = font.render(texto, True, color)
    screen.blit(texto_superficie, pos)

# Inicialización de pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simulador de Aspiradora")
clock = pygame.time.Clock()

# Configuración de las zonas
zona1 = {"largo": 500, "ancho": 150}
zona2 = {"largo": 309, "ancho": 480}
zona3 = {"largo": 101, "ancho": 480}
zona4 = {"largo": 90, "ancho": 220}
zonas = [zona1, zona2, zona3, zona4]

# Cálculos
superficieALimpiar = calculoDeLaSuperficieALimpiar(zonas)
tiempoEstimado = tiempoLimpiezaEnMinutos(superficieALimpiar, 2)

# Mensaje de advertencia
if tiempoEstimado > 55:
    print("robot_aspirador dice: ¡Me parece que esto va a tardar un poco!")

# Posición inicial de la aspiradora
aspiradora_x = 50
aspiradora_y = 50
move_direction = 1  # 1: derecha, -1: izquierda

# Bucle principal de pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar la posición de la aspiradora
    aspiradora_x += move_direction * 2
    if aspiradora_x > 750 or aspiradora_x < 50:
        move_direction *= -1  # Cambiar dirección

    # Dibujar las zonas
    screen.fill((255, 255, 255))  # Fondo blanco
    for idx, zona in enumerate(zonas):
        largo = zona['largo'] / 10
        ancho = zona['ancho'] / 10
        pygame.draw.rect(screen, (173, 216, 230), (10, 10 + idx * 60, largo, ancho))

    # Dibujar la aspiradora
    pygame.draw.circle(screen, (255, 0, 0), (aspiradora_x, aspiradora_y), 20)

    # Mostrar el tiempo estimado de limpieza
    mostrar_texto(screen, f"Tiempo estimado: {tiempoEstimado} minutos", (10, 10))

    pygame.display.flip()
    clock.tick(60)  # Limitar a 60 FPS

pygame.quit()
sys.exit()

