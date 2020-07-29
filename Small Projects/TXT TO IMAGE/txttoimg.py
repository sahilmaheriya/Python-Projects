from PIL import Image, ImageDraw

txt = input("Enter your String: ")

img = Image.new('RGB',(400,50),color=(73,12,137))

d = ImageDraw.Draw(img)
d.text((10,10),txt,fill=(300,300,300))

img.save("txt2img.png")
print("Close this window and check it was saved as txt2img.png file")
