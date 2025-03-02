import json
import aiofiles
import os
from typing import Dict
from base64 import b64encode, b64decode
from rsa import encrypt, PublicKey
import hmac
import struct
from time import time
from hashlib import sha1
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

path_secret_maFile = './secret.maFile'


async def load_steam_guard() -> Dict[str, str]:
    if os.path.isfile(path_secret_maFile):
        async with aiofiles.open(path_secret_maFile, 'r') as f:
            content = await f.read()
            return json.loads(content, parse_int=str)
    else:
        return json.loads(path_secret_maFile, parse_int=str)


async def generate_one_time_code(shared_secret: str, timestamp: int = None) -> str:
    if timestamp is None:
        timestamp = int(time())
    time_buffer = struct.pack('>Q', timestamp // 30)  # pack as Big endian, uint64
    time_hmac = hmac.new(b64decode(shared_secret), time_buffer, digestmod=sha1).digest()
    begin = ord(time_hmac[19:20]) & 0xF
    full_code = struct.unpack('>I', time_hmac[begin:begin + 4])[0] & 0x7FFFFFFF  # unpack as Big endian uint32
    chars = '23456789BCDFGHJKMNPQRTVWXY'
    code = ''

    for _ in range(5):
        full_code, i = divmod(full_code, len(chars))
        code += chars[i]

    return code


async def start(update: Update) -> None:
    user = update.message.from_user
    if user.username == 'your login tg':
        steam_guard = await load_steam_guard()
        shared_secret = steam_guard['shared_secret']
        code = await generate_one_time_code(shared_secret)
        print(code)
        await update.message.reply_text(f'your code: {code}')
    else:
        await update.message.reply_text('Not Auth')


app = ApplicationBuilder().token("707******:AAEAH6kUvEl8txpTN your TOKEN tg bot").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
