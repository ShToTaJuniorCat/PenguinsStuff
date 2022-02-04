def get_neutral_from_list(game, island_list):
    all_neutral = game.get_neutral()

    for island in island_list:
        if island in all_neutral:
            return island


def is_attacked(island, game):
    for enemy_penguin_group in game.get_enemy_penguin_groups():
        if enemy_penguin_group.destination == island:
            return True

    return False


def get_close_islands(game, target_island):
    close_islands = []
    for island in game.get_all_icebergs():
        if island.get_turns_till_arrival(target_island) <= 14:
            close_islands.append(island)


def get_ally_pg_count(game, island_list):
    ally_pg = 0

    for island in island_list:
        if island.owner.id == game.get_myself().id:
            ally_pg += island.penguin_amount

    return ally_pg