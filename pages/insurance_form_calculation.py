import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base_method import BasePage
from locators import MortgageInsuranceLocators
from allure_commons.types import AttachmentType


class InsuranceFormCalculation(BasePage):

    def type_of_insurance(self, insurance_type):
        with allure.step('Выбираем тип страховки.'):
            type = (By.XPATH, f'//span[text()="{insurance_type}"]/parent::*')
            type_of_insurance_button = self.find_element(type)
            type_of_insurance_button.click()

    def input_bank_value(self, bank_name):
        with allure.step('Выбираем банк.'):
            input_bank_field = self.find_element(
                MortgageInsuranceLocators.bank_input_field)
            input_bank_field.click()
            input_bank_field.send_keys(bank_name)
            value_bank_button = self.find_element(
                MortgageInsuranceLocators.input_bank_value)
            value_bank_button.send_keys(Keys.ARROW_UP)
            value_bank_button.send_keys(Keys.ENTER)

    def loan_balance_value(self, credit_value):
        with allure.step('Добавляем остаток по кредиту.'):
            input_credit_field = self.find_element(
                MortgageInsuranceLocators.input_credit_value)
            input_credit_field.click()
            input_credit_field.send_keys(Keys.CONTROL + 'a')
            input_credit_field.send_keys(Keys.DELETE)
            input_credit_field.send_keys(credit_value)

    def gender_type_field(self, gender_type):
        with allure.step('Выбираем пол.'):
            type = (By.XPATH, f'//span[text()="{gender_type}"]')
            gender_type_field = self.find_element(
                MortgageInsuranceLocators.gender_field)
            gender_type_field.click()
            gender_type = self.find_element(type)
            gender_type.click()

    def input_date_birth(self, birth_date):
        with allure.step('Добавляем дату рождения.'):
            input_date_birth_field = self.find_element(
                MortgageInsuranceLocators.date_birth_field)
            input_date_birth_field.send_keys(birth_date)

    def title_insurance_checkbox(self):
        with allure.step('Выбираем "Титульное страхование".'):
            title_insurance = self.find_element(
                MortgageInsuranceLocators.title_insurance_checkbox)
            title_insurance.click()
            button_view_offers = self.find_element(
                MortgageInsuranceLocators.view_offers_button)
            button_view_offers.click()

    def should_be_view_offers(self):
        with allure.step(
            'Проверяем, что мы перешли на страницу с предложениями.'):
            assert self.is_element_present_timeout(
                *MortgageInsuranceLocators.title_view_offers), 'View offers is not presented.'
            allure.attach(self.browser.get_screenshot_as_png(),
                          name='Screenshot',
                          attachment_type=AttachmentType.PNG)
