from selenium import webdriver

# High scores may result in your ban
# Keep your score limit under 800 - 900
score = 500
game_url = 'http://tbot.xyz/math/#your_unique_id'
driver = webdriver.Firefox()
driver.get(game_url)
button_correct = driver.find_element_by_id('button_correct')
button_wrong = driver.find_element_by_id('button_wrong')
text_x = driver.find_element_by_id('task_x')
text_y = driver.find_element_by_id('task_y')
text_operation = driver.find_element_by_id('task_op')
text_result = driver.find_element_by_id('task_res')
# This starts the game
button_correct.click()
for i in range(score):
    x = text_x.get_attribute("innerHTML")
    y = text_y.get_attribute("innerHTML")
    operation = text_operation.get_attribute("innerHTML")
    given_result = text_result.get_attribute("innerHTML")
    # Character correction
    if operation == '×':
        operation = '*'
    elif operation == '–':
        operation = '-'
    calculated_result = int(eval(x + operation[0] + y))
    if str(calculated_result) == given_result:
        button_correct.click()
    else:
        button_wrong.click()
