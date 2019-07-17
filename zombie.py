import random

class Zombie:

  max_speed = 5
  horde = []
  plague_level = 10
  default_speed = 1
  max_strength = 8
  default_strength = 3

  def __init__(self, speed, strength):
    """Initializes zombie's speed and strength
    """
    if speed > Zombie.max_speed:
      self.speed = Zombie.default_speed
    else:
      self.speed = speed

    if strength > Zombie.max_strength:
      self.strength = Zombie.default_strength
    else:
      self.strength = strength


  def __str__(self):
      return f"Zombie with a speed of: {self.speed}, and strength of: {self.strength}"

  @classmethod
  def spawn(cls):
    """Spawns a random number of new zombies, based on the plague level,
    adding each one to the horde.  Each zombie gets a random speed.
    """
    new_zombies = random.randint(1, Zombie.plague_level)
    count = 0

    while count < new_zombies:
      speed = random.randint(1, Zombie.max_speed)
      strength = random.randint(1, Zombie.max_strength)
      Zombie.horde.append(Zombie(speed, strength))
      count += 1

  @classmethod
  def new_day(cls):
    """Represents the events of yet another day of the zombie apocalypse.
    Every day some zombies die off (phew!), some new ones show up,
    and sometimes the zombie plague level increases.
    """
    Zombie.spawn()
    Zombie.increase_plague_level()
    Zombie.some_die_off()
    

  @classmethod
  def some_die_off(cls):
    """Removes a random number (between 0 and 10) of zombies from the horde.
    """
    how_many_die = random.randint(0, 10)
    counter = 0
    while counter < how_many_die and len(Zombie.horde) > 0:
      random_zombie = random.randint(0,len(Zombie.horde) - 1)
      Zombie.horde.pop(random_zombie)
      counter += 1

  @classmethod
  def increase_plague_level(cls):
    """Increases a zombies plague level by 0-2 levels
    """
    increase = random.randint(0, 2)
    Zombie.plague_level += increase

  def encounter(self):
    """This instance method represents you coming across a zombie! This can end in three possible outcomes:
    1. You outrun the zombie and escape unscathed!
    2. You don't outrun the zombie.
    3. You didnt outrun the zombie now, you will have to fight it. Even if you win you'll catch the plague.
    4. You didn't mange to beat the zombie, now you die and join the horde. :(
    Returns a summary of what happened.
    """
    outrun = self.chase()
    fight = self.fight()
    if outrun:
      return 'You escaped!'
    else:
      if fight:
        Zombie.spawn()
        return 'You fought the zombie and caught the plague.  You are now a zombie too.  Raaaawrgh'
      else:
        return 'You died.'

  def chase(self):
    """Represents you trying to outrun this particular zombie.
    Uses `Zombie.max_speed` to generate a random number that represents how fast you manage to run.
    """
    your_speed = random.randint(1, Zombie.max_speed)
    return your_speed > self.speed

  def fight(self):
    """Represents you trying to fight this particular zomibe.
    Uses 'Zombie.max_strength' to generate a random number that represents how strong you are
    """
    your_strength = random.randint(1, Zombie.max_strength)
    return your_strength > self.strength

print(Zombie.horde) # []
Zombie.new_day()
print(Zombie.horde) # [<__main__.Zombie object at 0x7f6f594f0d30>, <__main__.Zombie object at 0x7f6f594f0b70>, <__main__.Zombie object at 0x7f6f594f0d68>]
zombie1 = Zombie.horde[0]
print(zombie1) # Speed: 1 -- Strength: 7
zombie2 = Zombie.horde[1]
print(zombie2) # Speed: 2 -- Strength: 7
print(zombie1.encounter()) # You escaped!
print(zombie2.encounter()) # You fought the zombie and caught the plague.  You are now a zombie too.  Raaaawrgh
Zombie.new_day()
print(Zombie.horde) # [<__main__.Zombie object at 0x7f6f594f0d30>, <__main__.Zombie object at 0x7f6f594efef0>, <__main__.Zombie object at 0x7f6f594f0c50>, <__main__.Zombie object at 0x7f6f594f0cc0>]
zombie1 = Zombie.horde[0]
zombie2 = Zombie.horde[1]
print(zombie1.fight())
print(zombie1.encounter()) # You died!
print(zombie2.encounter()) # You escaped!