#pip install pyopengl
#pip install glfw
from cmath import cos, pi, sin
from scipy import rand
from Bicho import *
from OpenGL.GL import *
from glew_wish import *
import glfw
from Nave import *
from Boss import *
from PowerUp import *
from Fondo import *

window = None
nave = Nave()
boss = Boss()
fondo = Fondo()
powerUp = PowerUp()
bichos = [Bicho(0.55, 0.55),Bicho(-0.55, -0.55),Bicho(0.55, -0.55),Bicho(-0.55, 0.55),Bicho(-0.35, 0.0),Bicho(0.35, 0.0)]
tiempo_anterior = 0.0 
bicho_contador = 0

def actualizar():
    global tiempo_anterior
    global window
    global bicho_contador
    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior
    boss.actualizar(tiempo_delta)

    nave.actualizar(window, tiempo_delta)
    for bicho in bichos:
        if bicho.vivo:
            bicho.actualizar()
            if bicho.colisionando(nave):
                    bicho.vivo = False
                    bicho_contador = bicho_contador + 1
                    print(bicho_contador)
                    if bicho_contador == 6:
                        glfw.set_window_should_close(window, 1)

    if nave.colisionando(powerUp):
        nave.velocidad = nave.velocidad * 1.15
        powerUp.presente = False
    tiempo_anterior = tiempo_actual
    if nave.colisionando(boss):
        glfw.set_window_should_close(window, 1)

    
def colisionando():
    colisionando = False
    return colisionando

def colisionando_power_up():
    colisionandoP = False
    if (nave.posicion_x[0] + 0.05 >= powerUp.posicion_x - 0.05 
        and nave.posicion_x[0] - 0.05 <= powerUp.posicion_x + 0.05 
        and nave.posicion_y + 0.05 >= powerUp.posicion_y - 0.05 
        and nave.posicion_y - 0.05 <= powerUp.posicion_y + 0.05):
        colisionandoP = True 
    return colisionandoP

def draw():
    fondo.dibujar()
    for bicho in bichos:
        bicho.dibujar()
    #draw_bala()
    nave.dibujar()
    boss.dibujar()
    powerUp.dibujar()



def main():
    global window
    width = 700
    height = 700
    if not glfw.init():
        return

    window = glfw.create_window(width, height, "Mi ventana", None, None)

    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glewExperimental = True

    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    version = glGetString(GL_VERSION)
    print(version)


    while not glfw.window_should_close(window):
        glClearColor(0.22,0.58,0.2,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        actualizar()
        draw()
        glfw.poll_events()
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()
