import disnake
from disnake.ext import commands

from utils.color import color

class On_guild_join(commands.Cog):
      def __init__(self, bot: commands.Bot):
         self.bot = bot
         
      @commands.Cog.listener() 
      async def on_guild_join(self):
         ...
                        