from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_window():
    from ..core.lighting import is_day
    from ..render.texture import city_day_tex, city_night_tex

    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glPushMatrix()

    # Window position
    z = -3.99
    y_bottom = 1.4
    y_top = 2.7
    x_left = -1.0
    x_right = 1.0

    glDisable(GL_LIGHTING)

    # ===============================
    # OUTER FRAME
    # ===============================
    glColor3f(0.3, 0.3, 0.3)
    frame_thickness = 0.12
    
    # Top frame
    glBegin(GL_QUADS)
    glVertex3f(x_left - frame_thickness, y_top, z)
    glVertex3f(x_right + frame_thickness, y_top, z)
    glVertex3f(x_right + frame_thickness, y_top + frame_thickness, z)
    glVertex3f(x_left - frame_thickness, y_top + frame_thickness, z)
    glEnd()
    
    # Bottom frame
    glBegin(GL_QUADS)
    glVertex3f(x_left - frame_thickness, y_bottom - frame_thickness, z)
    glVertex3f(x_right + frame_thickness, y_bottom - frame_thickness, z)
    glVertex3f(x_right + frame_thickness, y_bottom, z)
    glVertex3f(x_left - frame_thickness, y_bottom, z)
    glEnd()
    
    # Left frame
    glBegin(GL_QUADS)
    glVertex3f(x_left - frame_thickness, y_bottom, z)
    glVertex3f(x_left, y_bottom, z)
    glVertex3f(x_left, y_top, z)
    glVertex3f(x_left - frame_thickness, y_top, z)
    glEnd()
    
    # Right frame
    glBegin(GL_QUADS)
    glVertex3f(x_right, y_bottom, z)
    glVertex3f(x_right + frame_thickness, y_bottom, z)
    glVertex3f(x_right + frame_thickness, y_top, z)
    glVertex3f(x_right, y_top, z)
    glEnd()

    # ===============================
    # GLASS PANES (WITH TEXTURES)
    # ===============================
    glEnable(GL_TEXTURE_2D)
    tex = city_day_tex if is_day else city_night_tex
    glBindTexture(GL_TEXTURE_2D, tex)
    glColor3f(1, 1, 1)

    # Glass quad
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(x_left, y_bottom, z + 0.01)
    glTexCoord2f(1, 0); glVertex3f(x_right, y_bottom, z + 0.01)
    glTexCoord2f(1, 1); glVertex3f(x_right, y_top, z + 0.01)
    glTexCoord2f(0, 1); glVertex3f(x_left, y_top, z + 0.01)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)

    # ===============================
    # WINDOW PANE DIVIDERS (CROSS)
    # ===============================
    glColor3f(0.5, 0.5, 0.5)
    glLineWidth(2.0)

    glBegin(GL_LINES)
    # Vertical divider
    glVertex3f(0.0, y_bottom, z + 0.015)
    glVertex3f(0.0, y_top, z + 0.015)
    
    # Horizontal divider
    glVertex3f(x_left, (y_bottom + y_top) / 2, z + 0.015)
    glVertex3f(x_right, (y_bottom + y_top) / 2, z + 0.015)
    glEnd()

    glLineWidth(1.0)
    glEnable(GL_LIGHTING)

    glPopMatrix()
    glPopAttrib()

