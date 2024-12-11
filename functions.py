import time as tm
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


def page_down(driver):
    driver.execute_script('''
                            const scrollStep = 200; // Размер шага прокрутки (в пикселях)
                            const scrollInterval = 100; // Интервал между шагами (в миллисекундах)

                            const scrollHeight = document.documentElement.scrollHeight;
                            let currentPosition = 0;
                            const interval = setInterval(() => {
                                window.scrollBy(0, scrollStep);
                                currentPosition += scrollStep;

                                if (currentPosition >= scrollHeight) {
                                    clearInterval(interval);
                                }
                            }, scrollInterval);
                        ''')


def collect_product_info(driver, url=''):
    driver.get(url)
    tm.sleep(3)

    page_source = str(driver.page_source)
    soup = BeautifulSoup(page_source, 'lxml')

    # product_id
    try:
        product_id = soup.find('span', class_='ok3_27').text.strip()
    except:
        product_id = None

    # product price
    try:
        product_price = soup.find('span', class_='v4l_27 lv3_27').text.strip()
    except:
        product_price = None

    product_data = {
        'product_id': product_id,
        'product_price': product_price,
    }

    return product_data