import discord
from discord import app_commands
from discord.ext import commands
import config

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help cog loaded.')
    

    @app_commands.command(name="help", description="Need some help?")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Need some help?", color=discord.Color.blue())
        embed.add_field(name="", value="``/checkforge``: Checks the forge for the bests flips.\n``/help``: Shows this message.\n``/credits``: Just some credits of some of the thigs I used.\n``/support``: Support me!.")
        embed.set_footer(text=f"Made by ElGeroIngles 🔹 {config.VERSION} 🔹 Support the bot! --> /support", icon_url="https://cdn.discordapp.com/avatars/715149020883976252/4f1ef6d5b23a9ccadbf72c86bedad68a.webp?size=80")
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot))
