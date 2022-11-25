import time
from pygame.math import Vector2
import core


def creationprojectiles():
    if len(core.memory("projectiles")) == 0:
        p = {}
        p["position"] = Vector2(core.memory("P2"))
        p["vitesse"] = Vector2(core.memory("vitesse"))
        p["vitesse"].scale_to_length(20)
        p["rayon"] = 2
        p["StartTime"] = time.time()
        core.memory("pCircle", p["position"])
        core.memory("projectiles").append(p)
    else:
        if time.time() - core.memory("projectiles")[-1]["StartTime"] > 0.3:
            p = {}
            p["position"] = Vector2(core.memory("P2"))
            p["vitesse"] = Vector2(core.memory("vitesse"))
            p["vitesse"].scale_to_length(20)
            p["rayon"] = 2
            p["StartTime"] = time.time()
            core.memory("pCircle", p["position"])
            core.memory("projectiles").append(p)


def projectilesmovement():
    for p in core.memory("projectiles"):
        p["position"] = p["position"] + p["vitesse"]


def drawprojectiles(p):
    for p in core.memory("projectiles"):
        core.Draw.circle((255, 165, 0), p["position"], p["rayon"])


def cleanprojectiles():
    for p in core.memory("projectiles"):
        if time.time() - p["StartTime"] > 30 / core.fps:
            core.memory("projectiles").remove(p)
