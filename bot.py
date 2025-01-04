import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("$"),
    intents=intents,
)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('pong (this is a table tennis reference)')

@bot.command()
async def add(ctx: commands.Context, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(str(left + right))


@bot.command()
async def roll(ctx: commands.Context, dice: str):
    """Rolls a die in NdN format."""
    try:
        rolls, limit = map(int, dice.split("d"))
    except ValueError:
        await ctx.send("Format has to be in NdN!")
        return

    # _ is used in the generation of our result as we don't need the number that comes from the usage of range(rolls).
    result = ", ".join(str(random.randint(1, limit)) for _ in range(rolls))
    await ctx.send(result)


@bot.command(description="For when you wanna settle the score some other way")
async def choose(ctx: commands.Context, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx: commands.Context, times: int, *, content: str = "repeating..."):
    """Repeats a message multiple times."""
    for _ in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx: commands.Context, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f"{member.name} joined in {member.joined_at}")

@bot.slash_command(guild_ids=[1287375183556116531])
async def utty(ctx):
    await ctx.respond("for the U.T.T.Y.!!!")

bot.run('')
