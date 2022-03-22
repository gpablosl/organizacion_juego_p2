from OpenGL.GL import *
from glew_wish import *
from Modelo import *
from random import random

class Boss(Modelo):

    velocidad = 2.8
    def __init__(self):
        super().__init__()
        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_inferior = 0.05
        self.extremo_superior = 0.05

    def actualizar(self,tiempo_delta):
        cantidad_movimiento = self.velocidad * tiempo_delta
        if self.direccion == 0:
            self.posicion_x = self.posicion_x - cantidad_movimiento
        elif self.direccion == 1:
            self.posicion_x = self.posicion_x + cantidad_movimiento
        if self.posicion_x <= -0.8 and self.direccion == 0:
            self.direccion = 1
        if self.posicion_x >= 0.8 and self.direccion == 1:
            self.direccion = 0

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
        glScalef(5,5,0)
        glBegin(GL_POLYGON)
        glColor3f(0.25, 0, random())
        glVertex3f(-0.01,0.01,0.0)
        glVertex3f(0.00,0.01,0.0)
        glVertex3f(0.01,-0.00,0.0)
        glVertex3f(0.01,-0.01,0.0)
        glVertex3f(0.0,-0.02,0.0)
        glVertex3f(-0.01,-0.02,0.0)
        glVertex3f(-0.02,-0.01,0.0)
        glVertex3f(-0.02,-0.00,0.0)
        glEnd()
        glPopMatrix()