from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():
    url = input('Username: ')
    root = webdriver.Chrome()
    root.get(f'https://ngl.link/{url}')
    while True:
        try:
            time.sleep(1)
            random_ask_button = root.find_element(By.XPATH, '/html/body/div[1]/form/div[1]/div[2]/div')
            random_ask_button.click()
            time.sleep(1)
            send_button = root.find_element(By.XPATH, '/html/body/div[1]/form/button')
            send_button.click()
            time.sleep(1)
            send_next_message = root.find_element(By.XPATH, '/html/body/div[1]/a[3]')
            send_next_message.click()
            time.sleep(1)
        except:
            print("Some button not found, I stop the program")
            break


if __name__ == '__main__':
    main()
