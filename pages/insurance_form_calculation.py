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

        gender_type_field = self.find_element(MortgageInsuranceLocators.gender_field)
        gender_type_field.click()
        gender_type_man = self.find_element(MortgageInsuranceLocators.gender_field_man)
        gender_type_man.click()

        input_date_birth_field = self.find_element(MortgageInsuranceLocators.date_birth_field)
        input_date_birth_field.send_keys('29081992')
        time.sleep(5)
