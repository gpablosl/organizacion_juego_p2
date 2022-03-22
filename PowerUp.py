from OpenGL.GL import *
from glew_wish import *
from Modelo import *

class PowerUp(Modelo):

    presente = True

    def __init__(self):
        super().__init__()
        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_inferior = 0.15
        self.extremo_superior = 0.05

    def dibujar(self):
        if self.presente: 
            glPushMatrix()
            glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
            glScalef(4,4,0)
            glBegin(GL_POLYGON)
            glColor3f(0.43, 0.81, 0.95)
            glVertex3f(0.0,0.0,0.0)
            glVertex3f(0.01,-0.01,0.0)
            glVertex3f(0.0,-0.03,0.0)
            glVertex3f(-0.01,-0.01,0.0)
            glEnd()
            glPopMatrix()
