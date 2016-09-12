#Sebastian Magana-Garcia
#9-09-16
#Proffesor Avner Biblarz
from PIL import Image
from PIL import ImageFilter
def blackandwhite(image):
	image = image.convert('1')
	image.show()
def emboss(image):
	image = image.filter(ImageFilter.EMBOSS)
	image.show()

theImages = []


imagePath = "C:\\Users\\Sebastian Magana\\Desktop\\project1\\Project1Images\\Project1Images\\"

pillowImage = Image.open(imagePath + "1.png")
# pillowImage = Image.open(imagePath + "1.png")
#pillowImage.show()


for myImage in range(1,10):
	print(imagePath + str(myImage) + ".png")
	theImages.append(Image.open(imagePath + str(myImage) + ".png"))


print("here is the list of 9 Pillow objects:")
print(theImages)

myCounter = 1
for aImage in theImages:
	if(myCounter%2 == 1):
		print("odd")
		blackandwhite(theImages[myCounter-1])
	else:
		print("even")
		emboss(theImages[myCounter])
	myCounter = myCounter + 1
