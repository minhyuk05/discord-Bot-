import discord
import os
import asyncio

Client = discord.Client()

@Client.event
async def on_ready():
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드 봇 이름 : " +client.user.name)
    print("디스코드 봇 ID" +str(client.user.id))
    print("디스코드봇 버전 : " + str(discord.__version__))
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("이원찬은 이준민 사랑"))
    
@Client.event
async def on_message(message):
    content = message.content
    
    if content.startswith("신무경"):
        await message.channel.send("KYuNG")

    if content.startswith("돌하르방"):
        embed=discord.Embed(title="슈.슈ㅠ슉.슈바.슈슈수우ㅠ슈발러마", description="돌대가리쉨", color=0x00ff56)
        embed.set_author(name="제주도돌대가리", url="https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbe7jWW%2Fbtq8dtuOZjw%2FBdN7ox04RdGdNCk5vEiNkK%2Fimg.jpg")
        embed.set_thumbnail(url="https://cdn.maily.so/9ql2ko6t1a97vj078j2pr1p0ncb4")
        await message.channel.send(embed=embed)


access-token - os.environ["BOT_TOKEN"]
Client.run('access_token')

