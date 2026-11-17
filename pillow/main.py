from PIL import Image
import glob, os

with Image.open("vam.jpg") as im:
    im.rotate(90).show()

size = 128, 128

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        im.thumbnail(size)
        im.save(file + ".thumbnail", "JPEG")