from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_credKart_login_params:

     def test_credKart_login_params(self, setup, getDataforLogin):py
         self.driver = setup
         self.driver.get("https://automation.credence.in/login")
         self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(getDataforLogin[0])
         self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(getDataforLogin[1])
         self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
         try:
             self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
             print("Login TestCase is Passed")
             self.driver.save_screenshot(".\\ScreenSHots\\"+getDataforLogin[0]+"_"+getDataforLogin[1]+"_"+"test_CredKart_Login.PNG")
             self.driver.close()
             assert True
         except:
             print("Login TestCase is Failed")
             self.driver.save_screenshot(".\\ScreenSHots\\"+getDataforLogin[0]+"_"+getDataforLogin[1]+"_"+"test_CredKart_Login.PNG")
             self.driver.close()
             assert False

