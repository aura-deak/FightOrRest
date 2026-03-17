RESET = "\033[0m"

# Font highlighting (foreground colors)
RESET = "\033[0m"
YELLOW_FONT = "\033[93m"
BLUE_FONT = "\033[1;94m"
YELLOW_BG = "\033[103m"
BLUE_BG = "\033[104m"

def highlight_text(text, color_type):
    """
    Apply color highlighting to a string.
    :param text: The string to highlight
    :param color_type: Color type, one of:
                       yellow_font, blue_font, yellow_bg, blue_bg
    :return: The highlighted string with ANSI codes
    """
    color_codes = {
        "yellow_font": YELLOW_FONT,
        "blue_font": BLUE_FONT,
        "yellow_bg": YELLOW_BG,
        "blue_bg": BLUE_BG
    }
    # Validate color type
    if color_type not in color_codes:
        raise ValueError(f"color_type must be one of {list(color_codes.keys())}")
    # Wrap string with color code and reset
    return f"{color_codes[color_type]}{text}{RESET}"
