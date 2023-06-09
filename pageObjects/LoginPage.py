from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert



class LoginPage:

    Text_Email_Xpath = (By.XPATH,"//input[@id='Email']")
    Text_Password_Xpath = (By.XPATH,"//input[@id='Password']")
    Btn_Login_Xpath = (By.XPATH,"//button[@type='submit']")
    Lnk_Logout_Xpath = (By.XPATH,"//a[normalize-space()='Logout']")

    def __init__(self,driver):
        self.driver = driver

    def EnterEmail(self,email):
        self.driver.find_element(*LoginPage.Text_Email_Xpath).clear()
        self.driver.find_element(*LoginPage.Text_Email_Xpath).send_keys(email)

    def EnterPassword(self,password):
        self.driver.find_element(*LoginPage.Text_Password_Xpath).clear()
        self.driver.find_element(*LoginPage.Text_Password_Xpath).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(*LoginPage.Btn_Login_Xpath).click()

    def ClickLogout(self):
        self.driver.find_element(*LoginPage.Lnk_Logout_Xpath).click()

















