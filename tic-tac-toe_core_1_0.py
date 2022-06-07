def print_grid(game_grid: list):
    print('---------')
    for row in game_grid:
        print('|', *row, '|')
    print('---------')


def unscript_grit(cells_string: str):
    cells_iterable = iter(cells_string)
    game_grid = []
    for row in range(3):
        game_grid.append([])
        for column in range(3):
            game_grid[row].append(next(cells_iterable))
    return game_grid


def wins_check(game_grid, char):
    line_list = []
    grid_size = len(game_grid[0])
    for row in game_grid:
        line_list.append(row)
    for column_number in range(grid_size):
        column = [row[column_number] for row in game_grid]
        line_list.append(column)
    if game_grid[1][1] == char:
        diagonal1 = [game_grid[index][index] for index in range(grid_size)]
        line_list.append(diagonal1)
        diagonal2 = [
            game_grid[index][grid_size - 1 - index] for index in range(grid_size)
        ]
        line_list.append(diagonal2)
    for line in line_list:
        if all(item == char for item in line):
            return True


def get_players_move(game_grid):
    row, column = None, None
    while not row and not column:
        try:
            row, column = (int(item) - 1 for item in input().split())
        except (IndexError, ValueError):
            print("You should enter numbers!")
        else:
            try:
                char_chosen = game_grid[row][column]
            except (ValueError, IndexError):
                print('Coordinates should be from 1 to 3!')
            else:
                if char_chosen in ('X', 'O'):
                    print('This cell is occupied! Choose another one!')
                else:
                    return row, column
        row, column = None, None


def game_end_check(game_grid, char):
    if wins_check(game_grid, char):
        return char + ' wins'
    if all(all(char != "_" for char in row) for row in game_grid):
        return 'Draw'


def main():
    PLAYERS_SIGN_DICT = {
        False: 'O',
        True: 'X',
    }
    game_grid = unscript_grit('_________')
    print_grid(game_grid)
    stop_game = False
    player = True
    while not stop_game:
        char = PLAYERS_SIGN_DICT.get(player)
        row, column = get_players_move(game_grid)
        game_grid[row][column] = char
        print_grid(game_grid)
        result = game_end_check(game_grid, char)
        if result:
            print(result)
            stop_game = True
        player = not player


if __name__ == "__main__":
    main()
