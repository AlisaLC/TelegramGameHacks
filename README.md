# TelegramGameHacks
Just some python scripts for Telegram games

## Main Script
main.py is not limited to only one game and can support all [@gamebot](https://t.me/gamebot) games including:
- [LumberJack](https://tbot.xyz/lumber/)
- [Math Battle](https://tbot.xyz/math/)
- [Corsairs](https://tbot.xyz/corsairs/)

It does so by submitting your desired score to the server.
### Prerequisites
- Python 3.6 or higher
- `pip install requests`

## Math Battle Graphical Script
math_battle_graphical.py can only support Math Battle but it does so using `selenium` and your browser.
It reads the page and calculates each mathematical operation it sees. 

### Prerequisites
- Python 3.6 or higher
- `pip install selenium`
- [geckodriver for Firefox](https://github.com/mozilla/geckodriver/releases)

You can learn more about installing selenium in [here](https://selenium-python.readthedocs.io/installation.html)

## LumberJack Graphical Script
lumberjack_graphical.py can only support LumberJack but it does so using `selenium` and your browser.
It reads the page and detects branches based on the screenshot it takes, so resizing the browser may cause it to crash.
Because of the time limit, the maximum score of this script can be limited to your system's specifications. (for me it was 700)

### Prerequisites
- Python 3.6 or higher
- `pip install selenium`
- [geckodriver for Firefox](https://github.com/mozilla/geckodriver/releases)

You can learn more about installing selenium in [here](https://selenium-python.readthedocs.io/installation.html)
