class Lrs_Login():

    loginButton1 = "//*[@id='loginData']/div/div[4]/input"

    def __init__(self,driver):

        self.driver = driver
        self.loginButton ="//*[@id='loginData']/div/div[4]/input"
        self.loginAcceptButton ="//*[@id='termsAndConditions']/div[2]/button[1]"

    def clickLoginButton(self):
        self.driver.find_element_by_xpath(self.loginButton).click()
        print("Click LoginButton")

# This method you can use when you font want to create constrictor class

    #@classmethod
    #def clickLoginButton(self,driver):
        #self.driver= driver
       # self.driver.find_element_by_xpath(Lrs_Login.loginButton1).click()
        #print("Button click")

    def clickAcceptButton(self):
        self.driver.find_element_by_xpath(self.loginAcceptButton).click()
        print("Button click")






