'''pygame.mouse.set_cursor()

Pygame Cursor Constant           Description
--------------------------------------------
pygame.SYSTEM_CURSOR_ARROW       arrow
pygame.SYSTEM_CURSOR_IBEAM       i-beam
pygame.SYSTEM_CURSOR_WAIT        wait
pygame.SYSTEM_CURSOR_CROSSHAIR   crosshair
pygame.SYSTEM_CURSOR_WAITARROW   small wait cursor
                                 (or wait if not available)
pygame.SYSTEM_CURSOR_SIZENWSE    double arrow pointing
                                 northwest and southeast
pygame.SYSTEM_CURSOR_SIZENESW    double arrow pointing
                                 northeast and southwest
pygame.SYSTEM_CURSOR_SIZEWE      double arrow pointing
                                 west and east
pygame.SYSTEM_CURSOR_SIZENS      double arrow pointing
                                 north and south
pygame.SYSTEM_CURSOR_SIZEALL     four pointed arrow pointing
                                 north, south, east, and west
pygame.SYSTEM_CURSOR_NO          slashed circle or crossbones
pygame.SYSTEM_CURSOR_HAND        hand

for example:
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)'''


# import pygame as pg
# import sys

# WHITE = (255, 255, 255)
# RED = (225, 0, 50)
# GREEN = (0, 225, 0)
# BLUE = (0, 0, 225)

# sc = pg.display.set_mode((400, 300))
# sc.fill(WHITE)
# pg.display.update()

# while 1:
#     for i in pg.event.get():
#         if i.type == pg.QUIT:
#             sys.exit()
#         if i.type == pg.MOUSEBUTTONDOWN:
#             if i.button == 1:
#                 pg.draw.circle(sc, RED, i.pos, 20)
#                 # pg.display.update()
#             elif i.button == 3:
#                 pg.draw.circle(sc, BLUE, i.pos, 20)
#                 pg.draw.rect(sc, GREEN,
#                              (i.pos[0] - 10,
#                               i.pos[1] - 10, 20, 20))
#                 # pg.display.update()
#             elif i.button == 2:
#                 sc.fill(WHITE)
#                 # pg.display.update()
#     pg.display.update()

#     pg.time.delay(20)
#----------------------------------------------------------

# import pygame as pg
# import sys

# WHITE = (255, 255, 255)
# BLUE = (0, 0, 225)

# sc = pg.display.set_mode((400, 300))
# sc.fill(WHITE)
# pg.display.update()

# while 1:
#     for i in pg.event.get():
#         if i.type == pg.QUIT:
#             sys.exit()

#     pressed = pg.mouse.get_pressed()
#     pos = pg.mouse.get_pos()
#     if pressed[0]:
#         pg.draw.circle(sc, BLUE, pos, 5)
#         pg.display.update()

#     pg.time.delay(20)

#----------------------------------------------------------

# import pygame as pg
# import sys

# WHITE = (255, 255, 255)
# BLUE = (0, 0, 225)

# pg.init()
# sc = pg.display.set_mode((400, 300))
# sc.fill(WHITE)
# pg.display.update()

# pg.mouse.set_visible(False)

# while 1:
#     for i in pg.event.get():
#         if i.type == pg.QUIT:
#             sys.exit()

#     sc.fill(WHITE)

#     if pg.mouse.get_focused():
#         pos = pg.mouse.get_pos()
#         pg.draw.rect(
#             sc, BLUE, (pos[0] - 10,
#                        pos[1] - 10,
#                        20, 20))

#     pg.display.update()
#     pg.time.delay(20)
