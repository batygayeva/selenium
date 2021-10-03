from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com/')

    #ввести запрос "Планета Земля", нажать Enter и проверить слово "Земля" во всех заголовках
    def test_01(self):
        driver = self.driver
        searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        searchbox.send_keys('Планета Земля')
        searchbox.send_keys(Keys.ENTER)
        time.sleep(5)
        titles = driver.find_elements_by_class_name('r')
        for title in titles:
            assert "Земля" in title.text.lower()

    # #ввести запрос "python", кликнуть по кнопке "Искать в Google" и проверить слово "python" во всех заголовках
    def test_02(self):
        driver = self.driver
        searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        searchbox.send_keys('python')
        button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
        button.click()
        time.sleep(5)
        titles = driver.find_elements_by_class_name('r')
        for title in titles:
            assert "python" in title.text.lower()

    #ввести запрос "test", нажать на клавиатуре два раза клавишу "Вниз",
    #нажать клавишу Enter, кликнуть по вкладке "Картинки",
    #кликнуть по вкладке "Видео"
    def test_03(self):
        driver = self.driver
        searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        searchbox.send_keys('test')
        time.sleep(2)
        searchbox.send_keys(Keys.DOWN)
        #searchbox.send_keys(Keys.DOWN)
        searchbox.send_keys(Keys.ENTER)
        button_pictures = driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
        button_pictures.click()
        button_videos = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[3]')
        button_videos.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()