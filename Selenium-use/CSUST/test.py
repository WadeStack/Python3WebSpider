from selenium import webdriver
import time

browser = webdriver.Chrome()
url = 'http://10.64.6.5/'
browser.get(url)
button1 = browser.find_element_by_id('m14')
button1.click()
time.sleep(1)
win2 = browser.current_window_handle
index = browser.switch_to.frame('frmHomeShow')  #iframe嵌套的切入当前页面
input1 = browser.find_element_by_id('txt_asmcdefsddsd')
input1.send_keys('学号')
input2 = browser.find_element_by_id('txt_pewerwedsdfsdff')
input2.send_keys('密码')
