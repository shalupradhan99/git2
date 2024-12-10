import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHollandBarret:

  @pytest.fixture()
  def setup(self):
      self.driver = webdriver.Chrome()
      self.driver.maximize_window()
      yield
      self.driver.close()

  def test_homepageTiltle(self,setup):
      self.driver.get("https://auth.hollandandbarrett.com/u/login")
      assert  self.driver.title == 'Sign in - to your account, for the best experience'

  def test_login(self, setup):
      self.driver.get("https://auth.hollandandbarrett.com/u/login")
      self.driver.find_element(By.ID,'username').send_keys("ridhishapradhan19@gmail.com")
      self.driver.find_element(By.ID, 'password').send_keys("Momdad@506")
      self.driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()
      assert self.driver.title



