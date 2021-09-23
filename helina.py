import discord, os
from discord import FFmpegPCMAudio
from discord.errors import ClientException
from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError, CommandNotFound
from lib import libhelina as lbh
from embedder import embeds

arrows_emojis = ['⬆️', '⬇️', '➡️', '⬅️']
num_emojis = ['0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']

idscontainer, datacontainer = {}, {}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
bot = commands.Bot(command_prefix="..")
bot.remove_command('help')

@bot.event
async def on_ready():
    print('bot is online.')

@bot.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    if not user.bot and message.author == bot.user:
        await message.remove_reaction(str(reaction), user)
        limit = int(message.embeds[0].footer.text)
        channel = message.channel
        starter_channel = user.voice.channel
        guild = message.guild
        reaction = str(reaction)
        if starter_channel == None:
            await channel.send("Please connect to a voice channel before using command.")
            return

        if reaction in arrows_emojis[:2]:
            if reaction == arrows_emojis[0]:limit -= 5
            if reaction == arrows_emojis[1]:limit += 5
            if limit < 5:limit = 5
            data, ids = lbh.getChannels()
            datacontainer[channel.id] = data
            idscontainer[channel.id] = ids
            embed = embeds.embedder(data, limit)
            await message.edit(embed=embed)
            return

        if reaction in num_emojis:
            await message.remove_reaction(arrows_emojis[0], bot.user)
            for i in range(len(num_emojis)-1):
                await message.remove_reaction(num_emojis[i+1], bot.user)
            await message.remove_reaction(arrows_emojis[1], bot.user)
            indx = num_emojis.index(reaction)
            data, ids = lbh.getChannels()
            datacontainer[channel.id] = data
            idscontainer[channel.id] = ids
            embed = embeds.embedder2(data, indx-1)
            await message.edit(embed=embed)
            stationid = ids[indx-1]
            await message.add_reaction(arrows_emojis[3])
            await message.add_reaction("🛑")
            await message.add_reaction(arrows_emojis[2])
        
        if reaction in (arrows_emojis[3], arrows_emojis[2]):
            if reaction == arrows_emojis[3]: stationIndex = limit-1
            if reaction == arrows_emojis[2]: stationIndex = limit+1
            if stationIndex < 1: stationIndex = 1
            ids = idscontainer[channel.id]
            data = datacontainer[channel.id]
            stationid = idscontainer[channel.id][stationIndex-1]
            embed = embeds.embedder2(data, stationIndex-1)
            await message.edit(embed=embed)

        try:
            vc = await starter_channel.connect()
        except ClientException:
            vc = discord.utils.get(bot.voice_clients, guild=guild)
            vc.stop()

        if reaction == "🛑" and vc.is_connected():
            await vc.disconnect()
            return
        
        if not vc.is_playing():
            URL = lbh.getListenUrl(stationid)
            vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('`Unknown command` \n Please use right command to operate. `help` for commands details.')
    if isinstance(error, CommandInvokeError):return

@bot.command(aliases=['hlp', 'h'])
async def help(ctx):
    await ctx.send("Prefix = rj help\n**play**: To start the radio")

@bot.command(aliases=['inv', 'invit'])
async def invite(ctx):
    await ctx.send(embed=embeds.invite_embed())

@bot.command(aliases=['jn'])
async def join(ctx):
    link='https://discord.gg/PyzaTzs2cF'
    await ctx.send('Join cricbot development server for any help or feedback/bug report.'+link)

@bot.command(aliases=['source', 'source-code'])
async def code(ctx):
    await ctx.send(embed=embeds.source_embed())

@bot.command(aliases=['credit', 'cred', 'creds'])
async def credits(ctx):
    embed = discord.Embed(title="Helina : Hindi Radio for discord", color=0x03f8fc)
    embed.add_field(name='API Disclaim: ', value="This API is owned by radio garden. It is an unofficial use of this API which is not public.", inline=False)    
    embed.add_field(name='Developed by:', value='0x0is1', inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['radio', 'rd', 'rdo', 'listen'])
async def play(ctx, limit=5):
    channel_id = ctx.message.channel.id
    data, ids = lbh.getChannels()
    embed = embeds.embedder(data, limit)
    datacontainer[channel_id] = data
    idscontainer[channel_id] = ids
    message = await ctx.send(embed=embed)
    await message.add_reaction(arrows_emojis[0])
    for i in range(len(num_emojis)-1):
        await message.add_reaction(num_emojis[i+1])
    await message.add_reaction(arrows_emojis[1])

auth_token = os.environ.get('BOT_TOKEN')
bot.run(auth_token)
