import time

from pygame import Vector2

import core

def setup():
    print("Setup START---------")
    core.fps = 30

    core.memory("position", Vector2(400, 400))
    core.memory("vitesse", Vector2(1, 0))
    core.WINDOW_SIZE = [800, 800]
    print("Setup END-----------")


def creationProjectile():
    pass


def run():
    core.cleanScreen()


    #Tir
    if core.getKeyPressList("SPACE"):
        if len(core.memory("projectiles"))>0:
             if time.time() - core.memory("projectiles")[-1]["startime"]>0.01:
                creationProjectile()
        else :
            creationProjectile()
    #Deplacement
    core.memory("position", core.memory("position")+core.memory("vitesse"))
    for p in core.memory("projectiles"):
        p["position"]=p["position"] + p["vitesse"]

    #update
    core.memory("position", core.memory("position") + core.memory("vitesse"))

    #control
    if core.getKeyPressList("z"):
        core.memory("vitesse").scale_to_length(core.memory("vitesse").length()+5)

    if core.getKeyPressList("d"):
        core.memory("vitesse", core.memory("vitesse").rotate(5))

    print(core.memory("vitesse"))

    vectP2 = Vector2(core.memory("vitesse"))

    vectP2.scale_to_length(40)
    p2=core.memory("position") + vectP2

    vecP1 = core.memory("vitesse")
    vecP1 = vecP1.rotate(90)
    vecP1.scale_to_length(10)
    p1 = core.memory("position")+vecP1

    vecP3 = core.memory("vitesse")
    vecP3 = vecP1.rotate(-90)
    vecP3.scale_to_length(10)
    p3 = core.memory("position") + vecP3



core.main(setup, run)