import pygame

from Screens.MenuScreen import MenuScreen
from UIItems.Button import Button
from UIItems.CenteredText import CenteredText

class GameSummaryScreen(MenuScreen):
    """
    Class representing summary of the game screen,
    inherited class MenuScreen
    """

    def __init__(self, click_count):
        self.click_count = click_count

        menu_button = Button("Menu")
        menu_button.set_click(lambda: MainMenuScreen())

        buttons = [menu_button]

        super().__init__(buttons, "Congratulations!", 60)


    def show(self, game):
        text_ = str.format("Your score is {0}.", self.click_count)
        text = CenteredText(text_, 40, (0, 0, 0))
        text.write(game.window, y = game.window.get_height() / 2 - 2 * text.size)

        return super().show(game)

from Screens.MainMenuScreen import MainMenuScreen