from pygame.math import Vector2
import core


def reset():
    core.memory("lifesaving3", core.memory("life"))
    core.memory("position", Vector2(400, 400))
    core.memory("vitesse", Vector2(0.00001, -1.0001))


def inertia(x, y):
    core.memory("inertia", core.memory("inertia") + (x, y))
    core.memory("vitesse", core.memory("vitesse") + core.memory("inertia"))


def accelerate(x):
    core.memory("vitesse").scale_to_length(core.memory("vitesse").length() + x)


def rotate(r):
    core.memory("vitesse", core.memory("vitesse").rotate(r))


def move():
    core.memory("position", core.memory("position") + core.memory("vitesse"))


def spaceshipcontrol():
    if core.getKeyPressList("z"):
        accelerate(0.4)
        #inertia(0.4, 0)
        #flame()
    if core.getKeyPressList("s"):
        core.memory("vitesse", Vector2(0.0001, 0.0001))
    if core.getKeyPressList("d"):
        rotate(6)
        #inertia(0, 0.4)
    if core.getKeyPressList("q"):
        rotate(-6)
        #inertia(0, -0.4)
    if core.getKeyPressList("r"):
        reset()
    print(core.memory("inertia"))


def spaceshipparameters():
    move()

    vectP3 = core.memory("vitesse")
    vectP3 = vectP3.rotate(-90)
    vectP3.scale_to_length(10)
    P3 = core.memory("position") + vectP3
    core.memory("P3", P3)

    vectP1 = core.memory("vitesse")
    vectP1 = vectP1.rotate(90)
    vectP1.scale_to_length(10)
    P1 = core.memory("position") + vectP1
    core.memory("P1", P1)

    vectP2 = Vector2(core.memory("vitesse"))
    vectP2.scale_to_length(40)
    P2 = core.memory("position") + vectP2
    core.memory("P2", P2)


def flame():
    move()

    vectP6 = core.memory("vitesse")
    vectP6 = vectP6.rotate(-90)
    vectP6.scale_to_length(-5)
    P6 = core.memory("position") + vectP6
    core.memory("P6", P6)

    vectP4 = core.memory("vitesse")
    vectP4 = vectP4.rotate(90)
    vectP4.scale_to_length(-5)
    P4 = core.memory("position") + vectP4
    core.memory("P4", P4)

    vectP5 = Vector2(core.memory("vitesse"))
    vectP5.scale_to_length(-20)
    P5 = core.memory("position") + vectP5
    core.memory("P5", P5)

    core.Draw.polygon((255, 165, 0), (P4, P5, P6), 0)


def drawspaceship():
    core.Draw.polygon((255, 0, 255), (core.memory("P1"), core.memory("P2"), core.memory("P3")), 0)
