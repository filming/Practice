MAX_CUBES_RED, MAX_CUBES_GREEN, MAX_CUBES_BLUE = 12, 13, 14

def get_input():
    games = []

    with open("input/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if line: games.append(line)
    
    return games

def parse_game_cubes(game):
    fewest_red_cubes, fewest_green_cubes, fewest_blue_cubes = 0, 0, 0

    game_parts = game.split(": ")

    game_index = int(game_parts[0].split(" ")[1])

    game_sets = game_parts[1].split("; ")

    for curr_set in game_sets:
        set_parts = curr_set.split(", ")

        for cube in set_parts:
            cube_parts = cube.split(" ")

            if cube_parts[1] == "red":
                cube_count = int(cube_parts[0])
                if cube_count > fewest_red_cubes:
                    fewest_red_cubes = cube_count

            elif cube_parts[1] == "green":
                cube_count = int(cube_parts[0])
                if cube_count > fewest_green_cubes:
                    fewest_green_cubes = cube_count
            
            else:
                cube_count = int(cube_parts[0])
                if cube_count > fewest_blue_cubes:
                    fewest_blue_cubes = cube_count
    
    return fewest_red_cubes * fewest_green_cubes * fewest_blue_cubes

def main():
    game_set_powers = []

    games = get_input()

    for game in games:
        res = parse_game_cubes(game)

        if res > 0:
            game_set_powers.append(res)
        
    print (game_set_powers)
    print (sum(game_set_powers))

if __name__ == "__main__":
    main()