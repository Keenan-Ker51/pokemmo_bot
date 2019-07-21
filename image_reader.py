# all image proecessing will happen here.

from PIL import Image, ImageGrab
from pytesseract import image_to_string
import numpy as np
from numpy import matrix


#print(image_to_string(Image.open('just_name.png')))

def get_text(img):
    print(img)
    print(image_to_string(Image.open(img)).split())
    print("\n")
    #return image_to_string(Image.open(img))

def get_poke_name():
    im = ImageGrab.grab(bbox=(287,138,575,169))
    im.save('just_name.png')
    #get_text(im)
    #im = ImageGrab.grab()
    #im.show()

def outside_battle(state):
    im = ImageGrab.grab(bbox=(58,536,266,613))
    im.save('outside_{}.png'.format(state))

def get_eff():
    first = ImageGrab.grab(bbox=(304,704,407,719))
    first.save('moves/frst.png')
    scnd = ImageGrab.grab(bbox=(304,759,407,773))
    scnd.save('moves/scnd.png')
    thrd = ImageGrab.grab(bbox=(517,704,620,719))
    thrd.save('moves/thrd.png')
    fourth = ImageGrab.grab(bbox=(517,759,620,773))
    fourth.save('moves/fourth.png')



# sourced from https://gist.github.com/olooney/1246268
def average_image_color(filename):
	i = Image.open(filename)
	h = i.histogram()

	# split into red, green, blue
	r = h[0:256]
	g = h[256:256*2]
	b = h[256*2: 256*3]

	# perform the weighted average of each channel:
	# the *index* is the channel value, and the *value* is its weight
	return (
		sum( i*w for i, w in enumerate(r) ) / sum(r),
		sum( i*w for i, w in enumerate(g) ) / sum(g),
		sum( i*w for i, w in enumerate(b) ) / sum(b)
	)

def return_avgs():
    l = matrix(average_image_color('outside_start.png'))
    d = matrix(average_image_color('outside_now.png'))
    return np.mean(l-d)
#get_poke_name()
#outside_battle()
#get_text('Tentacruel.png')

#get_eff()
first = ImageGrab.grab(bbox=(304,704,407,719))
first.save('moves/frst.png')
print(np.mean( matrix((average_image_color("moves/frst.png")))))
print(average_image_color('moves/frst.png'))
# print(np.mean( matrix((average_image_color('moves/scnd.png')))))

print(np.mean( matrix((average_image_color('moves/thrd.png')))))
print(average_image_color('moves/thrd.png'))
# print(np.mean( matrix((average_image_color('moves/fourth.png')))))
