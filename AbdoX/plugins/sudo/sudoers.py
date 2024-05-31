from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.types import Message
from strings.filters import command
from AbdoX  import app
from pyrogram.types import InputMediaVideo
from AbdoX .misc import SUDOERS
from AbdoX .utils.database import add_sudo, remove_sudo
from AbdoX .utils.decorators.language import language
from AbdoX .utils.extraction import extract_user
from AbdoX .utils.inline import close_markup
from config import BANNED_USERS, OWNER_ID, BAND


@app.on_message(command(["addsudo", "رفع مطور"]) & filters.user(OWNER_ID))
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id in SUDOERS:
        return await message.reply_text(_["sudo_1"].format(user.mention))
    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(_["sudo_2"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(command(["/delsudo", "/rmsudo", "تنزيل مطور"]) & filters.user(OWNER_ID))
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id not in SUDOERS:
        return await message.reply_text(_["sudo_3"].format(user.mention))
    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text(_["sudo_4"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(command(["/sudolist", "/listsudo", "/sudoers"," المطورين"]) & ~BANNED_USERS)
async def sudoers_list(client, message: Message):
    keyboard = [[InlineKeyboardButton("๏المطورين ๏", callback_data="check_sudo_list")]]
    reply_markups = InlineKeyboardMarkup(keyboard)

    # await message.reply_photo(photo="https://telegra.ph/file/36dd7c5bd7104baa0eca7.jpg", caption="**» ᴄʜᴇᴄᴋ sᴜᴅᴏ ʟɪsᴛ ʙʏ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ.**\n\n**» ɴᴏᴛᴇ:**  ᴏɴʟʏ sᴜᴅᴏ ᴜsᴇʀs ᴄᴀɴ ᴠɪᴇᴡ. ", reply_markup=reply_markups)
    await message.reply_photo(photo="https://telegra.ph/file/609670f31b8d02e512d65.jpg",caption="**»اعرض قائمة المطورين باستخدام الزر أدناه\n\n» ملاحظة: لا يمكنك رؤيتها‌‌ **",reply_markup=reply_markups)


# noinspection PyUnreachableCode
@app.on_callback_query(filters.regex("^check_sudo_list$"))
async def check_sudo_list(client, callback_query: CallbackQuery):
    keyboard = []
    if callback_query.from_user.id not in SUDOERS:
        return await callback_query.answer("هذا الامر للمطورين فقط", show_alert=True)
    else:
        user = await app.get_users(OWNER_ID)

        user_mention = (user.first_name if not user.mention else user.mention)
        caption = f"** قائمة المسؤولين\n\n🌹مالك الروبوت‌‌➥ {user_mention}\n\n**"

        keyboard.append([InlineKeyboardButton("๏ دخول للبوت ๏", url=f"tg://openmessage?user_id={OWNER_ID}")])

        count = 1
        for user_id in SUDOERS:
            if user_id != OWNER_ID:
                try:
                    user = await app.get_users(user_id)
                    user_mention = user.mention if user else f"** المطور {count} ايدي:** {user_id}"
                    caption += f"** المطور** {count} **»** {user_mention}\n"
                    button_text = f"๏ المطورين {count} ๏"
                    keyboard.append([InlineKeyboardButton(button_text, url=f"tg://openmessage?user_id={user_id}")]
                                    )
                    count += 1
                except:
                    continue

        # Add a "Back" button at the end
        keyboard.append([InlineKeyboardButton("๏ رجوع ๏", callback_data="back_to_main_menu")])

        if keyboard:
            reply_markup = InlineKeyboardMarkup(keyboard)
            await callback_query.message.edit_caption(caption=caption, reply_markup=reply_markup)


@app.on_callback_query(filters.regex("^back_to_main_menu$"))
async def back_to_main_menu(client, callback_query: CallbackQuery):
    keyboard = [[InlineKeyboardButton("๏المطورين  ๏", callback_data="check_sudo_list")]]
    reply_markupes = InlineKeyboardMarkup(keyboard)
    await callback_query.message.edit_caption(
        caption="**» اعرض قائمة المطورين باستخدام الزر أدناه\n\n» ملاحظة: لا يمكنك رؤيتها‌‌**",
        reply_markup=reply_markupes)
