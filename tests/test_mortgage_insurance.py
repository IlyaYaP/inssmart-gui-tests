import allure
import pytest
from pages.insurance_form_calculation import InsuranceFormCalculation
import time


insurance_page_url = "https://widgets.inssmart.ru/contract/mortgage/?appId=79f46bfb-d4ba-50aa-8269-7289dd16700c&secret=6ca520c0-328b-5b65-ab5c-b41332a3e667"

class TestsInsuranceForm():
    def test_mortgage_insurance(self, browser):
        page = InsuranceFormCalculation(browser, insurance_page_url)
        page.open_page()
        page.insurance_form()
        time.sleep(5)