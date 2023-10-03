import time
import unittest

from appium import webdriver
from alttester import AltDriver, By, AltKeyCode
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

class MyTests:
    def __init__(self, altdriver):
        self.altdriver = altdriver

    def wait_and_click(self, locator, timeout=10):
        element = self.altdriver.wait_for_object(locator, timeout)
        element.click()

    def bet_and_roll(self, coins_locator, bet_amount, roll_button_locator):
        self.wait_and_click(coins_locator)
        self.wait_and_click(bet_amount)
        self.wait_and_click(roll_button_locator)
        time.sleep(20)

    def test_normal_flow(self):
        # Rebet
        self.wait_and_click(By.PATH, "/Canvas/MainScene/Board/BottomBar/Rebet/Image")

        # Roll
        self.wait_and_click(By.PATH, "/Canvas/MainScene/Board/BottomBar/RollBtn/Image")
        time.sleep(20)

        # Betting on specific numbers
        self.bet_and_roll(By.PATH, "/Canvas/MainScene/Board/BottomBar/Coins/Coins (4)",
                          By.PATH, "/Canvas/MainScene/Board/Buttons/CornerBtn/31/BetAmountInfoUI(Clone)/Text (TMP)")

        # Betting on dozens
        self.bet_and_roll(By.PATH, "/Canvas/MainScene/Board/BottomBar/Coins/Coins (4)",
                          By.PATH, "/Canvas/MainScene/Board/Buttons/Dozen/1")

        # Betting on rows
        self.bet_and_roll(By.PATH, "/Canvas/MainScene/Board/BottomBar/Coins/Coins (4)",
                          By.PATH, "/Canvas/MainScene/Board/Buttons/RowBtn/1")

        # Betting on lower numbers
        self.bet_and_roll(By.PATH, "/Canvas/MainScene/Board/BottomBar/Coins/Coins (3)",
                          By.PATH, "/Canvas/MainScene/Board/Buttons/Higher/Lower/Lower")

        # Betting on higher numbers
        self.bet_and_roll(By.PATH, "/Canvas/MainScene/Board/BottomBar/Coins/Coins (2)",
                          By.PATH, "/Canvas/MainScene/Board/Buttons/Higher/Lower/Higher")

        # Betting on black color
        self.bet_and_roll(By.PATH, "/Canvas/MainScene/Board/BottomBar/Coins/Coins (3)",
                          By.PATH, "/Canvas/MainScene/Board/Buttons/Color/Black")

        # Betting on red color
        self.bet_and_roll(By.PATH, "/Canvas/MainScene/Board/BottomBar/Coins/Coins (3)",
                          By.PATH, "/Canvas/MainScene/Board/Buttons/Color/Red")

        # Betting on even numbers
        self.bet_and_roll(By.PATH, "/Canvas/MainScene/Board/BottomBar/Coins/Coins (3)",
                          By.PATH, "/Canvas/MainScene/Board/Buttons/Odd/Even/Even")

        # Betting on odd numbers
        self.bet_and_roll(By.PATH, "/Canvas/MainScene/Board/BottomBar/Coins/Coins (2)",
                          By.PATH, "/Canvas/MainScene/Board/Buttons/Odd/Even/Odd")

        # Betting on dozens
        self.bet_and_roll(By.PATH, "/Canvas/MainScene/Board/BottomBar/Coins/Coins (2)",
                          By.PATH, "/Canvas/MainScene/Board/Buttons/Dozen/3")

        # Betting on dozens
        self.bet_and_roll(By.PATH, "/Canvas/MainScene/Board/BottomBar/Coins/Coins (2)",
                          By.PATH, "/Canvas/MainScene/Board/Buttons/Dozen/2")

        # Betting on dozens
        self.bet_and_roll(By.PATH, "/Canvas/MainScene/Board/BottomBar/Coins/Coins (2)",
                          By.PATH, "/Canvas/MainScene/Board/Buttons/Dozen/1")

        # Betting on split numbers
        self.wait_and_click(By.PATH, "/Canvas/MainScene/Board/BottomBar/Coins/Coins (2)")
        split_numbers = [
            ("/Canvas/MainScene/Board/Buttons/SplitBtn/[18/21]"),
            ("/Canvas/MainScene/Board/Buttons/SplitBtn/17/16"),
            ("/Canvas/MainScene/Board/Buttons/SplitBtn/32/33"),
            ("/Canvas/MainScene/Board/Buttons/SplitBtn/10/13")
        ]
        for split_number in split_numbers:
            self.wait_and_click(By.PATH, split_number)

        self.wait_and_click(By.PATH, "/Canvas/MainScene/Board/BottomBar/RollBtn/Image")
        time.sleep(20)
