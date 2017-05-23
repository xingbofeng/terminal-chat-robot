RESET_COLOR = '\033[0m'

COLOR_CODES = {
    'blue': '\033[1;34m',  # blue
    'green': '\033[1;32m',  # green
    'yellow': '\033[1;33m',  # yellow
    'red': '\033[1;31m',  # red
}


def colormsg(level, msg):
    return COLOR_CODES[level] + msg + RESET_COLOR
