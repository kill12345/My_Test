import unittest
import time
from selenium import webdriver

class browsers_utility ():

   def test(self):

      driver = webdriver.Chrome
      driver = webdriver.Chrome(executable_path="C:\\Users\\MisirukS\\PycharmProjects\\My_Test\\chromedriver.exe")
      driver.get("http://pdlvdcsec03.laclrs.org:7780/c-iv/utilities/Homepage/homepage ")
      print("Pass")
      driver.close()










