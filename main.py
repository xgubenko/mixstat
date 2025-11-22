import asyncio
import logging
import os
from dotenv import load_dotenv
from telegram import Bot
import datetime
import urllib.request
import json
# import schedule
import time

# Load environment variables from .env file
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def main():
    # Get bot token and channel ID from environment variables
    TOKEN = os.getenv("BOT_TOKEN")
    CHANNEL_ID = os.getenv("CHANNEL_ID")
    
    # Validate that credentials are provided
    if not TOKEN or not CHANNEL_ID:
        logger.error("BOT_TOKEN and CHANNEL_ID must be set in .env file")
        return
    
    # Create bot instance
    bot = Bot(token=TOKEN)
    
    try:
        # Send hello message to channel
        await bot.send_message(chat_id=CHANNEL_ID, text=f"Bot started successfully at {datetime.datetime.now()}")
        logger.info("Message sent successfully!")
        contents = urllib.request.urlopen("https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.json?iss.meta=off&iss.only=marketdata&marketdata.columns=SECID,LAST").read()
        data = json.loads(contents)
        
        # Extract SBER value from marketdata
        marketdata_list = data['marketdata']['data']
        sber_value = None
        for item in marketdata_list:
            if item[0] == 'SBER':
                sber_value = item[1]
                break
        
        if sber_value is not None:
            await bot.send_message(chat_id=CHANNEL_ID, text=f"SBER: {sber_value}")
        else:
            await bot.send_message(chat_id=CHANNEL_ID, text="SBER value not found")
    except Exception as e:
        logger.error(f"Error sending message: {e}")

if __name__ == '__main__':
    asyncio.run(main())

# def job():
#     print("I'm working...")

# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)