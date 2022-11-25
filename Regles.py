from pygame import Rect
from SpaceShip import reset
from Target import targetdivision, cleantarget
import core


def lifesystem():
    core.Draw.text((255, 255, 255), "Lives :", (220, 0))
    core.Draw.text((255, 255, 255), str(core.memory("life")), (320, 0))
    for t in core.memory("target"):
        core.memory("tRect", Rect(t["position"], t["dimension"]))
        if core.memory("tRect").collidepoint(core.memory("position")):
            core.memory("nbrTarget", core.memory("nbrTarget") - 1)
            core.memory("life", core.memory("life") - 1)
            core.memory("score", core.memory("score") + 1)
            core.memory("target").remove(t)
            core.memory("rangD", t["rang"])
            core.memory("positionD", t["position"])
            targetdivision()
            reset()


def gameoverscreen():
    core.Draw.text((255, 255, 255), "GAME OVER", (core.WINDOW_SIZE[1] / 2 - 80, core.WINDOW_SIZE[1] / 2 - 150))
    core.Draw.text((255, 255, 255), "Score : ", (core.WINDOW_SIZE[1] / 2 - 80, core.WINDOW_SIZE[1] / 2 - 100))
    core.Draw.text((255, 255, 255), str(core.memory("score")), (core.WINDOW_SIZE[1] / 2 + 20, core.WINDOW_SIZE[1] / 2 - 100))
    core.Draw.text((255, 255, 255), "Press SPACE to play again", (core.WINDOW_SIZE[1] / 2 - 180, core.WINDOW_SIZE[1] / 2))
    if core.getKeyPressList("SPACE"):
        core.memory("highscore").append(core.memory("score"))
        core.memory("highestscore", max(core.memory("highscore")))
        cleantarget()
        core.memory("life", 3)
        core.memory("score", core.memory("score") - core.memory("score"))


def background():
    core.memory("background", core.Texture("./espace1.png", (1, 1), 0, (1440, 800)))
    if not core.memory("background").ready:
        core.memory("background").load()
    core.memory("background").show()
