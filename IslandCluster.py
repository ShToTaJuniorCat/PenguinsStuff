from IslandServices import is_attacked


class IslandCluster:
	# island_list is a list of all island currently in the cluster.
	def __init__(self, island_list):
		self.island_list = island_list

	def is_in_cluster(self, island):
		return island in self.island_list

	def add_island_to_cluster(self, island):
		self.island_list.append(island)

	def best_island_choice(self, game):
		# All islands we may conquer. Practically all islands that are not mine
		possible_islands = game.get_enemy_icebergs() + game.get_neutral_icebergs()
		# Each island in the cluster adds the best island for it to send.
		# distance: island
		best_islands = {}

		# Run over all islands in the cluster
		# For each one, add the best island choice to the cluster
		for island in self.island_list:
			# Distances from all the other islands
			# distance: island
			island_distances = {}
			# Run over all possible islands and add distance to them from current island
			for target_island in possible_islands:
				# Add distance
				island_distances[island.get_turns_till_arrival(target_island)] = target_island

			best_island_distance = min(island_distances.keys())
			best_islands[best_island_distance] = island_distances[best_island_distance]

		best_island_distance = min(best_islands.keys())
		return best_islands[best_island_distance]

	def is_attacked(self, game):
		for island in self.island_list:
			if is_attacked(island, game):
				# AAHHAHHAHAHHAHAHHHHHHHHHHH WE ARE UNDER FUCKING ATTACK!!!!!!!!!!!!!
				return island

		return False
