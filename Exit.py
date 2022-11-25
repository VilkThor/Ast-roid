import core


def exitasteroid():
    if core.getKeyPressList("ESCAPE"):
        core.memory("lifesaving2", core.memory("life"))
        core.memory("life", -3)
