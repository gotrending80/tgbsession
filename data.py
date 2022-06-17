from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("Start Generating Session", callback_data="generate")]

    home_buttons = [
        [InlineKeyboardButton(text="Return Home", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
    ]

    START = """
Welcome To Telegram Bot Generate Session
    """

    HELP = """
/start - Start the Bot
/about - About The Bot
/help - This Message
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
Telegram Bot Generate Session
    """
