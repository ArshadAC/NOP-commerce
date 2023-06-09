import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.Logger import LogGenerator

class Test_Login:

    url = ReadConfig.getUrl()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_001_Homepage(self, setup):
        self.log.info("Test__001__Homepage started")
        self.driver = setup
        self.log.info("Opening URl")
        self.driver.get("https://admin-demo.nopcommerce.com/")
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.log.info("Test__001__Homepage Test Passed")

        else:
            self.log.info("Test__001__Homepage Test Failed")
            assert False

    @pytest.mark.sanity
    def test_002_login(self,setup):
        self.log.info("Test__002__Homepage started")
        self.driver = setup
        self.log.info("Opening URl")
        self.driver.get(self.url)
        self.log.info("Test__002__login started" + str(self.url))
        self.lp = LoginPage(self.driver)
        self.log.info("Entering Email-->" + str(self.email))
        self.lp.EnterEmail(self.email)
        self.log.info("Entering Password-->" + str(self.password))
        self.lp.EnterPassword(self.password)
        self.log.info("Clicking Login")
        self.lp.ClickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.log.info("page title-->" + str(self.driver.title))
            self.log.info("clicking logout")
            self.lp.ClickLogout()
            self.log.info("Tset_002_login is passed")
            print("Tset_002_login is passed")
            assert True

        else:
            self.log.info("page title-->" + str(self.driver.title))
            self.driver.save_screenshot("E:\\Automation Project\\NOP Commerce\\Screenshots\\Login.PNG")
            self.log.info("Login failed")
            print("Test_002_LoginFailed")
            assert False























