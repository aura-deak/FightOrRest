RESET = "\033[0m"

# 字体高亮（前景色）
RESET = "\033[0m"
YELLOW_FONT = "\033[93m"
BLUE_FONT = "\033[1;94m"
YELLOW_BG = "\033[103m"
BLUE_BG = "\033[104m"

def highlight_text(text, color_type):
    """
    高亮显示字符串
    :param text: 要显示的字符串
    :param color_type: 颜色类型，可选值：
                       yellow_font, blue_font, yellow_bg, blue_bg
    :return: 带高亮样式的字符串
    """
    color_codes = {
        "yellow_font": YELLOW_FONT,
        "blue_font": BLUE_FONT,
        "yellow_bg": YELLOW_BG,
        "blue_bg": BLUE_BG
    }
    # 校验颜色类型是否合法
    if color_type not in color_codes:
        raise ValueError(f"color_type必须是{list(color_codes.keys())}中的一种")
    # 拼接颜色码、字符串、重置码
    return f"{color_codes[color_type]}{text}{RESET}"