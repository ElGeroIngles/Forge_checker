import discord
from discord import app_commands
from discord.ext import commands
import requests
import config

class Forge(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Forge cog loaded.')
    

    @app_commands.command(name="checkforge", description="Checks the forge for the best flips")
    @app_commands.describe(options='Checks the forge for the best flips')
    @app_commands.choices(options=[
        discord.app_commands.Choice(name='Refined ores', value=1),
        discord.app_commands.Choice(name='Item casting', value=2),
    ])
    async def checkforge(self, interaction: discord.Interaction, options: discord.app_commands.Choice[int]):
        # await interaction.response.send_message(f'Color selected: {options.name}')
        if options.value == 1:
            print('Selected Refined Ores')

            def cast():
                print("Calculating...")
                b_response = requests.get('https://api.hypixel.net/skyblock/bazaar')
                ft_response = requests.get('https://sky.coflnet.com/api/auctions/tag/FUEL_TANK/sold')
                bh_response = requests.get('https://sky.coflnet.com/api/auctions/tag/BEJEWELED_HANDLE/sold')
                gj_response = requests.get('https://sky.coflnet.com/api/auctions/tag/GLACITE_JEWEL/sold')
                gp_response = requests.get('https://sky.coflnet.com/api/auctions/tag/GOLDEN_PLATE/sold')
                de_response = requests.get('https://sky.coflnet.com/api/auctions/tag/DRILL_ENGINE/sold')
                mp_response = requests.get('https://sky.coflnet.com/api/auctions/tag/MITHRIL_PLATE/sold')
                gm_response = requests.get('https://sky.coflnet.com/api/auctions/tag/GEMSTONE_MIXTURE/sold')
                

                # Refined diamond:
                e_diamond_block_b_price = b_response.json()['products']['ENCHANTED_DIAMOND_BLOCK']['quick_status']['buyPrice']
                r_diamond_s_price = b_response.json()['products']['REFINED_DIAMOND']['quick_status']['sellPrice']
                r_diamond_profit = r_diamond_s_price - (e_diamond_block_b_price*2)
                cast.r_diamond_profit = round(r_diamond_profit, 2)
                print(f'Refined diamond profit: {r_diamond_profit}')

                # Refined mithril:
                e_mithril_b_price = b_response.json()['products']['ENCHANTED_MITHRIL']['quick_status']['buyPrice']
                r_mithril_s_price = b_response.json()['products']['REFINED_MITHRIL']['quick_status']['sellPrice']
                r_mithril_profit = r_mithril_s_price - (e_mithril_b_price*160)
                cast.r_mithril_profit = round(r_mithril_profit, 2)
                print(f'Refined mithril profit: {r_mithril_profit}')

                # Refined titanium:
                e_titanium_b_price = b_response.json()['products']['ENCHANTED_TITANIUM']['quick_status']['buyPrice']
                r_titanium_s_price = b_response.json()['products']['REFINED_TITANIUM']['quick_status']['sellPrice']
                r_titanium_profit = r_titanium_s_price - (e_titanium_b_price*16)
                cast.r_titanium_profit = round(r_titanium_profit, 2)
                print(f'Refined titanium profit: {r_titanium_profit}')

                # Fuel tank:
                ft_s_price = 0
                i = 0
                while ft_s_price == 0:
                    ft_count = ft_response.json()[i]['count']
                    ft_bin = ft_response.json()[i]['bin']
                    if ft_count == 1 and ft_bin == True:
                        ft_s_price = ft_response.json()[i]['highestBidAmount']
                    else:
                        i = i + 1
                e_coal_block_b_price = b_response.json()['products']['ENCHANTED_COAL_BLOCK']['quick_status']['buyPrice']
                ft_profit = ft_s_price - (e_coal_block_b_price*2)
                cast.ft_profit = round(ft_profit, 2)
                print(f'Fuel tank profit: {ft_profit}')

                # Bejeweled handle:
                gj_b_price = 0
                i = 0
                while gj_b_price ==0:
                    gj_count = gj_response.json()[i]['count']
                    gj_bin = gj_response.json()[i]['bin']
                    if gj_count == 1 and gj_bin == True:
                        gj_b_price = gj_response.json()[i]['highestBidAmount']
                    else:
                        i = i + 1
                bh_s_price = 0
                i = 0
                while bh_s_price ==0:
                    bh_count = bh_response.json()[i]['count']
                    bh_bin = bh_response.json()[i]['bin']
                    if bh_count == 1 and bh_bin == True:
                        bh_s_price = bh_response.json()[i]['highestBidAmount']
                    else:
                        i = i + 1
                bh_profit = bh_s_price - (gj_b_price*3)
                cast.bh_profit = round(bh_profit, 2)
                print(f'Bejeweled handle profit: {bh_profit}')

                # Drill engine:
                e_iron_block_b_price = b_response.json()['products']['ENCHANTED_IRON_BLOCK']['quick_status']['buyPrice']
                e_redstone_block_b_price = b_response.json()['products']['ENCHANTED_REDSTONE_BLOCK']['quick_status']['buyPrice']
                gp_b_price = 0
                i = 0
                while gp_b_price ==0:
                    gp_count = gp_response.json()[i]['count']
                    gp_bin = gp_response.json()[i]['bin']
                    if gp_count == 1 and gp_bin == True:
                        gp_b_price = gp_response.json()[i]['highestBidAmount']
                    else:
                        i = i + 1
                treasurite_b_price = b_response.json()['products']['TREASURITE']['quick_status']['buyPrice']
                de_s_price = 0
                i = 0
                while de_s_price ==0:
                    de_count = de_response.json()[i]['count']
                    de_bin = de_response.json()[i]['bin']
                    if de_count == 1 and de_bin == True:
                        de_s_price = de_response.json()[i]['highestBidAmount']
                    else:
                        i = i + 1
                r_diamond_b_price = b_response.json()['products']['REFINED_DIAMOND']['quick_status']['buyPrice']
                de_profit = de_s_price - (e_iron_block_b_price+(3*e_redstone_block_b_price)+gp_b_price+(10*treasurite_b_price)+r_diamond_b_price)
                cast.de_profit = round(de_profit, 2)
                print(f'Drill engine profit: {de_profit}')

                # Golden plate:
                e_gold_block_b_price = b_response.json()['products']['ENCHANTED_GOLD_BLOCK']['quick_status']['buyPrice']
                gp_s_price = gp_b_price
                gp_profit = gp_s_price - ((e_gold_block_b_price*2)+(gj_b_price*5)+r_diamond_b_price)
                cast.gp_profit = round(gp_profit, 2)
                print(f'Golden plate profit: {gp_profit}')

                # Mithril plate:
                mp_s_price = 0
                i = 0
                while mp_s_price ==0:
                    mp_count = mp_response.json()[i]['count']
                    mp_bin = mp_response.json()[i]['bin']
                    if mp_count == 1 and mp_bin == True:
                        mp_s_price = mp_response.json()[i]['highestBidAmount']
                    else:
                        i = i + 1
                r_mithril_b_price = b_response.json()['products']['REFINED_MITHRIL']['quick_status']['buyPrice']
                r_titanium_b_price = b_response.json()['products']['REFINED_TITANIUM']['quick_status']['buyPrice']
                mp_profit = mp_s_price - ((r_mithril_b_price*5)+gp_b_price+e_iron_block_b_price+r_titanium_b_price)
                cast.mp_profit = round(mp_profit, 2)
                print(f'Mithril plate profit: {mp_profit}')

                # Gemstone mixture:
                fn_j_b_price = b_response.json()['products']['FINE_JADE_GEM']['quick_status']['buyPrice']
                fn_amb_b_price = b_response.json()['products']['FINE_AMBER_GEM']['quick_status']['buyPrice']
                fn_ame_b_price = b_response.json()['products']['FINE_AMETHYST_GEM']['quick_status']['buyPrice']
                fn_s_b_price = b_response.json()['products']['FINE_SAPPHIRE_GEM']['quick_status']['buyPrice']
                sj_b_price = b_response.json()['products']['SLUDGE_JUICE']['quick_status']['buyPrice']
                gm_s_price = 0
                i = 0
                while gm_s_price ==0:
                    gm_count = gm_response.json()[i]['count']
                    gm_bin = gm_response.json()[i]['bin']
                    if gm_count == 1 and gm_bin == True:
                        gm_s_price = gm_response.json()[i]['highestBidAmount']
                    else:
                        i = i + 1
                gm_profit = gm_s_price - ((4*fn_j_b_price)+(4*fn_amb_b_price)+(4*fn_ame_b_price)+(fn_s_b_price)+(320*sj_b_price))
                cast.gm_profit = round(gm_profit, 2)
                print(f'Gemstone mixture profit: {gm_profit}')

                # Perfect jasper gemstone:
                fl_jas_b_price = b_response.json()['products']['FLAWLESS_JASPER_GEM']['quick_status']['buyPrice']
                p_jas_s_price = b_response.json()['products']['PERFECT_JASPER_GEM']['quick_status']['sellPrice']
                p_jas_profit = p_jas_s_price - (fl_jas_b_price*5)
                cast.p_jas_profit = round(p_jas_profit, 2)
                print(f'Perfect jasper gemstone profit: {p_jas_profit}')

                # Perfect ruby gemstone:
                fl_r_b_price = b_response.json()['products']['FLAWLESS_RUBY_GEM']['quick_status']['buyPrice']
                p_r_s_price = b_response.json()['products']['PERFECT_RUBY_GEM']['quick_status']['sellPrice']
                p_r_profit = p_r_s_price - (fl_r_b_price*5)
                cast.p_r_profit = round(p_r_profit, 2)
                print(f'Perfect ruby gemstone profit: {p_r_profit}')

                # Perfect jade gemstone:
                fl_jad_b_price = b_response.json()['products']['FLAWLESS_JADE_GEM']['quick_status']['buyPrice']
                p_jad_s_price = b_response.json()['products']['PERFECT_JADE_GEM']['quick_status']['sellPrice']
                p_jad_profit = p_jad_s_price - (fl_jad_b_price*5)
                cast.p_jad_profit = round(p_jad_profit, 2)
                print(f'Perfect jade gemstone profit: {p_jad_profit}')

                # Perfect sapphire gemstone:
                fl_s_b_price = b_response.json()['products']['FLAWLESS_SAPPHIRE_GEM']['quick_status']['buyPrice']
                p_s_s_price = b_response.json()['products']['PERFECT_SAPPHIRE_GEM']['quick_status']['sellPrice']
                p_s_profit = p_s_s_price - (fl_s_b_price*5)
                cast.p_s_profit = round(p_s_profit, 2)
                print(f'Perfect sapphire gemstone profit: {p_s_profit}')

                # Perfect amber gemstone:
                fl_amb_b_price = b_response.json()['products']['FLAWLESS_AMBER_GEM']['quick_status']['buyPrice']
                p_amb_s_price = b_response.json()['products']['PERFECT_AMBER_GEM']['quick_status']['sellPrice']
                p_amb_profit = p_amb_s_price - (fl_amb_b_price*5)
                cast.p_amb_profit = round(p_amb_profit, 2)
                print(f'Perfect amber gemstone profit: {p_amb_profit}')

                # Perfect topaz gemstone:
                fl_t_b_price = b_response.json()['products']['FLAWLESS_TOPAZ_GEM']['quick_status']['buyPrice']
                p_t_s_price = b_response.json()['products']['PERFECT_TOPAZ_GEM']['quick_status']['sellPrice']
                p_t_profit = p_t_s_price - (fl_t_b_price*5)
                cast.p_t_profit = round(p_t_profit, 2)
                print(f'Perfect topaz gemstone profit: {p_t_profit}')

                # Perfect amethyst gemstone:
                fl_ame_b_price = b_response.json()['products']['FLAWLESS_AMETHYST_GEM']['quick_status']['buyPrice']
                p_ame_s_price = b_response.json()['products']['PERFECT_AMETHYST_GEM']['quick_status']['sellPrice']
                p_ame_profit = p_ame_s_price - (fl_ame_b_price*5)
                cast.p_ame_profit = round(p_ame_profit, 2)
                print(f'Perfect amethyst gemstone profit: {p_ame_profit}')

                # Perfect opal gemstone:
                fl_o_b_price = b_response.json()['products']['FLAWLESS_OPAL_GEM']['quick_status']['buyPrice']
                p_o_s_price = b_response.json()['products']['PERFECT_OPAL_GEM']['quick_status']['sellPrice']
                p_o_profit = p_o_s_price - (fl_o_b_price*5)
                cast.p_o_profit = round(p_o_profit, 2)
                print(f'Perfect opal gemstone profit: {p_o_profit}')

                print("Calculations done!")

            cast()
            
            posibilidades = [cast.r_diamond_profit, cast.r_mithril_profit, cast.r_titanium_profit, cast.ft_profit, cast.bh_profit, cast.de_profit, cast.gp_profit, cast.mp_profit, cast.gm_profit, cast.p_jas_profit, cast.p_r_profit, cast.p_jad_profit, cast.p_s_profit, cast.p_amb_profit, cast.p_t_profit, cast.p_ame_profit, cast.p_o_profit]
            def ordenar():
                print("Sorting...")
                values = posibilidades
                values.sort(reverse=True)
                l = len(values)
                first = values[0]
                last = values[l-1]

                while l > 0:
                    values[l - 1] = f"{l} | {values[l- 1]}"
                    l = l-1
                
                l = len(values)
                values[0] = f"(<:stonks_up:1085615477373542440> Best!) {first}"
                values[l-1] = f"(<:not_stonks:1085616374690361395> Worst!) {last}"
                ordenar.values = values
                print(f"Sorted! --> {values}")


            def id_():
                print("Finding id...")
                where = [cast.r_diamond_profit, cast.r_mithril_profit, cast.r_titanium_profit, cast.ft_profit, cast.bh_profit, cast.de_profit, cast.gp_profit, cast.mp_profit, cast.gm_profit, cast.p_jas_profit, cast.p_r_profit, cast.p_jad_profit, cast.p_s_profit, cast.p_amb_profit, cast.p_t_profit, cast.p_ame_profit, cast.p_o_profit]
                a = [cast.r_diamond_profit, cast.r_mithril_profit, cast.r_titanium_profit, cast.ft_profit, cast.bh_profit, cast.de_profit, cast.gp_profit, cast.mp_profit, cast.gm_profit, cast.p_jas_profit, cast.p_r_profit, cast.p_jad_profit, cast.p_s_profit, cast.p_amb_profit, cast.p_t_profit, cast.p_ame_profit, cast.p_o_profit]
                sorted = [cast.r_diamond_profit, cast.r_mithril_profit, cast.r_titanium_profit, cast.ft_profit, cast.bh_profit, cast.de_profit, cast.gp_profit, cast.mp_profit, cast.gm_profit, cast.p_jas_profit, cast.p_r_profit, cast.p_jad_profit, cast.p_s_profit, cast.p_amb_profit, cast.p_t_profit, cast.p_ame_profit, cast.p_o_profit]
                sorted.sort(reverse=True)

                print(f"Where: {where}")
                print(f"Sorted: {sorted}")
                print(f"a: {a}")
                print(f"Values: {ordenar.values}")

                i = 0
                while i < 16:
                    print(i)
                    id = sorted.index(where[i])
                    a[i] = ordenar.values[id]
                    print(ordenar.values[id])
                    i = i+1
                    id_.prices = a
                print(f"Id founded! --> {a}")
                



            ordenar()
            id_()
            # print(f"All --> {ordenar.final_price}")
            embed = discord.Embed(title="Refined ores:", color=discord.Color.blue())
            embed.add_field(name="<:Refined_Diamond:957043148721364993> Refined Diamond (8h):", value=f"{id_.prices[0]} coins", inline= True)
            embed.add_field(name="<:Refined_Mithril:957042346766245888> Refined Mithril (6h):", value=f"{id_.prices[1]} coins", inline= True)
            embed.add_field(name="<:Refined_Titanium:957042821670514780> Refined Titanium (12h):", value=f"{id_.prices[2]} coins", inline= True)
            embed.add_field(name="<:Fuel_Tank:957335067255001258> Fuel Tank (10h):", value=f"{id_.prices[3]} coins", inline= True)
            embed.add_field(name="<:Bejeweled_Handle:960536732669997057> Bejeweled Handle (30min):", value=f"{id_.prices[4]} coins", inline= True)
            embed.add_field(name="<:Drill_Engine:960904703359717406> Drill Engine (1day 6h):", value=f"{id_.prices[5]} coins", inline= True)
            embed.add_field(name="<:Golden_Plate:960909814786052297> Golden Plate (6h):", value=f"{id_.prices[6]} coins", inline= True)
            embed.add_field(name="<:Mithril_Plate:960914302305456219> Mithril Plate (18h):", value=f"{id_.prices[7]} coins", inline= True)
            embed.add_field(name="<:Gemstone_Mixture:960919421965197413> Gemstone Mixture (4h):", value=f"{id_.prices[8]} coins", inline= True)
            embed.add_field(name="<:Perfect_Jasper:960926853391081472> Perfect Jasper Gemstone (20h):", value=f"{id_.prices[9]} coins", inline= True)
            embed.add_field(name="<:Perfect_Ruby:960926853374296074> Perfect Ruby Gemstone (20h):", value=f"{id_.prices[10]} coins", inline= True)
            embed.add_field(name="<:Perfect_Jade:960926853399457822> Perfect Jade Gemstone (20h):", value=f"{id_.prices[11]} coins", inline= True)
            embed.add_field(name="<:Perfect_Sapphire:960926853047136257> Perfect Sapphire Gemstone (20h):", value=f"{id_.prices[12]} coins", inline= True)
            embed.add_field(name="<:Perfect_Amber:960926853357510707> Perfect Amber Gemstone (20h):", value=f"{id_.prices[13]} coins", inline= True)
            embed.add_field(name="<:Perfect_Topaz:960926853483360268> Perfect Topaz Gemstone (20h):", value=f"{id_.prices[14]} coins", inline= True)
            embed.add_field(name="<:Perfect_Amethyst:960926853592416329> Perfect Amethyst Gemstone (20h):", value=f"{id_.prices[15]} coins", inline= True)
            embed.add_field(name="<:Perfect_Opal:1084907981637963826> Perfect Opal Gemstone (20h):", value=f"{id_.prices[16]} coins", inline= True)
            embed.add_field(name="", value="__**```NOTE: This calculations are done with INSTA BUY/SELL prices, the profit will be higher if you do sell/buy orders so don't worry.\nIf the profit is negative it may be it, try checking it later.```**__", inline=False)
            embed.set_footer(text=f"Made by ElGeroIngles 🔹 {config.VERSION}", icon_url="https://cdn.discordapp.com/avatars/715149020883976252/4f1ef6d5b23a9ccadbf72c86bedad68a.webp?size=80")
            await interaction.response.send_message(embed=embed)
            print('Finished')






        else:
            if options.value == 2:
                print('Selected Item Casting')
                embed = discord.Embed(title="Item casting:", color=discord.Color.blue())
                embed.add_field(name="", value="This feature will be added in a later version of this bot! (probably never)")
                embed.set_footer(text=f"Made by ElGeroIngles 🔹 {config.VERSION}", icon_url="https://cdn.discordapp.com/avatars/715149020883976252/4f1ef6d5b23a9ccadbf72c86bedad68a.webp?size=80")
                await interaction.response.send_message(embed=embed)
                print('Finished')
            else:
                print('Error')
                embed = discord.Embed(title="Error", color=discord.Color.red())
                embed.add_field(name="", value="An error ocurred, please try again in a few minutes.")
                embed.set_footer(text=f"Made by ElGeroIngles 🔹 {config.VERSION}", icon_url="https://cdn.discordapp.com/avatars/715149020883976252/4f1ef6d5b23a9ccadbf72c86bedad68a.webp?size=80")
                await interaction.response.send_message(embed=embed)
                print('Finished')


async def setup(bot):
    await bot.add_cog(Forge(bot))
