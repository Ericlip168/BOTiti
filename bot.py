import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('his dick'))
	print(f'Galing mo talagang kupal ka!')


@client.command()
async def rules(ctx):
	await ctx.send("Wag ka bastos!")
	print (f'rules command has been used in {ctx.guild} by {ctx.author}')
	

@client.command()
async def oi(ctx):
	await ctx.send("Kamusta sa inyo mga kanser!")
	print (f'Oi command has been used by {ctx.guild} by {ctx.author}')


@client.command()
async def kantut(ctx):
	await ctx.send("Oops bawal yan")
	print (f'Kantut command has been used in {ctx.guild} by {ctx.author}')



@client.command()
@commands.has_permissions(manage_messages = True)
async def zahando(ctx, amount=10):
	await ctx.channel.purge(limit = amount)
	print (f'10 messages has been deleted on {ctx.guild} by {ctx.author}')

@client.command()
async def meme(ctx):
	embed = discord.Embed(color = discord.Colour.red())
	random_link = random.choice(memes)
	embed.set_image(url=random_link)
	await ctx.send (embed = embed)
	print (f'Meme command has been used on {ctx.guild} by {ctx.author}')


                                                           #DATABASE  
memes = [
'https://i.redd.it/0udzp4q1ia561.png','https://i.redd.it/xosl2auoyb561.jpg',
'https://i.redd.it/nc8xyamp6b561.jpg','https://i.redd.it/19qvlzan8d561.jpg',
'https://i.redd.it/s6wb3mpu5b561.jpg','https://i.redd.it/858vz0etl8561.jpg',
'https://i.redd.it/y4wfwlu9sb561.jpg','https://i.redd.it/8dfcvbad6d561.jpg',
'https://i.redd.it/0qyrl7uzub561.jpg','https://i.redd.it/xi0a4x0g3d561.jpg',
'https://i.redd.it/6yhaf60vqb561.jpg','https://i.redd.it/54ohrwp189561.jpg',
'https://i.redd.it/7fv7uf0dfc561.jpg','https://i.redd.it/cq2cs647ih561.jpg',
'https://i.redd.it/6hwhqj76kc561.jpg','https://i.redd.it/wtsbiv8crb561.jpg',
'https://i.redd.it/7rkpm72o4c561.png','https://i.redd.it/asapli1anc561.jpg',
'https://i.redd.it/4mnen7kbwb561.png','https://i.redd.it/kxognirh49561.jpg',
'https://i.redd.it/3rdhv7jntb561.jpg','https://i.redd.it/jkv810wwo9561.jpg',
'https://i.redd.it/xa5ffq7jec561.jpg','https://i.redd.it/3svs2z5i2d561.jpg',
'https://i.redd.it/q3jf3hr7p9561.jpg','https://i.redd.it/098kvfy9ig561.jpg',
'https://i.redd.it/mdd3pot5zc561.jpg','https://i.redd.it/i3287zommc561.png',
'https://i.redd.it/54v564t6ua561.jpg','https://i.redd.it/31jid3ot4h561.png',
'https://i.redd.it/0a9e43fl8a561.jpg','https://i.redd.it/dkeozmihbh561.jpg',
'https://i.redd.it/sgs4wsvav9561.jpg','https://i.redd.it/ci16dmmpwa561.jpg',
'https://i.redd.it/yi6q0lfhja561.jpg','https://i.redd.it/cs7l5ue58b561.png',
'https://i.redd.it/2ocfhea7jb561.jpg','https://i.redd.it/div75id72b561.png',
'https://i.redd.it/rtwgwz76wa561.jpg','https://i.redd.it/u0v56v5joa561.jpg',
'https://i.redd.it/ugaqk73nzb561.jpg','https://i.redd.it/mkr2e5kghb561.jpg',
'https://i.redd.it/p6b0ugj7yc561.jpg','https://i.redd.it/kxw2kvjtnc561.png',
'https://i.redd.it/igu7pwanbc561.jpg','https://i.redd.it/46imhkmocc561.jpg',
'https://i.redd.it/0iekr50djb561.jpg','https://i.redd.it/1wvkjz6gzb561.jpg',
'https://i.redd.it/7pglchga9c561.jpg','https://i.redd.it/byli1rhhzb561.jpg',
'https://i.redd.it/zn21tozv7c561.jpg','https://i.redd.it/1u5q4xe9ya561.jpg',
'https://i.redd.it/a5nr91lfbb561.jpg','https://i.redd.it/3u26ue7xed561.jpg',
'https://i.redd.it/lbyv5pxasc561.jpg','https://i.redd.it/hdorh3e4ig561.jpg',
'https://i.redd.it/1brwgz3bdd561.jpg','https://i.redd.it/q8rczpqh6d561.jpg',
'https://i.redd.it/amen0jv3ed561.jpg','https://i.redd.it/0fu3cj0xub561.jpg',
'https://i.redd.it/l8tzmp8mdb561.jpg','https://i.redd.it/5f1cvj2tyf561.jpg',
'https://i.redd.it/mdp3hcuhyc561.jpg','https://i.redd.it/o3vogyfopc561.jpg',
'https://i.redd.it/0bnghtey2d561.png','https://i.redd.it/cj5ktvxfid561.png',
'https://i.redd.it/rnk64yxnmd561.jpg','https://i.redd.it/2ejrg7ws89561.jpg',
'https://i.redd.it/ygd5hlbs1d561.jpg','https://i.redd.it/b5m89ou60d561.jpg',
'https://i.redd.it/jtu2poh3gc561.png','https://i.redd.it/w6pfaigmyc561.jpg',
'https://i.redd.it/or0tnrtwnd561.jpg','https://i.redd.it/0tppoz8x4g561.jpg',
'https://i.redd.it/x5rrjr36ud561.jpg','https://i.redd.it/4az9xvakad561.jpg',
'https://i.redd.it/kp8pu1ul9c561.jpg','https://i.redd.it/cnq73jy9jd561.jpg',
'https://i.redd.it/ybvp6iv2jd561.jpg','https://i.redd.it/adduiwsymc561.jpg',
'https://i.redd.it/a4dwrsgdxc561.jpg','https://i.redd.it/3oyqp4oivd561.jpg',
'https://i.redd.it/7dnegbydvd561.jpg','https://i.redd.it/9tndk216ob561.jpg',
'https://i.redd.it/cc4io3mvud561.jpg','https://i.redd.it/88lonvd2rb561.jpg',
'https://i.redd.it/a6v1lpcqvd561.jpg','https://i.redd.it/2diokxw1gd561.jpg',
'https://i.redd.it/ywd80olhzd561.png','https://i.redd.it/t6yuusy8sd561.png',
'https://i.redd.it/sqb6fcqzwd561.jpg','https://i.redd.it/txrq54gvqd561.jpg',
'https://i.redd.it/0zxrlslwd8561.png','https://i.redd.it/479idkmxyd561.jpg',
'https://i.redd.it/71j1snm2td561.png','https://i.redd.it/rv72jk0gtd561.jpg',
'https://i.redd.it/641w531jxd561.jpg','https://i.redd.it/ma13ebfm1e561.jpg',
'https://i.redd.it/o6h801isnd561.jpg','https://i.redd.it/iou1in9zzb561.jpg',
'https://i.redd.it/khva2v5akb561.jpg','https://i.redd.it/jn5qn3xz2e561.jpg',
]



client.run("Nzg2ODY5NTU0MTUyMjEwNDUy.X9MrYQ.A1wMRd3oL4vYUDvOZ0NCInJiQ6Q")

