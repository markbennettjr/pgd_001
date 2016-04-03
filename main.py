# Companion code for part 1 of the Pragmatic Game Development Tutorials
# TODO: article link

from enum import Enum


class Fire_Gun_Return(Enum):
    no_los = -1
    no_ammo = -2


class GameObject(object):
    def get_position(self):
        return (1.0, 1.0, 1.0)

# Representsa 3rd-party library for projectiles
class ProjectileManager(object):
    def launch_projectile(self, damage, start, end):
        pass


class Map(object):
    def check_los(self, start, end):
        return True


class Weapon(object):
    def __init__(self):
        self._ammo = 5
        self._damage = 8

    def get_ammo(self):
        return self._ammo

    def get_damage(self):
        return self._damage

    def decrease_ammo(self, amount):
        self._ammo = self._ammo - amount


class GameManager(object):
    def __init__(self):
        self._projectile_manager = ProjectileManager()
        self._map = Map()

    def get_enemy_by_id(self, eid):
        return GameObject()

    def get_projectile_manager(self):
        return self._projectile_manager

    def get_map(self):
        return self._map


class Player(GameObject):
    def __init__(self, renderable, game_manager, weapon):
        self._game_manager = game_manager
        self._renderable = renderable
        self._primary_weapon = weapon
        self._position = (0.0, 1.0, 2.0)
        self._current_target_id = 2

    def fire_gun(self):
        target = self._game_manager.get_enemy_by_id(self._current_target_id)

        if not self._game_manager.get_map().check_los(
                self._position,
                target.get_position()):
            return Fire_Gun_Return.no_los

        if self._primary_weapon.get_ammo() <= 0:
            return Fire_Gun_Return.no_ammo

        damage = self._primary_weapon.get_damage()

        self._game_manager.get_projectile_manager().launch_projectile(
            damage, self._position, target.get_position())

        self._primary_weapon.decrease_ammo(1)

        return damage


# main:
if __name__ == "__main__":
    gm = GameManager()
    w = Weapon()
    player = Player(None, gm, w)

    damage = player.fire_gun()
    if damage > 0:
        print "Bang! You lost {} HP".format(damage)
    elif damage == -1:
        print "You can't see that guy!"
    elif damage == -2:
        print "You are out of ammo"
