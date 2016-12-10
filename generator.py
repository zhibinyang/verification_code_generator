from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def rndChar():
    # ASCII Map: 48 ~ 57 Number 0~9, 65 ~ 90 Alphabet A~Z
    random_range = random.choice([(48,57),(65,90)])
    # Change it to char 
    return chr(random.randint(*random_range))

def rndColor():
    # RGB color range
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
    # RGB color range
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# Pic Size: 240 x 60:
width = 60 * 4
height = 60

# set a white pic first
image = Image.new('RGB', (width, height), (255, 255, 255))

# Set the Font and size
font = ImageFont.truetype('Arial.ttf', 36)

# Draw white background
draw = ImageDraw.Draw(image)

# Draw random dots on white background
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

fileName = ""
for t in range(4):
    rndStr = rndChar()
    # Draw the alphabet in random color
    draw.text((60 * t + 10, 10), rndStr, font=font, fill=rndColor2())
    # Append the alphabet to the filename
    fileName += rndStr

image = image.filter(ImageFilter.BLUR)

# Finally set the fileName same to the characters, for further Pattern Recognition purpose.
image.save(fileName+'.jpg', 'jpeg');

