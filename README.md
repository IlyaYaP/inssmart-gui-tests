# Локальный запуск:
- Клонируем данный репозиторий:
```
git clone (https://github.com/IlyaYaP/inssmart-gui-tests.git)
```
- В папке с проектом создаем и активируем виртуальное окружение:
```
python -m venv venv
source venv/scripts/activate
```
- Устанавливаем зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- Устанавливаем allure на Windows(если у вас данная ОС) через scoop.
```
scoop install allure 
```
- Запускаем тесты (Chrome):
```
pytest -s -v --alluredir result_allure --tb=long
```
- Формируем отчет allure.
```
allure 
