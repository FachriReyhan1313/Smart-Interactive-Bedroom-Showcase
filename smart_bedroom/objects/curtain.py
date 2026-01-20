from OpenGL.GL import *
import math

from ..render import texture

curtain_open = None


def draw_curtain():
    from ..core.lighting import is_day
    
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glPushMatrix()

    # Determine coverage
    if curtain_open is None:
        cover = 0.35 if is_day else 1.0
    else:
        cover = curtain_open

    glEnable(GL_LIGHTING)
    glEnable(GL_TEXTURE_2D)
    
    if texture.curtain_tex is not None:
        glBindTexture(GL_TEXTURE_2D, texture.curtain_tex)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    glColor3f(1.0, 1.0, 1.0)

    # Constants
    z = -3.95
    y_bottom = 1.4
    y_top = 2.7
    folds = 8
    wave_amp = 0.15
    fold_width = 0.08
    
    extend_dist = cover
    step = extend_dist / folds

    # LEFT CURTAIN
    for i in range(folds):
        x0 = -1.0 + i * step
        x1 = -1.0 + (i + 1) * step
        bulge = wave_amp * (1.0 if i % 2 == 0 else -0.7)
        u0 = i / folds
        u1 = (i + 1) / folds

        glBegin(GL_QUADS)
        glTexCoord2f(u0, 0); glVertex3f(x0, y_bottom, z)
        glTexCoord2f(u1, 0); glVertex3f(x1, y_bottom, z)
        glTexCoord2f(u1, 1); glVertex3f(x1, y_top, z)
        glTexCoord2f(u0, 1); glVertex3f(x0, y_top, z)
        glEnd()
        
        glDisable(GL_TEXTURE_2D)
        glColor3f(0.4, 0.35, 0.3)
        glBegin(GL_QUADS)
        glVertex3f(x1 - fold_width/2, y_bottom, z)
        glVertex3f(x1 + fold_width/2, y_bottom, z + bulge)
        glVertex3f(x1 + fold_width/2, y_top, z + bulge)
        glVertex3f(x1 - fold_width/2, y_top, z)
        glEnd()
        
        glColor3f(0.95, 0.9, 0.85)
        glBegin(GL_QUADS)
        glVertex3f(x1, y_bottom, z)
        glVertex3f(x1 + fold_width/2, y_bottom, z + bulge)
        glVertex3f(x1 + fold_width/2, y_top, z + bulge)
        glVertex3f(x1, y_top, z)
        glEnd()
        
        glColor3f(1.0, 1.0, 1.0)
        glEnable(GL_TEXTURE_2D)

    # RIGHT CURTAIN
    for i in range(folds):
        x0 = 1.0 - i * step
        x1 = 1.0 - (i + 1) * step
        bulge = wave_amp * (1.0 if i % 2 == 0 else -0.7)
        u0 = i / folds
        u1 = (i + 1) / folds

        glBegin(GL_QUADS)
        glTexCoord2f(u0, 0); glVertex3f(x0, y_bottom, z)
        glTexCoord2f(u1, 0); glVertex3f(x1, y_bottom, z)
        glTexCoord2f(u1, 1); glVertex3f(x1, y_top, z)
        glTexCoord2f(u0, 1); glVertex3f(x0, y_top, z)
        glEnd()
        
        glDisable(GL_TEXTURE_2D)
        glColor3f(0.4, 0.35, 0.3)
        glBegin(GL_QUADS)
        glVertex3f(x1 + fold_width/2, y_bottom, z)
        glVertex3f(x1 - fold_width/2, y_bottom, z + bulge)
        glVertex3f(x1 - fold_width/2, y_top, z + bulge)
        glVertex3f(x1 + fold_width/2, y_top, z)
        glEnd()
        
        glColor3f(0.95, 0.9, 0.85)
        glBegin(GL_QUADS)
        glVertex3f(x1, y_bottom, z)
        glVertex3f(x1 - fold_width/2, y_bottom, z + bulge)
        glVertex3f(x1 - fold_width/2, y_top, z + bulge)
        glVertex3f(x1, y_top, z)
        glEnd()
        
        glColor3f(1.0, 1.0, 1.0)
        glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)

    glPopMatrix()
    glPopAttrib()
