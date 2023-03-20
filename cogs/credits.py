import discord
from discord import app_commands
from discord.ext import commands
import config

class Credits(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Credits cog loaded.')
    

    @app_commands.command(name="credits", description="Just some credits")
    async def credits(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Credits:", color=discord.Color.blue())
        embed.add_field(name="Api:", value="[Hypixel skyblock official api](https://api.hypixel.net/) and [HyAuctions api](https://sky.coflnet.com/api)")
        embed.add_field(name="Repository:", value="Click [here](https://github.com/ElGeroIngles) to go directly to my GitHub repositories", inline= False)
        embed.add_field(name="Special thanks:", value="Special thanks to Hypixel for developing such gamemode, my friends for helping me to make this bot and specially you for using it ;)", inline= False)
        embed.set_footer(text=f"Made by ElGeroIngles 🔹 {config.VERSION}", icon_url="https://cdn.discordapp.com/avatars/715149020883976252/4f1ef6d5b23a9ccadbf72c86bedad68a.webp?size=80")
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Credits(bot))
