import os 
from twitchio.ext import commands
from random import randint

TOKEN = os.environ['TMI_TOKEN']
CHANNELS = ['tozeleal']
MODERATORS = ['purpellvt', 'milan3d222', 'luigoalma', 'tozeleal']



class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=TOKEN, prefix='rpg:', initial_channels=CHANNELS)

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        
    
    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def d20(self, ctx: commands.Context):
        #Throws a D20 dice
        await ctx.send(f'You got {randint(1,20)}, {ctx.author.name}!')
    
    @commands.command()
    async def d6(self, ctx: commands.Context):
        #Throws a D20 dice
        await ctx.send(f'You got {randint(1,6)}, @{ctx.author.name}!')

    @commands.command()
    async def start(self, ctx: commands.Context):
        #Starts RPG campain

        await ctx.send(f'EMPTY')

    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command()
    async def test(self, ctx: commands.Context):
        #Starts RPG campain

        print(ctx.author.name in MODERATORS)
    
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command()
    async def lurk(self, ctx: commands.Context):
        #Starts RPG campain
        await ctx.send(f"Happy lurking @{ctx.author.name}! I hope you won't be afk for a long time :P")

        

    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    async def event_command_error(self, context: commands.Context, error: Exception):
        print(error)
    

bot = Bot()
bot.run()