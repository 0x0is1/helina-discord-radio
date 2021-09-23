import discord

def embedder(data, limit):
    embed = discord.Embed(title="Stations list", color=0x552E12)
    embed.set_author(name="Radio Garden", icon_url = "http://radio.garden/icons/favicon.png")
    for j, i in enumerate(data[:limit][-5:]):
        embed.add_field(name=f"{j+1}. {i[0]}", value=f"{i[1]}, {i[2]}", inline=False)
    embed.set_footer(text=limit)
    return embed

def embedder2(data, index):
    embed = discord.Embed(title="Now Playing", color=0x552E12)
    embed.set_author(name="Radio Garden", icon_url = "http://radio.garden/icons/favicon.png")
    embed.add_field(name=data[index][0], value=f"{data[index][1]}, {data[index][2]}")
    embed.set_footer(text=index+1)
    return embed

def invite_embed():
    embed = discord.Embed(title="Helina Radio Invite",
            url="https://discord.com/api/oauth2/authorize?client_id=890577942843883561&permissions=10304&scope=bot",
            description="Invite Helina to your server.", color=0x03f8fc)
    return embed

def source_embed():
    source_code = "https://github.com/0x0is1/helina-discord-radio"
    embed = discord.Embed(title="Helina Source code",
            url=source_code,
            description="Visit Helina source code.", color=0x03f8fc)
    return embed
