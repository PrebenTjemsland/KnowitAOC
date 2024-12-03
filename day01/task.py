blanket_pattern = [
    " xxx ",
    "xxxxx",
    "xxxxx",
    "xxxxx",
    "xxxxx",
    "  x  ",
    "xxxxx",
    "xxxxx",
    "xxxxx",
    "xxxxx",
    " xxx "
]

joe_grid = [
   "   222 ",
   "  11111",
   "  11111",
   "  11111",
   "   111 ",
   "    2  ",
   "   121 ",
   "  12221",
   " 1122211",
   " 1122211",
   " 1122211",
   " 1222211",
   " 1223211",
   " 1233211",
   " 1233211",
   " 1233211",
   " 1223211",
   " 2122212",
   " 3112113",
   "  11 11",
   "  12 21",
   "  12 21",
   "  22 22",
   "  23 32",
   "  23 32",
   "  23 32",
   "  23 32",
   "  23 32",
   "6332 2336"
]

def sum_covered_numbers(blanket_pattern, joe_grid, offset_row, offset_col):
    joe_rows, joe_cols = len(joe_grid), len(joe_grid[0])
    blanket_rows, blanket_cols = len(blanket_pattern), len(blanket_pattern[0])
    total_sum = 0

    for row in range(blanket_rows):
        for col in range(blanket_cols):
            grid_row = offset_row + row
            grid_col = offset_col + col
            if 0 <= grid_row < joe_rows and 0 <= grid_col < joe_cols:
                if blanket_pattern[row][col] != ' ':
                    cell_value = joe_grid[grid_row][grid_col]
                    if cell_value.isdigit():
                        total_sum += int(cell_value)

    return total_sum

def find_max_sum(blanket_pattern, joe_grid):
    max_sum = 0
    max_offset_row = 0
    max_offset_col = 0
    joe_rows, joe_cols = len(joe_grid), len(joe_grid[0])
    blanket_rows, blanket_cols = len(blanket_pattern), len(blanket_pattern[0])

    for offset_row in range(joe_rows - blanket_rows + 1):
        for offset_col in range(joe_cols - blanket_cols + 1):
            current_sum = sum_covered_numbers(blanket_pattern, joe_grid, offset_row, offset_col)
            if current_sum > max_sum:
                max_sum = current_sum
                max_offset_row = offset_row
                max_offset_col = offset_col

    return max_sum, max_offset_row, max_offset_col

max_sum, max_offset_row, max_offset_col = find_max_sum(blanket_pattern, joe_grid)

print("Maximum sum covered by blanket: ", max_sum)