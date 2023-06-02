from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 设置ChromeDriver的路径
driver_path = "./chromedriver_win32/chromedriver"

# 创建一个新的Chrome浏览器实例
driver = webdriver.Chrome(executable_path=driver_path)

# 打开企查查网站
driver.get("https://www.qcc.com")

# 找到搜索框并输入指定公司的名称，然后按Enter键进行搜索
search_box = driver.find_element_by_name("key")
search_box.send_keys("江西省佳铭玻化新材料有限公司")
search_box.send_keys(Keys.RETURN)

# 等待搜索结果页面加载完成
driver.implicitly_wait(10)

# 找到搜索结果中的第一个公司链接并点击
company_link = driver.find_element_by_css_selector(".ma_h1")
print(company_link)
#
# company_link.click()
#
# # 切换到新打开的标签页
# driver.switch_to.window(driver.window_handles[-1])
#
# # 找到法人信息的标签页并点击
# legal_tab = driver.find_element_by_css_selector(".nav.nav-tabs li:nth-child(2)")
# legal_tab.click()
#
# # 找到法人信息并提取法人ID
# legal_info = driver.find_element_by_css_selector(".humancompany tbody tr:nth-child(2) td:nth-child(2)")
# legal_id = legal_info.text
#
# # 输出法人ID
# print("法人ID为：", legal_id)
#
# # 关闭浏览器
# driver.quit()