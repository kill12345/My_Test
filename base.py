import time

from driver import driver
from selenium import webdriver
import scriptUtils
import unittest
import LRS_NewApll



class SetUp_Browsers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:\\Users\\MisirukS\\PycharmProjects\\My_Test\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):

        self.driver.get("http://pdlvdcsec03.laclrs.org:7780/c-iv/utilities/Homepage/homepage ")
        path = "C:\\Users\\MisirukS\\PycharmProjects\\My_Test\\venv\\Lib\\util_packages\\testexml.xlsx"

        password = scriptUtils.readData(path, 'Sheet1', 2, 2)
        username = scriptUtils.readData(path, 'Sheet1', 2, 1)
        print(username + "- This is user name ")
        print(password + "- This is password ")

        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)

          #LRS_NewApll.Lrs_Login.clickLoginButton(self.driver)

        lrs = LRS_NewApll.Lrs_Login(self.driver)
        lrs.clickLoginButton()
        lrs.clickAcceptButton()

        if self.driver.title == "LRS System - County of Los Angeles - LRS System":
            print("Title Correct ")
            scriptUtils.storeData(path, "Sheet1", 2, 3, "Title Correct")
        else:
            print("Title Failed")
            scriptUtils.storeData(path, "Sheet1", 2, 3, "Title Failed")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Test Pass")
        cls.driver.close()








