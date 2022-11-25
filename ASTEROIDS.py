import time
from pygame.math import Vector2
import core
from Projectiles import creationprojectiles, cleanprojectiles, drawprojectiles, projectilesmovement
from EdgeTeleportation import edgespaceship, edgetarget, edgeprojectiles
from SpaceShip import spaceshipcontrol, spaceshipparameters, drawspaceship, reset
from Target import creationtarget, targetcollision, drawtarget, targetmovement
from Regles import lifesystem, gameoverscreen, background
from Exit import exitasteroid


def setup():
    print("Setup START---------")

    core.fps = 30
    core.WINDOW_SIZE = [800, 800]
    core.memory("position", Vector2(core.WINDOW_SIZE[1]/2, core.WINDOW_SIZE[1]/2))
    core.memory("vitesse", Vector2(0.0001, -1.001))
    core.memory("velocity", Vector2())
    core.memory("inertia", Vector2(0, 0))
    core.memory("projectiles", [])
    core.memory("target", [])
    core.memory("nbrTarget", 5)
    core.memory("life", -1)
    core.memory("nbrRang3", 0)
    core.memory("nbrRang2", 0)
    core.memory("nbrRang1", 0)
    core.memory("score", 0)
    core.memory("background", 0)
    core.memory("nbrround", 1)
    core.memory("highscore", [])
    core.memory("highestscore", 0)

    print("Setup END-----------")


def run():
    exitasteroid()
    background()
    if core.memory("life") < -3:
        core.memory("life", core.memory("lifesaving3"))
    elif core.memory("life") == -3:
        core.Draw.text((255, 255, 255), "QUIT ? Y or N", (core.WINDOW_SIZE[1] / 2 - 90, core.WINDOW_SIZE[1] / 2))
        if core.getKeyPressList("y"):
            exit()
        elif core.getKeyPressList("n"):
            core.memory("life", core.memory("lifesaving2"))
    elif core.memory("life") == -1:
        core.cleanScreen()
        edgetarget(core.WINDOW_SIZE)
        creationtarget()
        targetmovement()
        drawtarget(core.memory("target"))
        core.Draw.text((255, 255, 255), "ASTEROIDS", (core.WINDOW_SIZE[1] / 2 - 90, core.WINDOW_SIZE[1] / 2 - 200))
        core.Draw.text((255, 255, 255), "Press any key to play",(core.WINDOW_SIZE[1] / 2 - 140, core.WINDOW_SIZE[1] / 2))
        core.Draw.text((255, 255, 255), "Z = Move forward", (core.WINDOW_SIZE[1] / 2 - 140, core.WINDOW_SIZE[1] / 2 + 60))
        core.Draw.text((255, 255, 255), "Q = Steer left", (core.WINDOW_SIZE[1] / 2 - 140, core.WINDOW_SIZE[1] / 2 + 90))
        core.Draw.text((255, 255, 255), "D = Steer right", (core.WINDOW_SIZE[1] / 2 - 140, core.WINDOW_SIZE[1] / 2 + 120))
        core.Draw.text((255, 255, 255), "S = Brake", (core.WINDOW_SIZE[1] / 2 - 140, core.WINDOW_SIZE[1] / 2 + 150))
        core.Draw.text((255, 255, 255), "Escape = Menu", (core.WINDOW_SIZE[1] / 2 - 140, core.WINDOW_SIZE[1] / 2 + 180))
        core.Draw.text((255, 255, 255), "B = Shox asteroid's hitboxes", (core.WINDOW_SIZE[1] / 2 - 140, core.WINDOW_SIZE[1] / 2 + 210))
        if core.getkeyPress():
            core.memory("nbrTarget", 5)
            core.memory("life", 3)
    elif core.memory("life") == -2:
        if time.time() - core.memory("nextround") > 60 / core.fps:
            reset()
            core.memory("life", core.memory("lifesaving"))
            core.memory("nbrTarget", 5)
        else:
            core.Draw.text((255, 255, 255), "Round", (core.WINDOW_SIZE[1] / 2 - 50, core.WINDOW_SIZE[1] / 2))
            core.Draw.text((255, 255, 255), str(core.memory("nbrround")), (core.WINDOW_SIZE[1] / 2 + 50, core.WINDOW_SIZE[1] / 2))
    elif core.memory("life") > 0:
        core.memory("inertia", Vector2(0, 0))
        core.cleanScreen()

        #HIGHSCORE
        core.Draw.text((255, 255, 255), str(core.memory("highestscore")), (185, 30))
        core.Draw.text((255, 255, 255), "HighScore : ", (20, 30))

        #PARAMETRES VAISSEAU
        spaceshipparameters()

        creationtarget()

        #TELEPORTATION
        edgespaceship(core.WINDOW_SIZE)
        edgetarget(core.WINDOW_SIZE)
        #edgeprojectiles(core.WINDOW_SIZE)

        #DESSIN
        drawprojectiles(core.memory("projectiles"))
        drawspaceship()
        drawtarget(core.memory("target"))

        # TIR
        if core.getKeyPressList("SPACE"):
            creationprojectiles()

        # DEPLACEMENT
        projectilesmovement()
        targetmovement()

        #COLLISIONS
        targetcollision()

        #REGLES
        lifesystem()

        #CONTROLES
        spaceshipcontrol()

        #NETTOYAGE
        cleanprojectiles()

        #RESUME


    else:
        gameoverscreen()


core.main(setup, run)
