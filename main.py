from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def auto_login_campus(username, password):
    # 使用 Chrome 浏览器驱动
    driver = webdriver.Edge()

    # 访问校园网的登录页面
    driver.get("https://pass.neu.edu.cn/tpass/login?service=http%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_portal_sso%3Fac_id%3D16")

    # 找到用户名和密码输入框
    username_input = driver.find_element(By.NAME, "un")  # 替换为实际输入框名称
    password_input = driver.find_element(By.NAME, "pd")  # 替换为实际输入框名称

    # 输入用户名和密码
    username_input.send_keys(username)
    password_input.send_keys(password)

    # 提交表单
    password_input.send_keys(Keys.RETURN)

    # 检查是否登录成功
    if "邮箱绑定" in driver.page_source:
        print("Login successful!")

    else:
        print("Login failed.")

# 使用你的用户名和密码
auto_login_campus("", "")
