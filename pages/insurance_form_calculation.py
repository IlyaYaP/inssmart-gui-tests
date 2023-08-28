import allure
from locators import MortgageInsuranceLocators
from base_method import BasePage
import time
from selenium.webdriver.common.keys import Keys

class InsuranceFormCalculation(BasePage):

    def insurance_form(self):
        type_of_insurance_button = self.find_element(MortgageInsuranceLocators.button_type_insurance)
        type_of_insurance_button.click()

        input_bank_field = self.find_element(MortgageInsuranceLocators.bank_input_field)
        input_bank_field.click()
        input_bank_field.send_keys('МТС БАНК')

        value_bank_button = self.find_element(MortgageInsuranceLocators.input_bank_value)
        value_bank_button.send_keys(Keys.ARROW_UP)
        value_bank_button.send_keys(Keys.ENTER)

        input_credit_field = self.find_element(MortgageInsuranceLocators.input_credit_value)
        input_credit_field.click()
        input_credit_field.send_keys(Keys.CONTROL + 'a')
        input_credit_field.send_keys(Keys.DELETE)
        input_credit_field.send_keys('2100000')
