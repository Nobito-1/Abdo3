import asyncio


import random


from AbdoX import app


from pyrogram.types import (InlineKeyboardButton,


                            InlineKeyboardMarkup, Message)


from pyrogram import filters, Client





@app.on_message(
    filters.command(["المميزات"], "")
& filters.group
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**⦿   قايمه مميزات سورس  :\n
╮⦿  المطور
│᚜⦿ سؤال
│᚜⦿ مين في الكول 
│᚜⦿ تفعيل الاذان
│᚜⦿ كت
│᚜⦿ احكام
│᚜⦿ افتح الكول
│᚜⦿ احرف
│᚜⦿ الرابط
│᚜⦿ البنك 
│᚜⦿ منع تصفيه تلقائي
│᚜⦿ رفع مشرف
│᚜⦿ بحث
│᚜⦿  المطور
│᚜⦿ زخرفه
│᚜⦿ مميزات
│᚜⦿ همسه
│᚜⦿ بوت
│᚜⦿ تحميل
│᚜⦿ لو خيروك
│᚜⦿ معلومات الجروب
│᚜⦿ طرد كتم
│᚜⦿ تلكراف ميديا
│᚜⦿ سورس 
│᚜⦿ صراحه
│᚜⦿ صور
│᚜⦿ صور بنات 
│᚜⦿ صور شباب
│᚜⦿ السورس 
│᚜⦿ كتم
│᚜⦿ اقتباس
│᚜⦿ هيدرات
│᚜⦿ اذكار 
╯⦿  بث مباشر للقنوات 
[𝗦𝗼𝘂𝗿𝗰𝗲](https://t.me/l2_2Y) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- 𝐀 𝐁 𝐃 𝐎 𝐨 ↺", url=f"https://t.me/EU_TM"),                        
                 ],[
                InlineKeyboardButton(
                        "close", callback_data="close"),
               ],
          ]
        ),
    )

