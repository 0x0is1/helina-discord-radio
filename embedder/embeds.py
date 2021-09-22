import discord

def embedder(data, limit):
    embed = discord.Embed(title="Stations list")
    for j, i in enumerate(data):
        embed.add_field(name=f"{j+1}. {i[0]}", value=f"{i[1]}, {i[2]}")
    embed.set_footer(text=limit)
    return embed

def embedder2(data, index):
    print(data)
    embed = discord.Embed(title="Now Playing")
    embed.add_field(name=data[index][0], value=f"{data[index][1]}, {data[index][2]}")
    embed.set_footer(text=index)
    return embed