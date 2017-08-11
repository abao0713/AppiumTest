import unittest
from zipfile import ZipFile
import json
import os
import random
from time import sleep
from dateutil.parser import parse

from selenium.common.exceptions import NoSuchElementException

from appium import webdriver
import desired_capabilities

class AppiumTests(unittest.TestCase):
    def setUp(self):
        desired_caps = get_desired_caps(platformName,platformVersion,deviceName,appPackage,appActivity)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()
