from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("Start Generating Session", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="Return Home", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
    ]

    START = """
Welcome
    """

    HELP = """
/start - Start the Bot
/about - About The Bot
/help - This Message
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
Telegram Bot to generate Pyrogram and Telethon string session by @StarkBots
    """
