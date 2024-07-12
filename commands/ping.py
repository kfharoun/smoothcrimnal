import discord
from discord.ext import commands
# core discord libraries

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # funct that will be run every time that command runs
    @commands.command()
    async def ping(self, ctx):
        # two required variables for a commant
        # every time someone types in ping this will run
        # await ctx.reply(f"{ctx.author.id}, youre a smooth crimnal!")
        # if ctx.author.id == 487817463094968351:
        #     await ctx.reply(f"{ctx.author} you're an imposter, officials have been notified")
        # else:
        #     await ctx.reply(f"{ctx.author}, you're a smooth crimnal")
        if ctx.author.id ==487817463094968351:
            embed=discord.Embed(title="gideon?!", description="youve been caught!", color=0xff0000)
            embed.add_field(name=" ", value="you're not a smoothec rimnal", inline=False)
            embed.add_field(name=" ", value="*crimnal", inline=False)
            await ctx.send(embed=embed)
        else: 
            embed=discord.Embed(title=f"woah, that's {ctx.author}!", description="we def cant catch you", color=0xf7e0ff)
            embed.add_field(name=" ", value="you're a smooth ecmnri", inline=False)
            embed.add_field(name=" ", value="*crimnal", inline=False)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Ping(bot))