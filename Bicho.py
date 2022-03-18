from msilib.schema import Directory
from re import M
from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Modelo import *

class Bicho(Modelo):

    vivo = True

    def __init__(self, x, y):
        super().__init__(x,y)
        self.extremo_izquierdo = 0.07
        self.extremo_derecho = 0.07
        self.extremo_inferior = 0.07
        self.extremo_superior = 0.07
        
    def actualizar (self):
        if self.vivo:
            if self.posicion_x > 1.05: 
                self.posicion_x = -1.0
            if self.posicion_x < -1.05: 
                self.posicion_x = 1.0
                
            if self.posicion_y > 1.05: 
                self.posicion_y = -1.0   
            if self.posicion_y < -1.05: 
                self.posicion_y = 1.0  

    def dibujar(self):
        if self.vivo:
            glPushMatrix()
            glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
            glBegin(GL_POLYGON)
            glColor3f(.75,0.18,.38)
            glVertex3f(-0.02*2.5,0.01*2.5,0)
            glVertex3f(-0.01*2.5,0.0,0)
            glVertex3f(-0.02*2.5,-0.01*2.5,0)
            glVertex3f(-0.0,-0.03*2.5,0)
            glVertex3f(0.02*2.5,-0.01*2.5,0)
            glVertex3f(0.01*2.5,0.00,0)
            glVertex3f(0.02*2.5,0.01*2.5,0)
            glVertex3f(0.00,0.03*2.5,0)
            glEnd()

            glPopMatrix()
            
            self.dibujar_bounding_box()