MAX_CUBES_RED, MAX_CUBES_GREEN, MAX_CUBES_BLUE = 12, 13, 14

def get_input():
    games = []

    with open("input/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if line: games.append(line)
    
    return games

def parse_game_cubes(game):
    game_parts = game.split(": ")

    game_index = int(game_parts[0].split(" ")[1])

    game_sets = game_parts[1].split("; ")

    for curr_set in game_sets:
        set_parts = curr_set.split(", ")

        for cube in set_parts:
            cube_parts = cube.split(" ")

            if cube_parts[1] == "red":
                if not (int(cube_parts[0]) <= MAX_CUBES_RED):
                    return -1
            
            elif cube_parts[1] == "green":
                if not (int(cube_parts[0]) <= MAX_CUBES_GREEN):
                    return -1
            
            else:
                if not (int(cube_parts[0]) <= MAX_CUBES_BLUE):
                    return -1
    
    return game_index

def main():
    valid_game_indexes = []

    games = get_input()

    for game in games:
        res = parse_game_cubes(game)

        if res > 0:
            valid_game_indexes.append(res)
        
    print (valid_game_indexes)
    print (sum(valid_game_indexes))

if __name__ == "__main__":
    main()