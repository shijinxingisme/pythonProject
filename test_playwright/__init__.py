# https://github.com/shijianzhihu/Playwright-Docs/blob/main/playwright/Playwright%E4%BB%8B%E7%BB%8D.md

# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     page.goto("http://baidu.com")
#     print(page.title())
#     browser.close()
#



# import asyncio
# from playwright.async_api import async_playwright
#
# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         page = await browser.new_page()
#         await page.goto("http://baidu.com")
#         print(await page.title())
#         await browser.close()
#
# asyncio.run(main())

# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.webkit.launch()
#     page = browser.new_page()
#     page.goto("http://baidu.com")
#     page.screenshot(path="example.png")
#     browser.close()


# playwright codegen wikipedia.org
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://power.bjguolian.cn/")
    page.goto("https://power.bjguolian.cn/#/")
    page.goto("https://power.bjguolian.cn/#/login?redirect=%2Fdashboard")
    page.get_by_role("tab", name="密码登录").click()
    page.get_by_placeholder("请输入密码（同OA密码）").click()
    page.get_by_placeholder("请输入您的员工编号/身份证号/邮箱").click()
    page.get_by_placeholder("请输入您的员工编号/身份证号/邮箱").press("CapsLock")
    page.get_by_placeholder("请输入您的员工编号/身份证号/邮箱").fill("F")
    page.get_by_placeholder("请输入您的员工编号/身份证号/邮箱").press("CapsLock")
    page.get_by_placeholder("请输入您的员工编号/身份证号/邮箱").fill("F1")
    page.get_by_placeholder("请输入您的员工编号/身份证号/邮箱").press("CapsLock")
    page.get_by_placeholder("请输入您的员工编号/身份证号/邮箱").fill("F1A")
    page.get_by_placeholder("请输入您的员工编号/身份证号/邮箱").press("CapsLock")
    page.get_by_placeholder("请输入您的员工编号/身份证号/邮箱").fill("F1A76")
    page.get_by_placeholder("请输入您的员工编号/身份证号/邮箱").press("Tab")
    page.get_by_placeholder("请输入密码（同OA密码）").click()
    page.get_by_placeholder("请输入密码（同OA密码）").fill("123qwer")
    page.get_by_role("button", name="登录").click()
    with page.expect_popup() as page1_info:
        page.get_by_text("已订阅工作流引擎").click()
    page1 = page1_info.value

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
