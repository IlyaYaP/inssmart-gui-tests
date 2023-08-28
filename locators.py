from selenium.webdriver.common.by import By


class MortgageInsuranceLocators():
    button_type_insurance = (By.XPATH,
                             '//span[text()="Жизнь"]/parent::*')
    button_bank_derop_list = (
        By.CSS_SELECTOR,
        '.MuiButtonBase-root.MuiIconButton-root.MuiAutocomplete-popupIndicator')
    bank_input_field = (
        By.CSS_SELECTOR,
        '.MuiInputBase-input.MuiOutlinedInput-input.MuiAutocomplete-input')
    input_bank_value = (By.CSS_SELECTOR,
                        'input[aria-activedescendant*="option-1"]')
    button_clear_bank = (By.CSS_SELECTOR,
                         '.MuiIconButton-root.MuiAutocomplete-clearIndicator')
    input_credit_value = (By.CSS_SELECTOR, 'input[name=creditValue]')
    gender_field = (By.CSS_SELECTOR, '.MuiSelect-root.MuiSelect-select')
    gender_field_man = (By.XPATH, '//span[text()="Мужской"]')
    date_birth_field = (By.CSS_SELECTOR, 'input[placeholder="dd.mm.yyyy"]')
    title_insurance_checkbox = (By.CSS_SELECTOR, 'input[name="titleInsurance"]')
    view_offers_button = (By.XPATH, '//h6[text()="Посмотреть предложения"]')
    title_view_offers = (By.XPATH, '//div[text()="Предложения страховых"]')
