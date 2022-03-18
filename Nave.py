#La nomenclatura indica que la primera letra del nombre de una clase va en mayusculas
from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Modelo import *

class Nave(Modelo):

    velocidad_rotacion = 270.0
    fase = 90.0
    herido = False

    def __init__(self):
        super().__init__(0.0,-0.8,0.0,1.2,0.0)
        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_inferior = 0.05
        self.extremo_superior = 0.05

    def dibujar(self):
        
        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
        glRotatef(self.direccion, 0.0, 0.0, 1.0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.6,0.1,1)
        glVertex3f(0.0,0.05,0)
        glColor3f(0,0.3,1)
        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0.05,-0.05,0)
        glEnd()
        glPopMatrix()

    def actualizar(self, window, tiempo_delta ):
        #Leer los estados de las teclas que queremos
        estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)
        estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
        estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)


        #Revisamos estados y realizamos acciones
        cantidad_movimiento = self.velocidad * tiempo_delta
        if estado_tecla_arriba == glfw.PRESS:
            self.posicion_x = self.posicion_x + (
                math.cos((self.direccion + self.fase) * math.pi / 180.0) * cantidad_movimiento
            )
            self.posicion_y = self.posicion_y + (
                math.sin((self.direccion + self.fase) * math.pi / 180.0) * cantidad_movimiento
            )

        cantidad_rotacion = self.velocidad_rotacion * tiempo_delta
        if estado_tecla_izquierda == glfw.PRESS:
            self.direccion = self.direccion + cantidad_rotacion
            if self.direccion > 360.0:
                self.direccion = self.direccion - 360.0 
        if estado_tecla_derecha == glfw.PRESS:
            self.direccion = self.direccion - cantidad_rotacion
            if self.direccion < 0.0:
                self.direccion = self.direccion + 360.0


        if self.posicion_x > 1.05: 
            self.posicion_x = -1.0
        if self.posicion_x < -1.05: 
            self.posicion_x = 1.0
            
        if self.posicion_y > 1.05: 
            self.posicion_y = -1.0   
        if self.posicion_y < -1.05: 
            self.posicion_y = 1.0  

