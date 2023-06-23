from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import Dropdowns.constant as const


class Dropdowns(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Selenium", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = Options()
        options.add_experimental_option("detach", True)
        super(Dropdowns, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
        else:
            print("Browser will remain open.")

    def land_first_page(self):
        self.get(const.BASE_URL)

    #Affiliate Dropdown
    def dropdown_affiliate(self):
        try:
            self.find_element(By.ID, 'dropdown-menu-5').click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    def go_to_learn(self):
        try:
            self.find_element(By.LINK_TEXT, "Learn").click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    def click_back_btn(self):
        try:
            self.find_element(By.LINK_TEXT, "Back").click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    def go_to_getting_started(self):
        try:
            self.find_element(By.LINK_TEXT, "Getting Started").click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")
    
    def go_to_how_to_make_money(self):
        try:
            self.find_element(By.LINK_TEXT, "How To Make Money").click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    #Event dropdown
    def dropdown_event(self):
        try:
            self.find_element(By.ID, 'dropdown-menu-7').click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    def go_to_influencer_marketing(self):
        try:
            self.find_element(By.LINK_TEXT, "Influencer Marketing").click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    def go_to_networks(self):
        try:
            self.find_element(By.LINK_TEXT, "Networks").click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    #About Us Dropdown
    def dropdown_about_us(self):
        try:
            self.find_element(By.ID, 'dropdown-menu-8').click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    def go_to_case_studies(self):
        try:
            self.find_element(By.LINK_TEXT, "Case Studies").click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    def go_to_who_we_are(self):
        try:
            self.find_element(By.LINK_TEXT, "Who we are").click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    #Support Dropdown
    def dropdown_support(self):
        try:
            self.find_element(By.ID, 'dropdown-menu-10').click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    def go_to_affiliate_support(self):
        try:
            self.find_element(By.LINK_TEXT, "Affiliate Support").click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    def go_to_customer_services_support(self):
        try:
            self.find_element(By.LINK_TEXT, "Customer Service Support").click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    def go_to_vendor_support(self):
        try:
            self.find_element(By.LINK_TEXT, "Vendor support").click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")

    #Blog Page
    def go_to_blog(self):
        try:
            self.find_element(By.LINK_TEXT, "Blog").click()
        except WebDriverException as e:
            print(f"An error occurred: {e}")