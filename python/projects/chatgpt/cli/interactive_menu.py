"""Generate interactive menu.

Returns selected item.
"""

import curses


def _menu(stdscr, items, message="Select a model:"):
    """Display an interactive menu to select an item.

    Args:
        stdscr: Standard screen object provided by curses.
        items: List of items to display in the menu.
        message: Message displayed at the top of the menu.

    Returns:
        The selected item from the menu.
    """
    curses.curs_set(0)
    current_row = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, message)
        for idx, item in enumerate(items):
            if idx == current_row:
                stdscr.addstr(idx + 1, 0, f"> {item}")
            else:
                stdscr.addstr(idx + 1, 0, item)
        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(items) - 1:
            current_row += 1
        elif key == ord("\n"):
            return items[current_row]
        elif key in (4, ord('q')):  # Handle EOF and 'q'
            print()
            exit(0)


def select(items):
    """Invoke an interactive menu to select an item.

    Args:
        items: List of items to display in the menu.

    Returns:
        The selected item from the menu.
    """
    selected_item = curses.wrapper(_menu, items)
    return selected_item
