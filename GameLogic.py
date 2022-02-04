"""
This is an example for a bot.
"""
from IslandCluster import *
from penguin_game import *
from IslandServices import *


def do_turn(game):
    """
    cluster = IslandCluster(game.get_my_icebergs())
    print("hello")
    close = cluster.best_island_choice()

    # for my_iceberg in game.get_my_icebergs(): close

    surrounding_icebergs = cluster.get_close_islands()

    if not is_attacked(my_iceberg) and surrounding_icebergs_status() != "enemy":
        close_neutral = get_neutral_from_list(surrounding_icebergs, game)
        if my_iceberg.penguin_amount > my_iceberg.upgrade_cost:
            my_iceberg.upgrade()
        elif is_attacked(close_neutral) and
         close_neutral.penguin_amount < get_ally_pg_count(game, surrounding_icebergs):
            close_neutral.send_penguins(close_neutral, occupation(close_neutral))
    """

    for island in game.get_my_icebergs():
        cluster = IslandCluster(game.get_my_icebergs())

        if type(cluster.is_attacked(game)) == Iceberg:
            print("AHHH!!!")

            # Tell me who's attacked, exactly
            attacked = cluster.is_attacked(game)

            # Can we defend it?
            for enemy_penguin_group in game.get_enemy_penguin_groups():
                if enemy_penguin_group.destination is attacked:
                    attacker = enemy_penguin_group


        else:
            island.send_penguins(cluster.best_island_choice(game),
                                                 cluster.island_list[0].penguin_amount)
            print("Phew!")


def occupation(game, i_island):
    # If island is my island
    for my_islands in game.get_my_icebergs():
        if my_islands == i_island:
            raise Exception

    current_amount_pg = i_island.penguin_amount
    if game.get_enemy() == i_island.owner():
        # time_pg_dilver_arrive = 0
        amount_pg_to_i_island = 0
        for enemy_islandPgGr in game.get_enemy_penguin_groups():
            if enemy_islandPgGr.destination == i_island:
                # time_pg_dilver_arrive = enemy_islandPgGr.turns_till_arrival
                amount_pg_to_i_island = enemy_islandPgGr.penguin_amount
        island_level = i_island.level
        amount_pg_be_there = amount_pg_to_i_island + (island_level * current_amount_pg)
        return amount_pg_be_there + 1
    else:
        return current_amount_pg + 1


def surrounding_icebergs_status(game, surrounding_icebergs):
    result = ""

    for iceberg in surrounding_icebergs:
        temp = iceberg
        if temp != iceberg.owner.id:
            return "none"
        elif iceberg.owner.id == game.get_neutral().id:
            result = "neutral"

        elif iceberg.owner.id == game.get_enemy().id:
            result = "enemy"

        elif iceberg.owner.id == game.get_myself().id:
            result = "ally"

    return result


def get_neutral_from_list(game, island_list):
    all_neutral = game.get_neutral()

    for island in island_list:
        if island in all_neutral:
            return island
