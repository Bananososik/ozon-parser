import json
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from functions import collect_product_info

def get_products_links(page_url='https://ozon.ru/t/649d91a'):
    driver = uc.Chrome()
    driver.implicitly_wait(5)
    driver.get(url=page_url)
    time.sleep(2)

    products_data = []

    while True:
        # Собираем ссылки на товары со страницы
        try:
            find_links = driver.find_elements(By.CLASS_NAME, 'tile-hover-target')
            products_urls = list(set([f'{link.get_attribute("href")}' for link in find_links]))

            print('[+] Ссылки на товары собраны!')
        except:
            print('[!] Что-то сломалось при сборе ссылок на товары!')
            break

        for url in products_urls:
            data = collect_product_info(driver=driver, url=url)
            print(f'[+] Собрал данные товара с id: {data.get("product_id")}')
            time.sleep(2)
            products_data.append(data)

        try:
            next_button = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Следующая страница"]')
            next_button.click()
            time.sleep(3)
        except:
            break

    with open('PRODUCTS_DATA.json', 'w', encoding='utf-8') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)

    driver.quit()

def main():
    print('[INFO] Сбор данных начался. Пожалуйста ожидайте...')
    get_products_links(page_url='https://ozon.ru/t/649d91a')
    print('[INFO] Работа выполнена успешно!')

if __name__ == '__main__':
    main()