import os
import time
import pytest
import unittest
from alttester import By, AltDriver, AltReversePortForwarding
from appium import webdriver

platform = None
screenshot_dir = None

def setup_port_forwarding(platform):
    try:
        AltReversePortForwarding().remove_reverse_port_forwarding_android()
    except:
        print(f'No adb forward was present')

    try:
        AltReversePortForwarding().kill_alliproxy_process()
    except:
        print("killed all")
# class MyTests(unittest.TestCase):
@pytest.fixture(scope="class", autouse=True)
def drivers(request):
    if os.getenv("APPIUM_PLATFORM", "android") == 'android':
        platform = 'android'
    else:
        platform = "ios"
    print("Running on", platform)

    desired_caps = {}
    desired_caps['platformName'] = os.getenv("APPIUM_PLATFORM", "Android")
    desired_caps['deviceName'] = os.getenv('APPIUM_DEVICE', 'RZCRB04CMGR')
    desired_caps['autoLaunch']= os.getenv("autoLaunch", 'true')
    desired_caps['app'] = os.getenv("APPIUM_APPFILE", os.path.abspath("./android/Roulette.apk"))
    desired_caps['automationName'] = os.getenv('APPIUM_AUTOMATION', 'UIAutomator2')
    desired_caps['AppPackage']=os.getenv('AppPackage',"com.DefaultCompany.Roullete")
    desired_caps['AppActivity']=os.getenv('AppActivity', "com.unity3d.player.UnityPlayerActivity")
    desired_caps['newcommandTimeout'] = 2000

    appium_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    appium_driver.implicitly_wait(20)
    print("Appium driver started")
    time.sleep(5)
    # altunity_driver.find_element_by_accessibility_id("Game view").click()

    setup_port_forwarding(platform)
    altunity_driver = AltDriver()
    print("Altunity driver started")

    screenshot_dir = os.getcwd() + '/screenshots'
    if not os.path.exists(screenshot_dir):
        os.mkdir(screenshot_dir)

    request.cls.appium_driver = appium_driver
    request.cls.altunity_driver = altunity_driver
    request.cls.platform = platform
    request.cls.screenshot_dir = screenshot_dir

    yield
    request.cls.altunity_driver.stop()
    request.cls.appium_driver.quit()
    
