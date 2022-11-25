import core


def edgespaceship(j):
    if core.memory("position").y < 0:
        core.memory("position").y = core.WINDOW_SIZE[1]
    if core.memory("position").x < 0:
        core.memory("position").x = core.WINDOW_SIZE[1]
    if core.memory("position").y > core.WINDOW_SIZE[1]:
        core.memory("position").y = 0
    if core.memory("position").x > core.WINDOW_SIZE[1]:
        core.memory("position").x = 0


def edgeprojectiles(k):
    for p in core.memory("projectiles"):
        if p["position"].y < 0:
            p["position"].y = core.WINDOW_SIZE[1]
        if p["position"].x < 0:
            p["position"].x = core.WINDOW_SIZE[1]
        if p["position"].y > core.WINDOW_SIZE[1]:
            p["position"].y = 0
        if p["position"].x > core.WINDOW_SIZE[1]:
            p["position"].x = 0


def edgetarget(i):
    for t in core.memory("target"):
        if (t["position"].y + t["dimensionv"].y / 2) < 0:
            t["position"].y = core.WINDOW_SIZE[1] - t["dimensionv"].y / 2
        if (t["position"].x + t["dimensionv"].x / 2) < 0:
            t["position"].x = core.WINDOW_SIZE[1] - t["dimensionv"].x / 2
        if (t["position"].y + t["dimensionv"].y / 2) > core.WINDOW_SIZE[1]:
            t["position"].y = 0 - t["dimensionv"].y / 2
        if (t["position"].x + t["dimensionv"].x / 2) > core.WINDOW_SIZE[1]:
            t["position"].x = 0 - t["dimensionv"].x / 2