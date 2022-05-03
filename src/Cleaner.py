import os

from colorama import Fore
from pyfade import Fade, Colors
from dotenv import load_dotenv
from discord.ext import commands

os.system("cls")
load_dotenv(dotenv_path=f"{os.path.dirname(__file__)}\\config\\token.env")
CLIENT = commands.Bot(command_prefix = '.', self_bot = True)

@CLIENT.event
async def on_ready():
    print(Fade.Horizontal(Colors.green_to_white,
    """
 ╔═╗╦  ╔═╗╔═╗╔╗╔╔═╗╦═╗
║  ║  ║╣ ╠═╣║║║║╣ ╠╦╝
╚═╝╩═╝╚═╝╩ ╩╝╚╝╚═╝╩╚═
    """))

@CLIENT.command()
async def clear(ctx, limit: int):
    removed = 0

    async for msg in ctx.message.channel.history(limit = limit):
        if msg.author.id == CLIENT.user.id:
            try:
                await msg.delete()
                removed += 1
            except:
                pass
    print(f"[{Fore.GREEN}!{Fore.RESET}] Removed {removed} messages. Now waiting.")

CLIENT.run(os.getenv("TOKEN"), bot = False)