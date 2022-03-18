from OpenGL.GL import *
from glew_wish import *

class Fondo():
    
    def dibujar(self):
        glBegin(GL_LINE_LOOP)
        glColor3f(0.0,0.0,0.0)
        glVertex3f(-0.9,-0.9,0.0)
        glVertex3f(0.9,-0.9,0.0)
        glVertex3f(0.9,0.9,0.0)
        glVertex3f(-0.9, 0.9,0.0)
        glVertex3f(-0.9,-0.9,0.0)
        glEnd()
        #wall 1
        glBegin(GL_QUADS)
        glColor3f(0.4,0.65,0.15)
        glVertex3f(-1,-1,0)
        glVertex3f(-1,1,0)
        glVertex3f(-0.9,1,0)
        glVertex3f(-0.9, -1,0.0)
        glEnd()
        #wall 2
        glBegin(GL_QUADS)
        glColor3f(0.28,0.7,0.17)
        glVertex3f(-1,1,0)
        glVertex3f(-1,0.9,0)
        glVertex3f(1,0.9,0)
        glVertex3f(1,1,0.0)
        glEnd()
        #wall 3
        glBegin(GL_QUADS)
        glColor3f(0.42,0.65,0.22)
        glVertex3f(-1,-1,0)
        glVertex3f(-1,-0.9,0)
        glVertex3f(1,-0.9,0)
        glVertex3f(1,-1,0.0)
        glEnd()
        #wall 4
        glBegin(GL_QUADS)
        glColor3f(0.28,0.5,0.17)
        glVertex3f(1,-1,0)
        glVertex3f(1,1,0)
        glVertex3f(0.9,1,0)
        glVertex3f(0.9, -1,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.40,0.53,0)
        glVertex3f(-1,1.56,0)
        glVertex3f(-1.0,0.5,0)
        glVertex3f(-0.5, 0.5,.0)
        glVertex3f(-0.5,1,0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.53,0.44,0.2)
        glVertex3f(1,-1.0,0)
        glVertex3f(1.0,-0.5,0)
        glVertex3f(0.5, -0.5,.0)
        glVertex3f(0.5,-1,0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.3,0.45,0.1)
        glVertex3f(0.4,-0.5,0)
        glVertex3f(0.4,-0.2,0)
        glVertex3f(0.5, -0.3,.0)
        glVertex3f(0.7,-0.4,0)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0.3,0.45,0.1)
        glVertex3f(0.2,0.4,0)
        glVertex3f(0.2,0.2,0)
        glVertex3f(-0.2,0.2,0)
        glVertex3f(-0.2, 0.4,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.3,0.7,0.9)
        glVertex3f(-0.1,-0.9,0)
        glVertex3f(0.1,-0.9,0)
        glVertex3f(0.1, -0.7,0.0)
        glVertex3f(-0.1,-0.7,0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.2,0.55,0.15)
        glVertex3f(-0.4,0.5,0)
        glVertex3f(-0.45,0.2,0)
        glVertex3f(-0.6,0.4,0)
        glVertex3f(-0.5, 0.3,.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.34,0.7,0.342)
        glVertex3f(0.56,0.56,0)
        glVertex3f(0.56,0.21,0)
        glVertex3f(0.21, 0.21,.0)
        glVertex3f(0.21,0.56,0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.25,0.5,0.22)
        glVertex3f(-0.36,-0.36,0)
        glVertex3f(-0.36,-.11,0)
        glVertex3f(-0.11, -0.11,.0)
        glVertex3f(-0.11,-0.36,0)
        glEnd()


        glBegin(GL_TRIANGLES)
        glColor3f(0.27,0.68,0.22)
        glVertex3f(-0.85, -0.74,.0)
        glVertex3f(-0.66,-.80,0)
        glVertex3f(-0.76,-0.87,0)
        glEnd()


        glBegin(GL_POLYGON)
        glColor3f(0.6,0.4,0.22)
        glVertex3f(-0.0, -0.0,.0)
        glVertex3f(0.01*3,-0.01*3,0.0)
        glVertex3f(0.0,-0.02*3,0.0)
        glVertex3f(0.02*3, -0.05*3,.0)
        glVertex3f(0.05*3,-0.06*3,0)
        glVertex3f(0.0,-0.1*3,0)
        glVertex3f(-0.05*3,-0.06*3,0)
        glVertex3f(-0.02*3, -0.05*3,.0)
        glVertex3f(-0.02*3,-0.02*3,0.0)
        glVertex3f(-0.01*3,-0.01*3,0.0)
        glEnd()