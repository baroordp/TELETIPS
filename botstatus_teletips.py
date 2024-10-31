from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os
import calendar

app = Client(
    name="botstatus_teletips",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    session_string=os.environ["SESSION_STRING"]
)
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]



def generate_progress_bar(percentage, total_circles=15):
    filled_circles = int(round(percentage / 100 * total_circles))
    empty_circles = total_circles - filled_circles
    return "●" * filled_circles + "○" * empty_circles

def calculate_progress():
    today = datetime.datetime.now(pytz.timezone(TIME_ZONE))
    days_in_year = 366 if calendar.isleap(today.year) else 365

    # Calculate year, month, and week progress
    year_progress = today.timetuple().tm_yday / days_in_year * 100
    month_progress = today.month / 12 * 100  # Fraction of the year based on months completed
    week_progress = (today.isocalendar()[1] / 52) * 100

    # Date and time information
    day_of_week = today.strftime("%A")
    current_date = today.strftime("%B %d, %Y")

    return year_progress, month_progress, week_progress, day_of_week, current_date, days_in_year  # Add days_in_year here

async def main_teletips():
    async with app:
        while True:
            print("Checking...")
            year_progress, month_progress, week_progress, day_of_week, current_date, days_in_year = calculate_progress()  # Unpack days_in_year here
            header = f"✨ | **ᖇᗴᗩᒪ-TIᗰᗴ ᗷOT ՏTᗩTᑌՏ**"
            xxx_teletips = header
            for bot in BOT_LIST:
                try:
                    yyy_teletips = await app.send_message(bot, "/start")
                    aaa = yyy_teletips.id
                    await asyncio.sleep(10)
                    zzz_teletips = app.get_chat_history(bot, limit=1)
                    async for ccc in zzz_teletips:
                        bbb = ccc.id
                    if aaa == bbb:
                        xxx_teletips += f"\n\n🤖  @{bot}\n        └ **Dᴏᴡɴ** ❌"
                        for bot_admin_id in BOT_ADMIN_IDS:
                            try:
                                await app.send_message(int(bot_admin_id), f"🚨 **Beep! Beep!! @{bot} is down** ❌")
                            except Exception:
                                pass
                        await app.read_chat_history(bot)
                    else:
                        xxx_teletips += f"\n\n🤖  @{bot}\n        └ **Aʟɪᴠᴇ** ✅"
                        await app.read_chat_history(bot)
                except FloodWait as e:
                    await asyncio.sleep(e.x)

            time = datetime.datetime.now(pytz.timezone(TIME_ZONE))
            last_update = time.strftime("%d %b %Y at %I:%M %p")
            
            # Use the generate_progress_bar function for each progress type
            progress_info = f"""

🌕 🌖 🌗 🌘 🌑 🌒 🌓 🌔 🌕

**Tɪᴍᴇ Is Tʜᴇ Vᴀʟᴜᴀʙʟᴇ Assᴇᴛ Yᴏᴜ Hᴀᴠᴇ ✓**

Today Is
{day_of_week}, {current_date}

Year {time.year}:
{generate_progress_bar(year_progress)}   {year_progress:.2f}%

Month Count: {time.month}/12
{generate_progress_bar(month_progress)}   {month_progress:.2f}%
Month Remaining: {12 - time.month}

Week Count: {time.isocalendar()[1]}/52
{generate_progress_bar(week_progress)}   {week_progress:.2f}%
Week Remaining: {52 - time.isocalendar()[1]}

Days Count: {time.timetuple().tm_yday}/{days_in_year}
{generate_progress_bar(year_progress)}   {year_progress:.2f}%
Days Remaining: {days_in_year - time.timetuple().tm_yday}

∎ Last Checked:
▸ Date: {day_of_week}, {current_date}
▸ Time: {time.strftime("%I:%M:%S %p")}
▸ Time Zone: {TIME_ZONE}

✧ Status Are Updated Daily ✨
"""

            xxx_teletips += f"\n\n✔️ Last checked on: {last_update} ({TIME_ZONE})\n\n<i>♻️ 𝚁𝚎𝚏𝚛𝚎𝚜𝚑𝚎𝚜 𝚊𝚞𝚝𝚘𝚖𝚊𝚝𝚒𝚌𝚊𝚕𝚕𝚢</i>"
            xxx_teletips += progress_info
            await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_teletips)
            print(f"Last checked on: {last_update}")
            await asyncio.sleep(21600)  # Check once daily

app.run(main_teletips())
