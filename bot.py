from discord import Client, Intents, Embed
import discord
from discord_slash import SlashCommand, SlashContext
import webbrowser
bot = Client(intents=Intents.default())
slash = SlashCommand(bot)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import os

@slash.slash(name="test")
async def test(ctx: SlashContext):
    await ctx.send("자가진단을 시작합니다")
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(/app/.chromedriver/bin/chromedriver, chrome_options=options)



    url = 'https://hcs.eduro.go.kr/#/relogin'
    time.sleep(0.1)
    driver.get(url)
    driver.find_element_by_id("btnConfirm2").click()
    driver.find_element_by_class_name("searchBtn").click()
    driver.find_element_by_xpath('//*[@id="sidolabel"]/option[12]').click()
    driver.find_element_by_xpath('//*[@id="crseScCode"]/option[4]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="orgname"]').send_keys("오창중학교")
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a').click()
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()

    driver.find_element_by_xpath('//*[@id="user_name_input"]').send_keys("김은율")
    driver.find_element_by_xpath('//*[@id="birthday_input"]').send_keys("070703")
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/div/button/img').click()
    time.sleep(0.2)
    driver.find_element_by_css_selector(f'[aria-label="0"]').click()
    time.sleep(0.2)
    driver.find_element_by_css_selector(f'[aria-label="7"]').click()
    time.sleep(0.2)
    driver.find_element_by_css_selector(f'[aria-label="0"]').click()
    time.sleep(0.2)
    driver.find_element_by_css_selector(f'[aria-label="3"]').click()


    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    time.sleep(1)
    driver.find_element_by_class_name('btn').click()
    time.sleep(2)
    for i in range(1, 4):
        driver.find_element_by_xpath(f'//*[@id="container"]/div/div/div[2]/div[2]/dl[{i}]/dd/ul/li[1]/label').click()
        time.sleep(0.3)
    driver.find_element_by_xpath(f'//*[@id="container"]/div/div/div[2]/div[2]/dl[4]/dd/ul/li[1]/label').click()
    time.sleep(0.3)
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    time.sleep(3)
    screenshot = driver.save_screenshot('자가진단.png')
    driver.quit
    await ctx.send(file=discord.File('자가진단.png'))

bot.run(os.environ['token'])  
