import discord

def embedder(data, limit, rtype, mtype, query):
    embed = discord.Embed(title="Stations list", color=0x552E12)
    embed.set_author(name="Radio Garden", icon_url = "http://radio.garden/icons/favicon.png")
    for j, i in enumerate(data[:limit][-5:]):
        embed.add_field(name=f"{j+1}. {i[0]}", value=f"{i[1]}, {i[2]}", inline=False)
    embed.set_footer(text=f"{limit}-{rtype}-{mtype}-{query}")
    return embed

def embedder2(data, index, rtype, mtype, query):
    embed = discord.Embed(title="Now Playing", color=0x552E12)
    embed.set_author(name="Radio Garden", icon_url = "http://radio.garden/icons/favicon.png")
    embed.add_field(name=data[index][0], value=f"{data[index][1]}, {data[index][2]}")
    embed.set_footer(text=f"{index+1}-{rtype}-{mtype}-{query}")
    return embed

def embedder3(data, limit, rtype):
    embed = discord.Embed(title="Stations list", color=0x552E12)
    embed.set_author(name="Live365", icon_url = "https://pbs.twimg.com/profile_images/479057267082272768/4DCnmXxO.jpeg")
    for j, i in enumerate(data[:limit][-5:]):
        embed.add_field(name=f"{j+1}. {i[0]}", value=f"Genre: {i[3]}", inline=False)
    embed.set_footer(text=f"{limit}-{rtype}")
    return embed

def embedder4(data, index, rtype):
    embed = discord.Embed(title="Now Playing", color=0x552E12)
    embed.set_thumbnail(url=data[index][2])
    embed.set_author(name="Live365", icon_url = "https://pbs.twimg.com/profile_images/479057267082272768/4DCnmXxO.jpeg")
    embed.add_field(name=data[index][0], value=f"{data[index][3]}")
    embed.set_footer(text=f"{index+1}-{rtype}")
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
