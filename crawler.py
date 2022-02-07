from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  
from time import sleep 
import json 

def crawl():
    # General constants
    secs_to_wait = 1
    city = 'Dortmund'
    immo_url = "https://www.wg-gesucht.de/"

    # Xpaths of elements to work with
    accept_cookies_button_xpath = '//*[@id="cmpwelcomebtnyes"]/a'
    city_input_xpath = '//*[@id="autocompinp"]'
    submit_button_xpath = '//*[@id="search_button"]'
    apt_add_xpath = '//div[@class="wgg_card.offer_list_item"]'
    apt_add_selector = '.wgg_card.offer_list_item'
    link_xpath = '//*[@id="liste-details-ad-8834598"]/div/div[1]/a'

    # Start the browser
    options = Options()
    # set headless option to True to run browser in headless mode
    # options.headless = True 

    browser = webdriver.Chrome(options=options)

    # Go to the immo website
    browser.get(immo_url)
    sleep(secs_to_wait)

    # Accept cookies if neccessary.
    try:
        accept_cookies_button = browser.find_element(By.XPATH, accept_cookies_button_xpath)
        accept_cookies_button.click()
        sleep(secs_to_wait)
    except NoSuchElementException:
        print('Cookies already accepted')

    # Enter city
    city_input = browser.find_element(By.XPATH, city_input_xpath)
    city_input.send_keys(city)
    sleep(secs_to_wait)
    city_input.send_keys(Keys.ENTER)
    sleep(secs_to_wait)

    submit_button = browser.find_element(By.XPATH, submit_button_xpath)
    submit_button.click()
    sleep(secs_to_wait)

    # download divs with ads
    # apt_adds = browser.find_elements(By.XPATH, apt_add_xpath)
    # print(apt_adds)
    # it did not work, returned empty array and Error:
    #  [16932:12704:0207/114111.072:ERROR:ssl_client_socket_impl.cc(995)] handshake failed; returned -1, SSL error code 1, net_error -201
    # so I decided to use javascript
    script_to_get_adds = "return document.querySelectorAll('.wgg_card.offer_list_item')"
    apt_adds = browser.execute_script(script_to_get_adds)

    # Write data to json
    output = []
    apt_id = 0
    for apt_add in apt_adds:
        apt_id += 1;
        info = apt_add.text.split('\n')
        rooms, area, address = info[1].split(' | ')
        info_dict = {
            'id': apt_id,
            'link': apt_add.find_element(By.XPATH, link_xpath).get_attribute('href'),
            'rooms': rooms,
            'area': area,
            'address': address,
            'description': info[0],
            'price': info[2],
            'available from': info[3].replace('ab ', ''),
            'size': info[4],
            'owner': info[5],
            'online since': info[6].replace('Online: ', '')
            }
        output.append(info_dict)

    browser.close()

    output = {'apts': output}
    output = json.dumps(output)
    print(output)
    with open('db.json', 'w') as f:
        json.dump(output, f)
    
    return output

if __name__ == '__main__':
    crawl()