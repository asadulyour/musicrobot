# 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 𝐚𝐧𝐝 𝐄𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭𝐬
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

# 𝐈𝐧𝐭𝐞𝐫𝐧𝐚𝐥 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 (@𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫)
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

# 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 //𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 @𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫
API_HASH = getenv("API_HASH", "7f10cf5e8390a3ff33c7bbc581469984")
API_ID = int(getenv("API_ID", "9620148"))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "𝘽𝙍𝙊𝙆𝙀𝙉 𝘼𝙎𝙎𝙄𝙎𝙏𝘼𝙉𝙏")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "brokenx_Assistant")
BOT_IMAGE = getenv("BOT_IMAGE", "https://te.legra.ph/file/e70f61a413b17c6add2a1.jpg")
BOT_NAME = getenv("BOT_NAME", "𝘽𝙍𝙊𝙆𝙀𝙉 𝙓 (𝙈𝙐𝙎𝙄𝘾)")
BOT_TOKEN = getenv("BOT_TOKEN", "5448034271:AAH-DIWacTVqpi6cMPGf131PwUj-uKjU0Ks")
BOT_USERNAME = getenv("BOT_USERNAME", "BROKENX_musicplayarbot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
OWNER_NAME = getenv("OWNER_NAME", "- ❛𝗠𝘁𝘀 ➻ 𝗕𝗿𝗼𝗸𝗲𝗻 𝗕𝗼𝘆 [🇮🇳]")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Broken_boyxd")
SOURCE_CODE = getenv("SOURCE_CODE", "https://t.me/"Broken_boyxd)
STRING_SESSION = getenv("STRING_SESSION", "BQB_PENmyW-SsPsVmPnJvf9lPaaZSVxRKk4sDb2pGZPimo31G-wvjVFov3TwCL1bhpf-fbme2vHFpgJJ0HsFWX5u7dqY7oiNPel53205MslhaJhiybvq1cV9MRtCehUdK05PdmGfuTbCzbtokJh4f3gqhXekk_g3yQrVhtxNWiSAfX-4rVQTMfuUnezGxdTaZv4PuSyFSUVhl_gERiowZzkksIXkUJCusTnpSYQF7gfmjmkZLm3gY4haAMQyfXUZvRvwaQkZlbfOgRTgrcw6jewvmmV9LOmf8TIObI9aDq9J2EMR3gSAfHNS7s576XAkcrOEEyeE2D4ELuV5BHbVBOvZAAAAAUBfQeEA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5374951905").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/MYSTERIOUS_CHATS")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/RTH_FIGHTERS")

# 𝐃𝐨 𝐍𝐨𝐭 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐢𝐬 𝐋𝐢𝐧𝐞𝐬 // 𝐈𝐠𝐧𝐨𝐫𝐞 𝐓𝐡𝐢𝐬 (𝐀𝐝𝐢𝐭𝐲𝐚 𝐇𝐚𝐥𝐝𝐞𝐫) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/kaalxd")
