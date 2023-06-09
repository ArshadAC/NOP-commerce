import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.Logger import LogGenerator
from utilities import XLutils
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert

class Test_Login_DDT:

    url = ReadConfig.getUrl()
    log = LogGenerator.loggen()
    path = "E:\\Automation Project\\NOP Commerce\\testCases\\TestData\\Logindata.xlsx"
    #
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
    def test_004_DDT(self,setup):
        self.log.info("Test__004__Homepage started")
        self.driver = setup
        self.log.info("Opening URl")
        self.driver.get(self.url)
        self.log.info("Test__004__login started" + str(self.url))
        self.lp = LoginPage(self.driver)

        self.row = XLutils.Rowcount(self.path, "Sheet1")
        print("Number of rows in Sheet1 is-->" + str(self.row))

        StatusList = []
        for r in range(2, self.row + 1):
            self.Email = XLutils.ReadData(self.path, "Sheet1", r, 2)
            self.Password = XLutils.ReadData(self.path, "Sheet1", r, 3)
            self.exp_result = XLutils.ReadData(self.path, "Sheet1", r, 4)


            self.log.info("Entering Email-->" + str(self.Email))
            self.lp.EnterEmail(self.Email)
            self.log.info("Entering Password-->" + str(self.Password))
            self.lp.EnterPassword(self.Password)
            self.log.info("Clicking Login")
            self.lp.ClickLogin()
            time.sleep(2)


            if self.driver.title == "Dashboard / nopCommerce administration":
                if self.exp_result == "Pass":
                    self.log.info("page title-->" + str(self.driver.title))
                    self.log.info("clicking logout")
                    self.lp.ClickLogout()
                    self.log.info("Tset_004_login is passed")
                    print("Tset_004_login is passed")
                    StatusList.append("Pass")
                    XLutils.WriteData(self.path, "Sheet1", r, 5, "Pass")

                elif self.exp_result == "Fail":
                    self.log.info("page title-->" + str(self.driver.title))
                    self.log.info("clicking logout")
                    self.lp.ClickLogout()
                    self.log.info("Tset_004_login is Failed")
                    print("Tset_004_login is Failed")
                    StatusList.append("Fail")
                    XLutils.WriteData(self.path, "Sheet1", r, 5, "Fail")


            else:
                if self.exp_result == "Pass":
                    self.log.info("page title-->" + str(self.driver.title))
                    self.driver.save_screenshot("E:\\Automation Project\\NOP Commerce\\Screenshots\\LoginDDT.PNG")
                    self.log.info("Tset_004_login is Failed")
                    print("Tset_004_login is Failed")
                    StatusList.append("Fail")
                    XLutils.WriteData(self.path, "Sheet1", r, 5, "Fail")

                elif self.exp_result == "Fail":
                    self.log.info("page title-->" + str(self.driver.title))
                    self.driver.save_screenshot("E:\\Automation Project\\NOP Commerce\\Screenshots\\LoginDDT.PNG")
                    time.sleep(2)
                    self.log.info("Tset_004_login is Failed")
                    print("Tset_004_login is Failed")
                    StatusList.append("Pass")
                    XLutils.WriteData(self.path, "Sheet1", r, 5, "Pass")

        print(StatusList)
        if "Fail" not in StatusList:
            assert True
            self.log.info("test_login_ddt_04 is Passed")
        else:
            self.log.info("test_login_ddt_04 is Failed")
            assert False
        self.log.info("test_login_ddt_04 is Completed")



