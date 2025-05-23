from load_env import get_discord_token
import discord

token = get_discord_token()
print(token, type(token))

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


# 調用event函式庫
@client.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份1 --> {client.user}")


@client.event
# 當頻道有新訊息
async def on_message(message):
    # 排除機器人本身的訊息，避免無限循環
    if message.author == client.user:
        return
    # 新訊息包含Hello，回覆Hello, world!
    if message.content == "Hello":
        # await message.channel.send("Hello, world!")
        await message.channel.send("這是第一行\nhttps://www.youtube.com/\n這是第三行")


client.run(token)
