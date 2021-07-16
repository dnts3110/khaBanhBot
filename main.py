import discord
import random

TOKEN = 'ODYzMDAxMzU2NzYzNzkxMzgw.YOgipQ.r6lzgVupo60bZwapN7hUV1cQ-BQ'

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# the input is every msg in the server
# func to react/respond to every msg in the server
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name != 'gener':  # allow to respond only in the general channel in the server
        if user_message.lower() == 'hello':
            await message.channel.send(f" Anh Bảnh chào em Zai {username}!")
            return
        elif user_message.lower() == 'ai la nguoi dut nhat trong nay?' or user_message.lower() == 'ai là người đụt nhất trong này?':

            await message.channel.send(f' Chắc chắn là {username}')
            return
        elif user_message.lower() == 'xin so danh de anh banh oi' or user_message.lower() == 'xin số đánh đề anh bảnh ơi' or user_message.lower() == 'xin so danh de banh oi' or user_message.lower() == 'xin số đánh đề bảnh ơi':
            response = f'Em zai tin anh đánh con đề này đi {random.randint(10, 99)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == 'buong' or user_message.lower() == 'bướng':
            await message.channel.send(f'Bướng cc à đmm {username}!')
            return
        elif user_message.lower() == 'cam on banh' or user_message.lower() == 'cảm ơn bảnh':
            await message.channel.send(f'Không có gì nhé em zai {username}!')
            return
        elif user_message.lower() == "nau an di banh" or user_message.lower() == 'nấu ăn đi bảnh':
            await message.channel.send(file=discord.File('cook.gif'))
            return

    chuibay = ["Xoắn ai chứ đừng xoắn tao. Đã là chó ngao thì đừng quá tự cao :’)",
               "Bố mày ỉa vào mồm mày bây giờ dcmm", "Mặt thì mụn mà tưởng là kim cương, Chân thì đầy ghẻ mà tưởng là "
                                                     "hột xoàn, Coi lại bản thân mình đi nha em zai",
               "Tao biết sống là phải tàn ác, Và phải cảnh giác với những con chó như tụi mày",
               "Bố mài chửi chúng mài 1 câu gọn nhẹ thôi nhớ \n Địt con mẹ, địt cả lò cả họ cả xóm nhà chúng mài ra chứ ngồi đấy làm chi mà rách việc.Bố đã đéo thích nói đến thì thôi, chúng mày lại còn chu cái mỏ như cái mỏ lồn vào làm gì, thích thì phắn mẹ chúng mày hết đi, không bố lại xua con chó cái nhà bố ra cho chúng mày bú lồn thì có mà ngộ độc thực phẩm cả lũ, cả nút đấy nhá..hãm vcl.",
               "Đĩ mẹ mày, bố mày ra tù thì bố mày đập bỏ mẹ mày ;)", "Chửi cái đầu buồi à??? Tao làm gì mày",
               f"May cho em {username} là anh vẫn đang ngồi tù nhé ;))",
               "Sủa nửa đi dcmm con chó", "Dm thằng chưa mọc lông cu",
               "Tiền rách rán lại vẫn có giá trị, \n Nhân cách thối nát có xịt nước hoa vẫn nặng mùi. \n Sống làm sao "
               "cko.người ta nể. \n Chứ đừng để người ta khinh. ;)",
               "Mồm cứt, dcmm cả làng ơi có thằng bé mồm dính đầy cứt vừa lên tiếng nè",
               "Bố mẹ dạy mày để cứt vào mồm à? Sao toàn sủa ra cứt thế hả thằng chó", "Em zai đợi bố mày ra tù đi <3",
               "Tao là bố mày đấy, dcmm", "Mày ăn cơm hay ăn cứt mà ngu thế?",
               "Tạo hoá thật keo kiệt với bộ não của em zai ;)", "Khổ thân em zai, sinh ra đã đéo có não :(",
               f"Nhìn {username} cũng giống búp bê đó. \n Nhưng búp bê hình như không não mà chỉ toàn nhựa. \n Mà nhựa cuối cùng cũng chỉ ra bãi đồng nát mà thôi.", f"Dạ em xin lỗi {username} ạ, em còn trẻ người non dạ mong {username} thông cảm ạ", f"Người ta bảo nghĩ gì thì uốn lưỡi 7 lần trước khi nói, riêng mày, {username}, lưỡi chó nói đéo khác sủa gâu gâu", f"Tổ sư bố thằng {username}, mịe mày lễ phép mày đâu? Dcmm thằng ăn bốc đái ngồi", f"Này, chửi cái đéo gì?? Mày có quyền gì chửi tao, giỏi thì oẳn tù tì thắng tao đi ;). \n Đấm, kéo, lá. Mày ra trước"]
    randNum = random.randrange(0, len(chuibay))
    strings = user_message.lower()
    words = ['dcm', 'đcm', 'con', 'dm', 'dmm', 'dit', 'me', 'ma', 'du', 'đm', 'đmm', 'địt', 'mẹ', 'má', 'đụ', 'banh',
             'bảnh']
    stringlist = strings.split()
    word1, word2, word3, word4, word5, word6, word7, word8, word9, word10, word11, word12, word13, word14, word15, word16, word17 = words
    # if (word1 in stringlist and word3 in stringlist) or (word2 in stringlist and word3 in stringlist):
    if (
            word1 in stringlist or word2 in stringlist or word3 in stringlist or word4 in stringlist or word5 in stringlist or word6 in stringlist or word7 in stringlist or word8 in stringlist or word9 in stringlist or word10 in stringlist or word11 in stringlist or word12 in stringlist or word13 in stringlist or word14 in stringlist or word15 in stringlist) and (
            word16 in stringlist or word17 in stringlist):
        print(True)
        await message.channel.send((chuibay[randNum]))
        randNum = random.randrange(0, len(chuibay))  # make the number random again
        return

    dieunhay = random.randrange(1, 6)
    if user_message.lower() == "nhay di banh" or user_message.lower() == 'nhảy đi bảnh' or user_message.lower() == 'múa đi bảnh' or user_message.lower() == 'mua di banh':
        print('true nhay')
        if dieunhay == 1:
            await message.channel.send(file=discord.File('dance1.gif'))
            dieunhay = random.randrange(1, 6)
            return
        if dieunhay == 2:
            await message.channel.send(file=discord.File('dance2.gif'))
            dieunhay = random.randrange(1, 6)
            return
        if dieunhay == 3:
            await message.channel.send(file=discord.File('dance3.gif'))
            dieunhay = random.randrange(1, 6)
            return
        if dieunhay == 4:
            await message.channel.send(file=discord.File('dance4.gif'))
            dieunhay = random.randrange(1, 6)
            return
        if dieunhay == 5:
            await message.channel.send(
                f'Nhảy nhảy múa múa cái địt con bà già mày à {username} ??! Địt mịe mày bố mày ngồi tù gọt khoai tây trầm cảm vãi loz bảo bố mày nhảy cái đầu buồi. Đợi bố mày 9 năm nữa ra khỏi tù rồi bố mày nhảy địt mẹ mày ;)')
            dieunhay = random.randrange(1, 6)
            return

    if user_message.lower() == "dam" or user_message.lower() == 'đấm':
        await message.channel.send("Lá \n tao thắng")
        return
    if user_message.lower() == "keo" or user_message.lower() == 'kéo':
        await message.channel.send("Đấm \n tao thắng")
        return
    if user_message.lower() == "la" or user_message.lower() == 'lá':
        await message.channel.send("Kéo \n tao thắng")
        return


client.run(TOKEN)
