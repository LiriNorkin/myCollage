from PIL import Image, ImageDraw
import random

class myCollage:
    def __init__(self, paths):
        self.paths = paths

    def changeSize(img, w, h):
        img = img.resize((int(w),int(h)))

    def makeCollage(self):
        width, height = Image.open(self.paths[0]).size
        background = Image.new('RGB', (width//2,height), color='pink')
        background.save("background.jpg")

        for i in range(0,50):
            img = Image.open(self.paths[i%len(self.paths)])
            smaller = img.resize((int(width/5), int(height/5)))
            rand_w = random.randint(0,width)
            rand_h = random.randint(0,int(3*height/4))
            background.paste(smaller, (rand_h, rand_w))
           # smaller.show()
          #  background.show()
        #  myimg =
        #  myimg.save("background.jpg")
        background.save("brand_new_collage.jpg")
        background.show()
