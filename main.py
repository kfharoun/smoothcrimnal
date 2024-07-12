import discord 
import asyncio
from discord.ext import commands
from commands.ping import Ping
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=">", intents=intents)

async def main():
    async with bot:
        await bot.add_cog(Ping(bot))
        # await bot.start("discord_token")
        #github wont let me push this without this uncommented out
        # taken from discord developers / bot /token

asyncio.run(main())
# this is a call
# now the bot will run

# after inviting to discord, run python3 main.py
