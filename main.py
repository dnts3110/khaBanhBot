import discord
import random

TOKEN = 'ODYzMDAxMzU2NzYzNzkxMzgw.YOgipQ.lOJQjzB81HYqcrSGnmId3E6ys54'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#the input is every msg in the server
#func to react/respond to every msg in the server
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'generals': #allow to respond only in the general channel in the server
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'ai la nguoi dut nhat trong nay?' or user_message.lower() == 'ai là người đụt nhất trong này?' :
            randomNo = random.randrange()
            await message.channel.send(f'Chac chan la {username}')
            return
        elif user_message.lower() == 'xin so danh de anh banh oi' or user_message.lower() == 'xin số đánh đề anh bảnh ơi' or user_message.lower() == 'xin so danh de banh oi' or user_message.lower() == 'xin số đánh đề bảnh ơi':
            response = f'Em zai tin anh danh con de nay di {random.randint(10,99)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == 'buong' or user_message.lower() == 'bướng':
            await message.channel.send(f'Buong cc ah dmm {username}!')
            return
        elif user_message.lower() == 'cam on banh' or user_message.lower() == 'cảm ơn bảnh':
            await message.channel.send(f'Khong co gi nhe em zai {username}!')
            return
        elif user_message.lower() == 'cam on banh' or user_message.lower() == 'cảm ơn bảnh':
            await message.channel.send(f'Khong co gi nhe em zai {username}!')
            return

    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be use everywhere')




client.run(TOKEN)