import discord
from discord.ext import commands
import random
import datetime

description = 'A pug bot for Overwatch Israel.'
bot = commands.Bot(command_prefix='!', description=description)

token = 'NTQyMDM0ODY1NDIwNTAxMDM1.DzoRcA.'

client = discord.client



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='twitch.tv/ow_il'))
    print('Fired up!')


@bot.command()
async def pug(ctx):
    Main_DPS = discord.utils.get(ctx.guild.roles, name="DPS")
    DPS = discord.utils.get(ctx.guild.roles, name="Secondary - DPS")
    Tank = discord.utils.get(ctx.guild.roles, name="Secondary - Tank")
    Main_Tank = discord.utils.get(ctx.guild.roles, name="Tank")
    Main_Support = discord.utils.get(ctx.guild.roles, name="Support")
    Support = discord.utils.get(ctx.guild.roles, name="Secondary - Support")
    Pug_Runner = discord.utils.get(ctx.guild.roles, name="PUG Runner")

    list_of_forced_players = []
    number_of_forced_players = int
    voice_channel = discord.utils.get(ctx.guild.channels, id=547108815435464717)
    team_1_vc = discord.utils.get(ctx.guild.channels, id=505023650202648577)
    team_2_vc = discord.utils.get(ctx.guild.channels, id=505023848425455616)
    member_list = voice_channel.members
    choice1 = discord.Member
    choice2 = discord.Member
    choice3 = discord.Member
    choice4 = discord.Member
    choices = [choice1, choice2, choice3, choice4]
    async def role_arragement(list_of_roles, list_of_members_role, role_str, team_1_role, team_2_role):

        index = 0
        for i in choices:
            if index < 3:
                team_role = team_1_role
                team_vc = team_1_vc
                team_num = 1
            else:
                team_role = team_2_role
                team_vc = team_2_vc
                team_num = 2
            i = random.choice(list_of_roles)
            team_role = team_role + [i.mention]

            await i.send("You're playing " + role_str + " for Team " + str(team_num) + ", at the PUG that took place in: ")
            await i.send(datetime.datetime.now())
            await i.move_to(team_vc)
            list_of_roles.remove(i)
            list_of_members_role.remove(i)
            index = index + 1

    if len(member_list) < 12:
        # what to do if there are less then 12 people in the vc
        await ctx.send('Not Enough Members to start a PUG')

    while len(member_list) > 12:
        # what to do if there are more then 12 people in the vc - the force players system
        choice = random.choice(member_list)
        if choice not in list_of_forced_players:
            list_of_forced_players = list_of_forced_players + [choice.mention]
            member_list.remove(choice)

    if len(member_list) == 12:
        # if there are only 12 people - no forced players
        if Pug_Runner in ctx.author.roles:

            list_of_supports = []
            team_1_supports = []
            team_2_supports = []

            for member in member_list:
                if Main_Support in member.roles:
                    list_of_supports = list_of_supports + [member]

            if len(list_of_supports) < 4:  # what to do if there are less then 4 maintanks
                for member in member_list:
                    if Support in member.roles:
                        list_of_supports = list_of_supports + [member]

                if len(list_of_supports) == 4:
                    role_arragement(list_of_supports, member_list, "SUPPORT", team_1_supports, team_2_supports)
                while len(list_of_supports) > 4:
                    choice1 = random.choice(list_of_supports)
                    if Support in choice1.roles:
                        print(choice1)
                        list_of_supports.remove(choice1)

            while len(list_of_supports) >= 5:
                choice1 = random.choice(list_of_supports)
                print(choice1)
                list_of_supports.remove(choice1)

            if len(list_of_supports) == 4:
                role_arragement(list_of_supports, member_list, "SUPPORT", team_1_supports, team_2_supports)


            # -----------------------------------------------------#
            # -----------------------tanks-------------------------#
            list_of_tanks = []
            list_of_members_tank = member_list
            team_1_tanks = []
            team_2_tanks = []

            for member in member_list:
                if Main_Tank in member.roles:
                    list_of_tanks = list_of_tanks + [member]
            if len(list_of_tanks) < 4:  # what to do if there are less then 4 maintanks
                for member in member_list:
                    if Tank in member.roles:
                        list_of_tanks = list_of_tanks + [member]
                if len(list_of_tanks) == 4:
                    role_arragement(list_of_tanks, list_of_members_tank, "TANL", team_1_tanks, team_2_tanks)
                while len(list_of_tanks) > 4:
                    choice1 = random.choice(list_of_tanks)
                    if Tank in choice1.roles:
                        list_of_tanks.remove(choice1)

            while len(list_of_tanks) > 4:
                choice1 = random.choice(list_of_tanks)
                list_of_tanks.remove(choice1)

            if len(list_of_tanks) == 4:
                role_arragement(list_of_tanks, list_of_members_tank, "TANL", team_1_tanks, team_2_tanks)

            member_list = list_of_members_tank

            # -----------------------------------------------------#
            # -----------------------DPS---------------------------#

            list_of_dps = []
            list_of_members_dps = member_list
            team_1_dps = []
            team_2_dps = []

            for member in member_list:
                if Main_DPS in member.roles:
                    list_of_dps = list_of_dps + [member]

            if len(list_of_dps) < 4:  # what to do if there are less then 4 maintanks
                for member in member_list:
                    if DPS in member.roles:
                        list_of_dps = list_of_dps + [member]

                if len(list_of_dps) < 4:
                    if list_of_members_dps != []:
                        list_of_dps = list_of_members_dps

                if len(list_of_dps) == 4:
                    role_arragement(list_of_dps, list_of_members_dps, "DPS", team_1_dps, team_2_dps)


                while len(list_of_dps) > 4:
                    choice1 = random.choice(list_of_dps)
                    if DPS in choice1.roles:
                        list_of_dps.remove(choice1)

            while len(list_of_dps) > 4:
                choice1 = random.choice(list_of_dps)
                list_of_dps.remove(choice1)

            if len(list_of_dps) < 4:
                if member_list != []:
                    list_of_dps.remove(member_list)
                    list_of_dps = list_of_members_dps

            if len(list_of_dps) == 4:
                role_arragement(list_of_dps, list_of_members_dps, "DPS", team_1_dps, team_2_dps)

            print(member_list)
            await ctx.send('```Team 1:```' + ' ```Supports```' + " " + str(team_1_supports) + '```Tanks```' + '' + str(
                team_1_tanks) + '```DPS```' + '' + str(team_1_dps))
            await ctx.send('```Team 2:```' + ' ```Supports```' + " " + str(team_2_supports) + '```Tanks```' + '' + str(
                team_2_tanks) + '```DPS```' + '' + str(team_2_dps))
            if list_of_forced_players != []:
                await ctx.send('```These members did not play this time, but they will play next time:```')
                await ctx.send(list_of_forced_players)

        else:
            await ctx.send("You're not a PUG Runner.")


@bot.command()
async def clear(ctx):
    team_1_vc = discord.utils.get(ctx.guild.channels, id=505023650202648577)
    team_2_vc = discord.utils.get(ctx.guild.channels, id=505023848425455616)
    voice_channel = discord.utils.get(ctx.guild.channels, id=547108815435464717)
    list_of_members_t1 = team_1_vc.members
    list_of_members_t2 = team_2_vc.members
    list_of_members = list_of_members_t1 + list_of_members_t2
    while len(list_of_members) != 0:
        choice1 = random.choice(list_of_members)
        await choice1.move_to(voice_channel)
        list_of_members.remove(choice1)
    print('all donezo!')


bot.run(token)
