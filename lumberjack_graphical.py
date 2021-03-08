import time
from io import BytesIO

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# High scores may result in your ban
# Keep your score limit under 800 - 900
score_loop = 42
# your score = 12 * score_loop + 2
game_url = 'https://tbot.xyz/lumber/#your_unique_id'


def image_analyze(screenshot, x):
    # Checks for pixel color to detect branches and decide which button to click
    instructions = []
    if x == 173:
        instructions.append('R')
    else:
        instructions.append('L')
    if screenshot.getpixel((173, 414))[0] == 161:
        instructions.append('R')
    else:
        instructions.append('L')
    if screenshot.getpixel((173, 314))[0] == 161:
        instructions.append('R')
    else:
        instructions.append('L')
    if screenshot.getpixel((173, 214))[0] == 161:
        instructions.append('R')
    else:
        instructions.append('L')
    if screenshot.getpixel((173, 114))[0] == 161:
        instructions.append('R')
    else:
        instructions.append('L')
    if screenshot.getpixel((173, 14))[0] == 161:
        instructions.append('R')
    else:
        instructions.append('L')
    return instructions


def click_buttons(instructions):
    for instruction in instructions:
        if instruction == 'L':
            body.send_keys(Keys.ARROW_LEFT)
            time.sleep(0.05)
            body.send_keys(Keys.ARROW_LEFT)
            time.sleep(0.05)
        else:
            body.send_keys(Keys.ARROW_RIGHT)
            time.sleep(0.05)
            body.send_keys(Keys.ARROW_RIGHT)
            time.sleep(0.05)


# Run in headless state for performance boost and higher scores
# These delays were calibrated for my system's performance so you may need to tune them up yourself
# options = webdriver.FirefoxOptions()
# options.headless = True
# driver = webdriver.Firefox(options=options)
driver = webdriver.Firefox()
driver.set_window_size(300, 1000)
driver.get(game_url)
button_left = driver.find_element_by_id('button_left')
button_right = driver.find_element_by_id('button_right')
body = driver.find_element_by_tag_name('body')
# This starts the game
button_left.click()
body.send_keys(Keys.ARROW_LEFT)
time.sleep(0.05)
body.send_keys(Keys.ARROW_LEFT)
time.sleep(0.05)
canvas = driver.find_element_by_tag_name('canvas')
for i in range(score_loop):
    time.sleep(0.11)
    png_screenshot = canvas.screenshot_as_png
    image_screenshot = Image.open(BytesIO(png_screenshot))
    # Checks for the nearest branch
    if image_screenshot.getpixel((281, 514))[0] == 161:
        click_buttons(image_analyze(image_screenshot, 281))
    else:
        click_buttons(image_analyze(image_screenshot, 173))
# To close the driver in case it's headless
# driver.close()
