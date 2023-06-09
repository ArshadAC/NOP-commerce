import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.Logger import LogGenerator

class Test_Login_Parameter:

    url = ReadConfig.getUrl()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    log = LogGenerator.loggen()

    # def test_001_Homepage(self, setup):
    #     self.log.info("Test__001__Homepage started")
    #     self.driver = setup
    #     self.log.info("Opening URl")
    #     self.driver.get("https://admin-demo.nopcommerce.com/")
    #     act_title = self.driver.title
    #     if act_title == "Your store. Login":
    #         assert True
    #         self.log.info("Test__001__Homepage Test Passed")
    #
    #     else:
    #         self.log.info("Test__001__Homepage Test Failed")
    #         assert False



    @pytest.mark.sanity
    def test_003_login(self,setup,GetDataforlogin):
        self.log.info("Test__002__Homepage started")
        self.driver = setup
        self.log.info("Opening URl")
        self.driver.get(self.url)
        self.log.info("Test__002__login started" + str(self.url))
        self.lp = LoginPage(self.driver)
        self.log.info("Entering Email-->" + str(GetDataforlogin[0]))
        self.lp.EnterEmail(GetDataforlogin[0])
        self.log.info("Entering Password-->" + str(GetDataforlogin[1]))
        self.lp.EnterPassword(GetDataforlogin[1])
        self.log.info("Clicking Login")
        self.lp.ClickLogin()
        act_title = self.driver.title

        statusList = []
        if act_title == "Dashboard / nopCommerce administration":

            if GetDataforlogin[2] == "Pass":
                self.log.info("page title-->" + str(self.driver.title))
                self.log.info("clicking logout")
                self.lp.ClickLogout()
                self.log.info("Tset_002_login is passed")
                print("Tset_002_login is passed")
                statusList.append("Pass")

            elif GetDataforlogin[2] == "Fail":
                self.log.info("clicking logout")
                self.lp.ClickLogout()
                self.log.info("Tset_002_login is failed")
                print("Tset_002_login is failed")
                statusList.append("Fail")

        else:
            if GetDataforlogin[2] == "Pass":
                self.log.info("page title-->" + str(self.driver.title))
                self.driver.save_screenshot("E:\\Automation Project\\NOP Commerce\\Screenshots\\Login.PNG")
                self.log.info("Login failed")
                print("Test_002_LoginFailed")
                statusList.append("Fail")

            elif GetDataforlogin[2] == "Fail":
                self.log.info("page title-->" + str(self.driver.title))
                self.driver.save_screenshot("E:\\Automation Project\\NOP Commerce\\Screenshots\\Login.PNG")
                self.log.info("Login failed")
                print("Test_002_LoginFailed")
                statusList.append("Pass")

        print(statusList)
        if "Fail" not in statusList:
            assert True
            self.log.info("Test_003_Login passed")


        else:
            self.log.info("Test_003_Login failed")
            assert False

        self.log.info("Test_003_Login completed")