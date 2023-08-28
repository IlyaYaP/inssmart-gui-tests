import allure
import pytest

from data import InsuranceFormCalculationData
from pages.insurance_form_calculation import InsuranceFormCalculation

insurance_page_url = "https://widgets.inssmart.ru/contract/mortgage/?appId=79f46bfb-d4ba-50aa-8269-7289dd16700c&secret=6ca520c0-328b-5b65-ab5c-b41332a3e667"


class TestsInsuranceForm():

    @pytest.mark.parametrize('insurance_type, \
                             bank_name, \
                             credit_value, \
                             gender_type, \
                             birth_date',
                             [InsuranceFormCalculationData.positive_test_data_1])
    def test_mortgage_insurance(self,
                                browser,
                                insurance_type,
                                bank_name,
                                credit_value,
                                gender_type,
                                birth_date):
        page = InsuranceFormCalculation(browser, insurance_page_url)
        page.open_page()
        page.type_of_insurance(insurance_type)
        page.input_bank_value(bank_name)
        page.loan_balance_value(credit_value)
        page.gender_type_field(gender_type)
        page.input_date_birth(birth_date)
        page.title_insurance_checkbox()
        page.should_be_view_offers()
