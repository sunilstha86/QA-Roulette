import time
import unittest
from appium import webdriver
from alttester import AltDriver, By
import random

class MyTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.altdriver = AltDriver(enable_logging=False)

    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop()

    def click_element(self, element_path):
        element = self.altdriver.wait_for_object(By.PATH, element_path)
        element.click()

    def place_random_bet(self, possible_bets,num_bets,coin_values):
      for _ in range(num_bets):
        random_bet = random.choice(possible_bets)
        random_coin_value = random.choice(coin_values)
        self.click_element(random_bet)

       # set the coin values here
        self.click_element(f"/Canvas/MainScene/Board/BottomBar/Coins/Coins ({random_coin_value})")


    def roll_wheel(self):
        self.click_element("/Canvas/MainScene/Board/BottomBar/RollBtn/Image")
        time.sleep(40)

    def test_normal_flow(self):
        # Click the Board
        # self.click_element("/AltTesterPrefab/AltDialog/Icon")
        self.click_element("/Canvas/MainScene/Board")
    
        # Place random  bets on random numbers
        straight_bets = [
            "/Canvas/MainScene/Board/Buttons/StraightBtn/10",
            "/Canvas/MainScene/Board/Buttons/StraightBtn/3",
            "/Canvas/MainScene/Board/Buttons/StraightBtn/18",
            "/Canvas/MainScene/Board/Buttons/StraightBtn/15",
            "/Canvas/MainScene/Board/Buttons/StraightBtn/13",
            "/Canvas/MainScene/Board/Buttons/StraightBtn/30",
            "/Canvas/MainScene/Board/Buttons/StraightBtn/31",
            "/Canvas/MainScene/Board/Buttons/StraightBtn/23",
            "/Canvas/MainScene/Board/Buttons/StraightBtn/25",
            "/Canvas/MainScene/Board/Buttons/StraightBtn/8",
            "/Canvas/MainScene/Board/Buttons/StraightBtn/29",
            "/Canvas/MainScene/Board/Buttons/StraightBtn/7",
            "/Canvas/MainScene/Board/Buttons/StraightBtn/36",
            "/Canvas/MainScene/Board/Buttons/SplitBtn/18\/21",
            "/Canvas/MainScene/Board/Buttons/SplitBtn/16\/17",
            "/Canvas/MainScene/Board/Buttons/SplitBtn/13\/14",
            "/Canvas/MainScene/Board/Buttons/SplitBtn/13\/16",
            "/Canvas/MainScene/Board/Buttons/SplitBtn/12\/15",
            "/Canvas/MainScene/Board/Buttons/SplitBtn/17\/20",
            "/Canvas/MainScene/Board/Buttons/SplitBtn/17\/18",
            "/Canvas/MainScene/Board/Buttons/SplitBtn/11\/14",
            "/Canvas/MainScene/Board/Buttons/CornerBtn/31",
            "/Canvas/MainScene/Board/Buttons/CornerBtn/3",
            "/Canvas/MainScene/Board/Buttons/CornerBtn/9",
            "/Canvas/MainScene/Board/Buttons/CornerBtn/21",
            "/Canvas/MainScene/Board/Buttons/CornerBtn/27",
            "/Canvas/MainScene/Board/Buttons/CornerBtn/1",
            "/Canvas/MainScene/Board/Buttons/CornerBtn/10",
            "/Canvas/MainScene/Board/Buttons/CornerBtn/19",
            "/Canvas/MainScene/Board/Buttons/CornerBtn/28",
            "/Canvas/MainScene/Board/Buttons/CornerBtn/18",
            "/Canvas/MainScene/Board/Buttons/Dozen/1",
            "/Canvas/MainScene/Board/Buttons/RowBtn/1",
            "/Canvas/MainScene/Board/Buttons/Higher\/Lower/Lower",
            "/Canvas/MainScene/Board/Buttons/Higher\/Lower/Higher",
            "/Canvas/MainScene/Board/Buttons/Color/Black",
            "/Canvas/MainScene/Board/Buttons/Color/Red",
            "/Canvas/MainScene/Board/Buttons/Odd\/Even/Even",
            "/Canvas/MainScene/Board/Buttons/Odd\/Even/Odd",
            "/Canvas/MainScene/Board/Buttons/Dozen/3",
            "/Canvas/MainScene/Board/Buttons/Dozen/2",
            "/Canvas/MainScene/Board/Buttons/SixLineBtn/33",
            "/Canvas/MainScene/Board/Buttons/SixLineBtn/33 (1)",
            "/Canvas/MainScene/Board/Buttons/SixLineBtn/3",
            "/Canvas/MainScene/Board/Buttons/SixLineBtn/3 (1)",
            "/Canvas/MainScene/Board/Buttons/SixLineBtn/12",
            "/Canvas/MainScene/Board/Buttons/SixLineBtn/12 (1)",
            "/Canvas/MainScene/Board/Buttons/SixLineBtn/18",
            "/Canvas/MainScene/Board/Buttons/SixLineBtn/18 (1)",
            "/Canvas/MainScene/Board/Buttons/SixLineBtn/27",
            "/Canvas/MainScene/Board/Buttons/SixLineBtn/27 (1)",
            "/Canvas/MainScene/Board/Buttons/StreetBtn/3",
            "/Canvas/MainScene/Board/Buttons/StreetBtn/3 (1)",
            "/Canvas/MainScene/Board/Buttons/StreetBtn/6",
            "/Canvas/MainScene/Board/Buttons/StreetBtn/6 (1)",
            "/Canvas/MainScene/Board/Buttons/StreetBtn/18",
            "/Canvas/MainScene/Board/Buttons/StreetBtn/18 (1)",
            "/Canvas/MainScene/Board/Buttons/StreetBtn/24",
            "/Canvas/MainScene/Board/Buttons/StreetBtn/24 (1)",
            "/Canvas/MainScene/Board/Buttons/StreetBtn/15",
            "/Canvas/MainScene/Board/Buttons/StreetBtn/15 (1)",
            "/Canvas/MainScene/Board/Buttons/StreetBtn/12 (1)"
        ]
        coin_values=["1","2","3","4"]
        self.place_random_bet(straight_bets, num_bets=10,coin_values=coin_values )  # Place 3 straight bets


        # Click Coins (1)
        coins_bets = [
            "/Canvas/MainScene/Board/BottomBar/Coins/Coins",
            "/Canvas/MainScene/Board/BottomBar/Coins/Coins (1)",
            "/Canvas/MainScene/Board/BottomBar/Coins/Coins (2)",
            "/Canvas/MainScene/Board/BottomBar/Coins/Coins (3)",
            "/Canvas/MainScene/Board/BottomBar/Coins/Coins (4)"
        ]
        self.place_random_bet(coins_bets,num_bets=4,coin_values=coin_values)
        print("First roll has been done")
        # Roll the wheel
        self.roll_wheel()

        # Rebet functions
        self.click_element("/Canvas/MainScene/Board/BottomBar/Rebet/Image")
        print("Rebet has been done")
        self.roll_wheel()
        

        # Clear functions
        self.click_element("/Canvas/MainScene/Board/BottomBar/Rebet/Image")
        time.sleep(10)
        self.click_element("/Canvas/MainScene/Board/BottomBar/Clear/Image")
        print("Clear has been done")
        time.sleep(20)

        # Undo function
        self.place_random_bet(straight_bets,num_bets=1,coin_values=coin_values)
        self.place_random_bet(coins_bets,num_bets=1,coin_values=coin_values)
        self.click_element("/Canvas/MainScene/Board/BottomBar/Undo/Image")
        print("Undo has been done")


        # Place random bets on random numbers
        self.place_random_bet(straight_bets, num_bets=15,coin_values=coin_values)
        self.place_random_bet(coins_bets,num_bets=3,coin_values=coin_values)

        # Roll the wheel
        self.roll_wheel()
        print("Second roll has been done")
        time.sleep(10)


        # Place random bets on random numbers
        self.place_random_bet(straight_bets, num_bets=10,coin_values=coin_values)
        self.place_random_bet(coins_bets,num_bets=4,coin_values=coin_values)

        # Roll the wheel
        self.roll_wheel()
        print("Third roll has been done")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)