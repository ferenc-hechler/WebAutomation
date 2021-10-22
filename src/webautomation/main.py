import time
from selenium import webdriver

from webautomation.humble_bundle import HumbleBundle



def wait(seconds=1):
    time.sleep(seconds)
    
    
def readDriver():
    with open ("../../session_data.txt", "r") as myfile:
        data=myfile.readlines()
    session_url=data[0]
    session_id=data[1]
    #Pass the session_url you extracted
    driver = webdriver.Remote(command_executor=session_url,desired_capabilities={})
    driver.close()
    #Attach to the session id you extracted
    driver.session_id = session_id
    return driver

def run():    
    #driver_path = r'C:\DEV\wspython\WebAutomation\drivers\chromedriver_win32\chromedriver.exe'
    print("connecting Chrome")
    driver = readDriver()
    print("read session")
    session_id = driver.session_id            
    print(session_id)
    
    hb = HumbleBundle(driver)
    print("selectEinkaeufe")
    hb.selectEinkaeufe()
    wait()
    print("filter_einkaeufe")
    hb.filter_einkaeufe("book")
    wait()
    while True:
        cnt = hb.get_count_items()
        for n in range(1, cnt+1):
            item = hb.get_item(n)
            print(f'{item[0]};{item[1]};{item[2]}')
        if (hb.has_next_page()):
            hb.next_page()
        else:
            break

if __name__ == '__main__':
    run()