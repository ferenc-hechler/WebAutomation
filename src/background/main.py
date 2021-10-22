'''
Created on 19.10.2021

@author: feri
'''
from selenium import webdriver


def saveCookies(drv):
    session_url = driver.command_executor._url 
    session_id = driver.session_id
    print(f"session_url=\"{session_url}\"")
    print(f"session_id=\"{session_id}\"")
    with open("../../session_data.txt", "w") as text_file:
        text_file.write(f"{session_url}\n{session_id}")



driver_path = r'C:\Users\feri\git\WebAutomation\drivers\chromedriver_win32\chromedriver.exe'



print("init Chrome")
driver = webdriver.Chrome(executable_path=driver_path)

print("getting")
driver.get('https://humblebundle.com/')

saveCookies(driver)
print("saved")

while True:
    line = input("Start Browser and keep it open until 'exit' is entered: ")
    print(f"got {line}")
    if line == "exit":
        break
    
    
if __name__ == '__main__':
    pass