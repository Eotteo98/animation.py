import pgzrun
import random
import itertools

WIDTH = 400
HEIGHT = 400

BLOCK_POSITIONS = [
    (40,40), (360,40), (40,360), (360, 360)
] 

block_positions = itertools.cycle(BLOCK_POSITIONS)

ship = Actor("ship.png")
block = Actor("block.png")

def draw():
    screen.clear()
    screen.blit("space", (0,0))
    ship.draw()
    block.draw()

def move_block():
    animate(block, "bounce_end", duration = 1, pos = next(block_positions))


move_block()

clock.schedule_interval(move_block, 1)

def ship_angles():
    x = random.randint(0,360)
    y = random.randint(0,360)
    ship.target = x,y
    target_angle = ship.angle_to(ship.target)
    target_angle += 360 * ((ship.angle - target_angle + 180)/ 360)
    animate(ship, angle = target_angle, duration = 0.5, on_finished = move_ship())

def move_ship():
    animate(ship, tween = "accel_decel", pos = ship.target, duration = ship.distance_to(ship.target) / 200, on_finished = ship_angles)

ship_angles()



pgzrun.go()