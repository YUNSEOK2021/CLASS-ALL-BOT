# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio
import os

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("MADE BY YUNSEOK TSET OK.\nTEST START OK.")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("경찰봇 도움이라 입력해보세요 !"))

@client.event
async def on_message(message):
    if message.content.startswith ("~청소"):
        if message.author.guild_permissions.administrator:
            amount = message.content[4:]
            await message.delete()
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n고위간부 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x14f7f2)
            embed.set_footer(text="Bot Made by. 윤석#2537", icon_url="https://cdn.discordapp.com/attachments/861573914128023552/878319144913739846/b1fe094dcf753017.png")
            await message.channel.send(embed=embed)
        
        else:
            await message.delete()
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))         

@client.event
async def on_message(message):
    if message.content == "디스코드 주소": # 메세지 감지
        await message.channel.send ("**경찰청 디스코드 주소는 https://discord.gg/Wj2dYPKq8P 입니다.**".format(message.author, message.author.mention))
        
    if message.content == "경찰봇 도움": # 메세지 감지
        await message.channel.send ("**```명령어 안내 (적어보세요) : 클래스 경찰청 안내 / 디스코드 주소 / !경찰공지 / ~청소 / 레오 정보좀 알려줘 / 스피드렉카 정보좀 알려줘(방문자전용) / 곽현&오구 정보좀 알려줘 / !레오 정보좀 알려줘```**".format(message.author, message.author.mention))   
    
    if message.content == "레오 정보좀 알려줘":
        ch = client.get_channel(870663553693143070)
        await ch.send ("레오는 치안총감으로, 현실 나이 42세이며 8월 7일부로 경찰청 치안총감에 올랐다. 이상 낙하산".format(message.author, message.author.mention))

    if message.content == "!레오 정보좀 알려줘":
        ch = client.get_channel(889438832657850368)
        await ch.send ("레오는 치안총감으로, 현실 나이 42세이며 8월 7일부로 경찰청 치안총감에 올랐다. 이상 낙하산이며 전화번호를 알고 싶으면 동부에게 개인디엠 하기 바란다.".format(message.author, message.author.mention))
        
    if message.content == "휴가복귀":
        ch = client.get_channel(881075252971573258)
        await ch.send ("클래스 경찰청 발신ㅣ휴가복귀 확인되었습니다.".format(message.author, message.author.mention))    
        
    if message.content == "스피드렉카 정보좀 알려줘":
        ch = client.get_channel(889438832657850368)
        await ch.send ("내가 왜? 적당히 해라 벌레들아".format(message.author, message.author.mention))   

    if message.content == "오구 정보좀 알려줘":
        ch = client.get_channel(889438832657850368)
        await ch.send ("오구는 닉변을 철새같이 존나 많이한다. 그래서 정보 알려주기 귀찮다".format(message.author, message.author.mention))
              
    if message.content == "클래스 경찰청 안내": # 메세지 감지
        embed = discord.Embed(title="클래스 경찰청 안내", description="", color=0x14f7f2)

        embed.add_field(name="클래스 경찰청 영구 디스코드 주소", value="https://discord.gg/Wj2dYPKq8P", inline=False)

        embed.add_field(name="경찰청 치안총감", value="    레오    ", inline=True)
        embed.add_field(name="경찰청 지원문의", value="경찰지원 확인 후 문의", inline=True)

        embed.set_footer(text="Bot Made by. 윤석#2537", icon_url="https://cdn.discordapp.com/attachments/861573914128023552/878319144913739846/b1fe094dcf753017.png")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/863305304434671646/863305345417740298/XCXCZ.png")
        await message.channel.send (embed=embed)

    if message.content.startswith ("~청소"):
        if message.author.guild_permissions.administrator:
            amount = message.content[4:]
            await message.delete()
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n고위간부 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x14f7f2)
            embed.set_footer(text="Bot Made by. 윤석#2537", icon_url="https://cdn.discordapp.com/attachments/861573914128023552/878319144913739846/b1fe094dcf753017.png")
            await message.channel.send(embed=embed)
        
        else:
            await message.delete()
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))                

    if message.content.startswith ("!경찰공지"):
        await message.delete()
        if message.author.guild_permissions.administrator:
            notice = message.content[6:]
            channel = client.get_channel(863005622399926293)
            embed = discord.Embed(title="**클래스 경찰청 공지사항**", description="공지사항 내용은 항상 숙지 해주시기 바랍니다\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice), color=0x14f7f2)
            embed.set_footer(text="Bot Made by. 윤석 # 2537 | 담당 경찰 간부 : {}".format(message.author), icon_url="https://cdn.discordapp.com/attachments/861573914128023552/878319144913739846/b1fe094dcf753017.png")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/863305304434671646/863305345417740298/XCXCZ.png")
            await channel.send ("<@&853323534947844156>", embed=embed)
            await message.author.send("**[ BOT 자동 알림 ]** | 클래스 경찰청에 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        else:
            await message.channel.send("{}, 당신은 경찰청 고위간부(명령권자)가 아닙니다".format(message.author.mention))
    
client.run('ODkwOTM4MjgxMDYyMTc4ODE3.YU3E7w.E2KfKoANawNFjfZ2uk9gE5X0TNM')
