import discord
import youtube_dl
import pafy
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get


players = {}


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.songs = {}
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('... Added Music Cog ...')
    
    @commands.command(pass_context=True)
    async def join(self, ctx):
        """Joins the users channel"""
        try:
            channel = ctx.message.author.voice.channel
            voice = get(self.bot.voice_clients, guild=ctx.guild)
            if voice and voice.is_connected():
                await voice.move_to(channel)
                await ctx.send("Moved channel")
            else:
                voice = await channel.connect()
                await ctx.send("Joined channel")
        except:
            await ctx.send("You are not connected to a channel")
        
    
    @commands.command()
    async def leave(self, ctx):
        """Leaves the user channel"""
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await ctx.send("Disconnecting from channel")
            await voice.disconnect()
        else:
            await ctx.send("")
    
    @commands.command()
    async def play(self, ctx, url: str):
        # video = pafy.new(url)
        # #self.songs[video.title] = video
        # audio = video.getbestaudio()
        # audio.download(filepath="audio")
        
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('Eli Noir - Real (Lyrics) [CC].webm')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

        
        await ctx.send("Playing song")

        # voice = get(self.bot.voice_clients, guild=ctx.guild)
        # voice.play(url)
        # guild = ctx.message.guild
        # voice_client = guild.voice_client
        # player = await voice_client.create_ytdl_player(url)
        # players[server.id] = player
        # player.start()

def setup(bot):
    bot.add_cog(Music(bot))