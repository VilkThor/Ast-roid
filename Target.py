import random
import time
import pygame.transform
from pygame import Rect
from pygame.math import Vector2
import core


def creationtarget():
    if core.memory("nbrTarget") == 0:
        core.memory("nbrround", core.memory("nbrround") + 1)
        core.memory("nextround", time.time())
        core.memory("lifesaving", core.memory("life"))
        core.memory("life", -2)
    for t in range(0, core.memory("nbrTarget")):
        t = {}
        t["position"] = Vector2(random.randint(0, core.WINDOW_SIZE[1]), random.randint(0, core.WINDOW_SIZE[1]))
        t["rang"] = random.randint(1, 3)
        t["dimension"] = (t["rang"] * 50, t["rang"] * 50)
        t["dimensionv"] = Vector2(t["dimension"])
        t["milieu"] = Vector2(t["dimensionv"].x/2, t["dimensionv"].y/2)
        t["vitesse"] = Vector2(random.uniform(-3, 3), random.uniform(-3, 3))
        core.memory("tRect", Rect(t["position"], t["dimension"]))

        if t["vitesse"].x == 0:
            t["vitesse"].x = random.uniform(-3, 3)
        if t["vitesse"].y == 0:
            t["vitesse"].y = random.uniform(-3, 3)

        t["lengthlist"] = len(core.memory("target"))
        core.memory("target").append(t)

        if t["lengthlist"] == core.memory("nbrTarget"):
            core.memory("target").remove(t)


def targetmovement():
    for t in core.memory("target"):
        t["position"] = t["position"] + t["vitesse"]


def rotatetarget(n):
    core.memory("asteroidR", pygame.image.load("./asteroid150.png"))
    pygame.transform.rotate(core.memory("asteroidR"), n)


def drawtarget(t):
    for t in core.memory("target"):
        if core.getKeyPressList("b"):
            core.Draw.rect((255, 0, 0), (t["position"], t["dimension"]), 0)
            core.Draw.rect((0, 255, 0), (t["position"], t["dimension"]), 0)
            core.Draw.rect((0, 0, 255), (t["position"], t["dimension"]), 0)
        elif t["rang"] == 3:
            core.memory("pAsteroid150", Vector2(t["position"].x, t["position"].y))
            core.memory("asteroid150", core.Texture("./asteroid150.png", core.memory("pAsteroid150"), 0, (150, 150)))
            if not core.memory("asteroid150").ready:
                core.memory("asteroid150").load()
            core.memory("asteroid150").show()
        elif t["rang"] == 2:
            core.memory("pAsteroid100", Vector2(t["position"].x, t["position"].y))
            core.memory("asteroid100", core.Texture("./asteroid100.png", core.memory("pAsteroid100"), 0, (100, 100)))
            if not core.memory("asteroid100").ready:
                core.memory("asteroid100").load()
            core.memory("asteroid100").show()
        else:
            core.memory("pAsteroid50", Vector2(t["position"].x, t["position"].y))
            core.memory("asteroid50", core.Texture("./asteroid50.png", core.memory("pAsteroid50"), 0, (50, 50)))
            if not core.memory("asteroid50").ready:
                core.memory("asteroid50").load()
            core.memory("asteroid50").show()


def targetdivision():
    if core.memory("rangD") == 3:
        core.memory("nbrTarget", core.memory("nbrTarget") + 2)

        t = {}
        t["position"] = core.memory("positionD")
        t["rang"] = 2
        t["dimension"] = (t["rang"] * 50, t["rang"] * 50)
        t["vitesse"] = Vector2(random.uniform(-5, 0), random.uniform(-5, 5))
        t["dimensionv"] = Vector2(t["dimension"])

        if t["vitesse"].x == 0:
            t["vitesse"].x = random.uniform(-5, 0)
        if t["vitesse"].y == 0:
            t["vitesse"].y = random.randint(-5, 5)

        t["lengthlist"] = len(core.memory("target"))
        core.memory("target").append(t)

        t = {}
        t["position"] = core.memory("positionD")
        t["rang"] = 2
        t["dimension"] = (t["rang"] * 50, t["rang"] * 50)
        t["vitesse"] = Vector2(random.uniform(0, 5), random.uniform(-5, 5))
        t["dimensionv"] = Vector2(t["dimension"])

        if t["vitesse"].x == 0:
            t["vitesse"].x = random.uniform(0, 5)
        if t["vitesse"].y == 0:
            t["vitesse"].y = random.uniform(-5, 5)

        t["lengthlist"] = len(core.memory("target"))
        core.memory("target").append(t)
        if t["lengthlist"] == core.memory("nbrTarget"):
            core.memory("target").remove(t)
    if core.memory("rangD") == 2:
        core.memory("nbrTarget", core.memory("nbrTarget") + 2)

        t = {}
        t["position"] = core.memory("positionD")
        t["rang"] = 1
        t["dimension"] = (t["rang"] * 50, t["rang"] * 50)
        t["vitesse"] = Vector2(random.uniform(-8, 0), random.uniform(-8, 8))
        t["dimensionv"] = Vector2(t["dimension"])

        if t["vitesse"].x == 0:
            t["vitesse"].x = random.uniform(-8, 0)
        if t["vitesse"].y == 0:
            t["vitesse"].y = random.uniform(-8, 8)

        t["lengthlist"] = len(core.memory("target"))
        core.memory("target").append(t)

        t = {}
        t["position"] = core.memory("positionD")
        t["rang"] = 1
        t["dimension"] = (t["rang"] * 50, t["rang"] * 50)
        t["vitesse"] = Vector2(random.uniform(0, 8), random.uniform(-8, 8))
        t["dimensionv"] = Vector2(t["dimension"])

        if t["vitesse"].x == 0:
            t["vitesse"].x = random.uniform(0, 8)
        if t["vitesse"].y == 0:
            t["vitesse"].y = random.uniform(-8, 8)

        t["lengthlist"] = len(core.memory("target"))
        core.memory("target").append(t)
        if t["lengthlist"] == core.memory("nbrTarget"):
            core.memory("target").remove(t)


def targetcollision():
    for t in core.memory("target"):
        core.memory("tRect", Rect(t["position"], t["dimension"]))
        for p in core.memory("projectiles"):
            if core.memory("tRect").collidepoint(p["position"]):
                core.memory("nbrTarget", core.memory("nbrTarget") - 1)
                core.memory("score", core.memory("score") + 1)
                core.memory("target").remove(t)
                core.memory("projectiles").remove(p)
                core.memory("rangD", t["rang"])
                core.memory("positionD", t["position"])
                targetdivision()
    core.Draw.text((255, 255, 255), "Score : ", (20, 0))
    core.Draw.text((255, 255, 255), str(core.memory("score")), (120, 0))


def cleantarget():
    core.memory("nbrTarget", 5)
    for t in core.memory("target"):
        core.memory("target").remove(t)
