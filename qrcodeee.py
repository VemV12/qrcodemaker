import discord
from discord.ext import commands
import qrcode
client = commands.Bot(command_prefix="$")


@client.command()
async def linktoqr(ctx,link):
    await ctx.send(f"Converting {link} To QRcode")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=100,
        border=2,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('hell0p.png')
    await ctx.send(f"Here is the QRcode of {link}",file=discord.File('hell0p.png'))

client.run("token here")