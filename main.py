saveDirectory = 'Desktop/'
fileName = 'Desktop/tmpfile.jpg'
savedFileFormat = 'jpeg'
from PIL import Image


def get_size_after_slice(originSize, pieces):
	newSize = originSize//pieces
	redundant = originSize-newSize*pieces
	return newSize, redundant

def slice(columns=1, rows=1):
	imageData = Image.open(fileName)
	imageWidth, imageHeight = imageData.size

	newWidth, widthRedundant = get_size_after_slice(imageWidth, columns)
	newHeight, heightRedundant = get_size_after_slice(imageHeight, rows)
	#TODO: figure out how to deal if has redundant

	for i in xrange(0, columns):
		for j in xrange(0, rows):
			startX = newWidth*i
			startY = newHeight*j
			endX = startX+newWidth-1
			endY = startY+newHeight-1
			area = (startX, startY, endX, endY)
			cropedImage = imageData.crop(area)
			newFilename = 'slice_%s_%s.jpg' %(i, j)
			cropedImage.save(newFilename, savedFileFormat)

slice(rows=2)
