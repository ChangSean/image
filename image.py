from PIL import Image
import os



for file in os.listdir('original'):
	if file.endswith('.png'):
		image_file = Image.open(os.path.join('original',file)) # open color image
		image_file = image_file.convert('L') # convert image to balck and white
		image_file.save(os.path.join('new',file[:-4] + '_grey.png'))
