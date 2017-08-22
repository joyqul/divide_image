saveDirectory = 'Desktop/'
fileName = 'Desktop/tmpfile.jpg'
savedFileFormat = 'jpeg'

class Image:
    def __init__(self, filename, columns=1, rows=1, ext='jpg'):
        self.filename = filename
        self.columns = columns
        self.rows = rows
        self.ext = ext
        self.save_basename()

    def save_basename(self):
        import os
        self.basename = os.path.splitext(os.path.basename(filename))[0]

    def get_size_after_slice(self, originSize, pieces):
        newSize = originSize//pieces
        redundant = originSize-newSize*pieces
        return newSize, redundant

    def slice(self):
        from PIL import Image
        imageData = Image.open(self.filename)
        imageWidth, imageHeight = imageData.size
    
        newWidth, widthRedundant = self.get_size_after_slice(imageWidth, self.columns)
        newHeight, heightRedundant = self.get_size_after_slice(imageHeight, self.rows)

        #TODO: figure out how to deal if has redundant
        if widthRedundant:
            print 'Has redundant %s in width' %( widthRedundant )
        if heightRedundant:
            print 'Has redundant %s in height' %( heightRedundant )
    
        for i in xrange(0, self.columns):
            for j in xrange(0, self.rows):
                startX = newWidth*i
                startY = newHeight*j
                endX = startX+newWidth-1
                endY = startY+newHeight-1
                area = (startX, startY, endX, endY)
                cropedImage = imageData.crop(area)
                newFilename = '%s_%s_%s.%s' %(self.basename, i, j, self.ext)
                cropedImage.save(newFilename, savedFileFormat)

testImages = ['tmpfile.jpg', 'tmpfile2.jpg']
for filename in testImages:
    tmp = Image(filename, rows=2)
    tmp.slice()
