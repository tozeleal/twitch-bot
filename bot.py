import os, pickle

from models.user import User

from pathlib import Path
from random import randint
from twitchio.ext import commands
from datetime import datetime



TOKEN = os.environ['TMI_TOKEN']
CHANNELS = ['tozeleal']
MODERATORS = ['purpellvt', 'milan3d222', 'luigoalma', 'tozeleal']
USERDATAPATH = "userdata.txt"





class Bot(commands.Bot):

    userdata = None

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=TOKEN, prefix='!', initial_channels=CHANNELS)
        userdata_path = Path(USERDATAPATH)
        userdata_path.touch()
        try:
            self.userdata=pickle.load(open(USERDATAPATH,"rb"))
        except EOFError:
            self.userdata = {}

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
        await ctx.send(f"Happy lurking @{ctx.author.name}! I hope you won't be afk for a long time :P")
        
        if self.userdata.get(ctx.author.name, None) is not None:
            self.userdata[ctx.author.name].set_lurktime(time=datetime.now())
        else:
            self.userdata[ctx.author.name] = User(0,datetime.now(),0)

    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command()
    async def unlurk(self, ctx: commands.Context):
        
        user = self.userdata.get(ctx.author.name)
        
        if user.get_lurktime() is None:
            await ctx.send(f"Welcome back @{ctx.author.name}! But you didn't start the lurk command :P ")
            return
        result = datetime.now() - user.get_lurktime()
        user.add_lurk(result)
        self.userdata[ctx.author.name]=user
        await ctx.send(f"Welcome back @{ctx.author.name}! Have been lurking for {int(result.total_seconds()//60)} minutes and {int(result.total_seconds()%60)} seconds.")
        
    

bot = Bot()
bot.run()