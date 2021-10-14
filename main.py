import discord
from discord.ext import commands #music
import random
import asyncio

import music #music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

TOKEN = 'ODYzMDAxMzU2NzYzNzkxMzgw.YOgipQ.r6lzgVupo60bZwapN7hUV1cQ-BQ'





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

    if message.channel.name != 'genera':  # allow to respond only in the general channel in the server
        if user_message.lower() == 'hello banh':
            await message.channel.send(f" Anh Bảnh chào em {username}!")
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
               f"Nhìn {username} cũng giống búp bê đó. \n Nhưng búp bê hình như không não mà chỉ toàn nhựa. \n Mà nhựa cuối cùng cũng chỉ ra bãi đồng nát mà thôi.",
               f"Dạ em xin lỗi {username} ạ, em còn trẻ người non dạ mong {username} thông cảm ạ",
               f"Người ta bảo nghĩ gì thì uốn lưỡi 7 lần trước khi nói, riêng mày, {username}, lưỡi chó nói đéo khác sủa gâu gâu",
               f"Tổ sư bố thằng {username}, mịe mày lễ phép mày đâu? Dcmm thằng ăn bốc đéo ăn đũa",
               f"Ngô Bá Khá từ lúc lọt từ lồn ra đến nay, mới được tận mắt thấy một thanh niên mặc váy đái ngồi, "
               f"mồm ngậm cứt {username}", "Vãi cả lồn bây giờ chó còn biết gõ bàn phím sủa gâu gâu"]
    randNum = random.randrange(0, len(chuibay))
    strings = user_message.lower()
    words = ['dcm', 'đcm', 'con', 'dm', 'dmm', 'dit', 'me', 'ma', 'du', 'đm', 'đmm', 'địt', 'mẹ', 'má', 'đụ', 'long',
             'lon', 'lông', 'lồn', 'dcmm', 'đcm', 'banh',
             'bảnh']
    stringlist = strings.split()
    word1, word2, word3, word4, word5, word6, word7, word8, word9, word10, word11, word12, word13, word14, word15, word16, word17, word18, word19, word20, word21, word22, word23 = words
    # if (word1 in stringlist and word3 in stringlist) or (word2 in stringlist and word3 in stringlist):
    if (
            word1 in stringlist or word2 in stringlist or word3 in stringlist or word4 in stringlist or word5 in stringlist or word6 in stringlist or word7 in stringlist or word8 in stringlist or word9 in stringlist or word10 in stringlist or word11 in stringlist or word12 in stringlist or word13 in stringlist or word14 in stringlist or word15 in stringlist or word16 in stringlist or word17 in stringlist or word18 in stringlist or word19 in stringlist or word20 in stringlist or word21 in stringlist) and (
            word22 in stringlist or word23 in stringlist):
        await message.channel.send((chuibay[randNum]))
        randNum = random.randrange(0, len(chuibay))  # make the number random again
        return

    dongvien = [f"Đâu sẽ có đó, Bảnh tin em zai sẽ làm được, cố lên nhé em {username}", f"Cố lên {username}, em có "
                                                                                        f"thể làm được mà. Bảnh sẽ "
                                                                                        f"luôn bên cạnh hỗ trợ, "
                                                                                        f"giúp đỡ em zai bằng hết khả "
                                                                                        f"năng của mình. Cuộc đời của "
                                                                                        f"em zai thì hãy tự tin “dám "
                                                                                        f"nghĩ dám làm”. Sai thì sửa. "
                                                                                        f"Ngu quá thì vào tù cũng "
                                                                                        f"được", f"Trứng vịt còn lộn "
                                                                                                 f"huống chi là con "
                                                                                                 f"người. Có vấp ngã, "
                                                                                                 f"sai lầm mới có "
                                                                                                 f"thành công. Em zai {username} "
                                                                                                 f"hãy cứ vững tin và "
                                                                                                 f"bước tiếp thành "
                                                                                                 f"công sẽ đến.",
                f"Cuộc sống có lúc thăng trầm nhưng hãy luôn vững tin vào bản thân để đối diện với nó. Hãy biến chúng "
                f"thành những bài học quý giá giúp ta trưởng thành hơn. Hãy vui lên và nhìn về phía trước.", f"Buồn "
                                                                                                             f"hay áp "
                                                                                                             f"lực "
                                                                                                             f"quá "
                                                                                                             f"thì "
                                                                                                             f"khóc "
                                                                                                             f"cũng "
                                                                                                             f"được "
                                                                                                             f"em zai "
                                                                                                             f"à, "
                                                                                                             f"rồi "
                                                                                                             f"mọi "
                                                                                                             f"chuyện "
                                                                                                             f"sẽ qua "
                                                                                                             f"thôi",
                f"Động viên cái đéo gì ?? Địt mẹ mày tao nói một câu thôi, tập trung vào. Tắt mẹ discord đi dcmm",
                f"Ngô Bá Khá rất tiếc nhưng mà động viên cái đầu buồi", f"Đằng nào cũng thất bại thôi em zai "
                f"{username}", "Đời có bao nhiêu đâu mà buồn, hãy vững tin và quên đi tất cả. Cuộc sống có vô vàng "
                "những điều tốt đẹp đang chờ em zai ở phía trước, vui vẻ đón nhận em zai sẽ thấy thật hạnh phúc và bình "
                "yên.", f"Thành công sẽ không bao giờ từ chối những con người dám nghĩ dám làm. Ngô Bá Khá tin em {username} sẽ làm được tốt hơn thế.",
                "Sau cơn mưa bầu trời sẽ xuất hiện cầu vồng đấy. Nỗi buồn cũng vậy sẽ qua đi và hãy mạnh mẽ để chào đón tương lai phía trước.",
                f"Một ngày trôi qua là một ngày đến gần hơn với cái chết. Cho nên em zai {username} hãy tận dụng từng giây phút của mình để trải nghiệm và cải thiện bản thận nhé, Bảnh tin {username} sẽ thành công",
                f"{username} à, Bảnh tin là em zai sẽ đạt được mọi mục đích, cố lên nha đcm em", "Không có con đường nào trải đầy hoa hồng và không có thành công nào là không có thất bại. Đó chỉ là những thử thách giúp em zai mài dũa sự cứng rắn và giúp em zai tỏa sáng hơn mà thôi.",
                f"Làm một cốc nước lọc đi em zai, rồi hít một hơi thật sâu, em zai sẽ bình tĩnh và tập trung hơn đó, Bảnh biết em zai {username} làm được", "Mọi người có thể quay lưng với em zai, nhưng mà có một người em zai không được cho phép người đấy mất niềm tin. \n Đó chính là bản thân em zai, nếu mình còn không tin bản thân thì ai còn tin mình được nữa", f"Bảnh tin em zai {username} sẽ làm được điều vĩ đại trong tương lai \n Không tin Bảnh à? \n Hãy nhớ lại quá khứ khi em zai chưa sinh ra \n chính em zai là người vượt qua hàng trăm chục triệu thằng đầu buồi khác chứ k phải ai khác", f"Cố lên nha em zai {username}"]
    rand_dong_vien = random.randrange(0, len(dongvien))
    words2 = ['dong', 'vien', 'động', 'viên', 'buồn', 'banh', 'bảnh']
    word_1, word_2, word_3, word_4, word_5, word_6, word_7 = words2
    if (
            word_1 in stringlist or word_2 in stringlist or word_3 in stringlist or word_4 in stringlist or word_5 in stringlist) and (
            word_6 in stringlist or word_7 in stringlist):
        print(True)
        await message.channel.send((dongvien[rand_dong_vien]))
        rand_dong_vien = random.randrange(0, len(dongvien))  # make the number random again
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

    if message.content.startswith('bố thí bảnh') or message.content.startswith('bo thi banh'):
        channel = message.channel
        await channel.send(f'Gửi anh ít tiền  \N{Money with Wings} nha em zai {username}, anh đang cần gấp lắm')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '\N{Money with Wings}'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=34.0, check=check)
        except asyncio.TimeoutError:
            await channel.send(f'Dcmm {username}, có dăm ba đồng bạc lẻ em zai cũng tiếc, cũng tính toán lâu vcloz \N{Smirking Face}')
        else:
            await channel.send(f'Được vãi l em zai ơi, uy tín đấy {username} ')

client.run(TOKEN)
