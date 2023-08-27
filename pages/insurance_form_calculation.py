import allure
from locators import button_type_insurance, button_bank_derop_list, bank_input_field, input_bank_value, button_clear_bank, input_credit
from base_method import BasePage
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

class InsuranceFormCalculation(BasePage):

    def insurance_form(self):
        type_of_insurance_button = self.find_element(button_type_insurance)
        type_of_insurance_button.click()

        input_bank_field = self.find_element(bank_input_field)
        input_bank_field.click()
        input_bank_field.send_keys('МТС БАНК')

        value_bank_button = self.find_element(input_bank_value)
        value_bank_button.click()

        # input_credit_field = self.find_element(input_credit)
        # input_credit_field.send_keys('90909090')
        time.sleep(5)


        # action = ActionChains(self.browser)
        # action.move_by_offset(50, 50).perform()
        # time.sleep(5)




        # bank_derop_list_button = self.find_element(button_bank_derop_list)
        # bank_derop_list_button.click()





        # bank_value_field = self.find_element(bank_input_field)
        # bank_input_field.send_keys('')

        # time.sleep(5)
        # web_element = self.find_element(input_bank_value)
        # action = ActionChains(self.browser)
        # action.move_to_element(web_element).s.perform()


        # # ActionChains(self.browser).scroll_to_element(product_button).perform()
        # # product_button.click()
