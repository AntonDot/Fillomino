def draw_simple_hex_board(board):
    CELL_WIDTH = 2
    CELL_HEIGHT = 1

    Q_VEC_X = CELL_WIDTH // 2
    Q_VEC_Y = -CELL_HEIGHT

    R_VEC_X = -CELL_WIDTH // 2
    R_VEC_Y = -CELL_HEIGHT

    min_screen_x_start = float('inf')
    max_screen_x_start = float('-inf')
    min_screen_y_start = float('inf')
    max_screen_y_start = float('-inf')

    for q, r in board.keys():
        screen_x_origin = q * Q_VEC_X + r * R_VEC_X
        screen_y_origin = q * Q_VEC_Y + r * R_VEC_Y

        min_screen_x_start = min(min_screen_x_start, screen_x_origin)
        max_screen_x_start = max(max_screen_x_start, screen_x_origin)
        min_screen_y_start = min(min_screen_y_start, screen_y_origin)
        max_screen_y_start = max(max_screen_y_start, screen_y_origin)

    total_canvas_width = max_screen_x_start - min_screen_x_start + CELL_WIDTH
    total_canvas_height = max_screen_y_start - min_screen_y_start + CELL_HEIGHT

    canvas = [[' ' for _ in range(total_canvas_width)] for _ in
              range(total_canvas_height)]

    for (q, r), value in board.items():
        raw_x = q * Q_VEC_X + r * R_VEC_X
        raw_y = q * Q_VEC_Y + r * R_VEC_Y

        draw_x = raw_x - min_screen_x_start
        draw_y = raw_y - min_screen_y_start

        val_str = str(value)
        if len(val_str) > CELL_WIDTH:
            padded_val = val_str[:CELL_WIDTH]
        else:
            padded_val = val_str.ljust(CELL_WIDTH)

        for i in range(
                len(padded_val)):
            if (0 <= draw_y < total_canvas_height and
                    0 <= draw_x + i < total_canvas_width):
                canvas[draw_y][draw_x + i] = padded_val[i]

    output_lines = ["".join(row) for row in canvas]
    print("\n".join(output_lines))


def draw_hex_board(board): #неправильные оси, но вроде красивое
    HEX_ART_WIDTH = 7
    HEX_ART_HEIGHT = 4

    X_STEP_Q = HEX_ART_WIDTH - 2

    Y_STEP_R = HEX_ART_HEIGHT - 1

    X_SHIFT_R = X_STEP_Q // 2

    min_screen_x = float('inf')
    max_screen_x = float('-inf')
    min_screen_y = float('inf')
    max_screen_y = float('-inf')

    for q, r in board.keys():
        screen_x_origin = q * X_STEP_Q + r * X_SHIFT_R
        screen_y_origin = r * Y_STEP_R

        min_screen_x = min(min_screen_x, screen_x_origin)
        max_screen_x = max(max_screen_x, screen_x_origin + HEX_ART_WIDTH - 1)
        min_screen_y = min(min_screen_y, screen_y_origin)
        max_screen_y = max(max_screen_y, screen_y_origin + HEX_ART_HEIGHT - 1)

    total_canvas_width = max_screen_x - min_screen_x + 1
    total_canvas_height = max_screen_y - min_screen_y + 1

    canvas = [[' ' for _ in range(total_canvas_width)] for _ in
              range(total_canvas_height)]

    def get_hexagon_art(value):
        val_str = str(value)
        if len(val_str) > 1:
            display_val = val_str[0]
        else:
            display_val = val_str

        return [
            "  ___  ",
            " /   \\ ",
            f"|  {display_val}  |",
            " \\___/ "
        ]

    for (q, r), value in board.items():
        screen_x_start = q * X_STEP_Q + r * X_SHIFT_R
        screen_y_start = r * Y_STEP_R

        draw_x = screen_x_start - min_screen_x
        draw_y = screen_y_start - min_screen_y

        hex_art_lines = get_hexagon_art(value)

        for h_row_idx, line in enumerate(hex_art_lines):
            for h_col_idx, char in enumerate(line):
                canvas_row = draw_y + h_row_idx
                canvas_col = draw_x + h_col_idx

                if (0 <= canvas_row < total_canvas_height and
                        0 <= canvas_col < total_canvas_width):
                    canvas[canvas_row][canvas_col] = char

    output_lines = ["".join(row) for row in canvas]
    print("\n".join(output_lines))

