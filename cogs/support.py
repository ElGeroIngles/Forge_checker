import discord
from discord import app_commands
from discord.ext import commands
import config

class Support(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Support cog loaded.')
    

    @app_commands.command(name="support", description="Support me and my projects!")
    async def support(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Support me!", color=discord.Color.blue())
        embed.set_thumbnail(url="https://play-lh.googleusercontent.com/aMb_Qiolzkq8OxtQZ3Af2j8Zsp-ZZcNetR9O4xSjxH94gMA5c5gpRVbpg-3f_0L7vlo")
        embed.add_field(name="", value="You can support me and this bot donating in my [BuyMeACoffe](https://www.buymeacoffee.com/ElGeroIngles)!")
        embed.set_footer(text=f"Made by ElGeroIngles 🔹 {config.VERSION} 🔹 Support the bot! --> /support", icon_url="https://cdn.discordapp.com/avatars/715149020883976252/4f1ef6d5b23a9ccadbf72c86bedad68a.webp?size=80")
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Support(bot))
