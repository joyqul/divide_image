savedFileFormat = 'jpeg'

class Image:
    def __init__(self, filename, dest=None, columns=1, rows=1, ext='jpg'):
        self.filename = filename
        self.dest = dest or self.get_dest()
        self.columns = columns
        self.rows = rows
        self.ext = ext
        self.basename = self.get_basename()

    def get_dest(self):
        import os
        dest = os.path.dirname(self.filename)
        return dest

    def get_basename(self):
        import os
        basename = os.path.splitext(os.path.basename(self.filename))[0]
        return basename

    def get_size_after_slice(self, originSize, pieces):
        newSize = originSize//pieces
        redundant = originSize-newSize*pieces
        return newSize, redundant

    def get_saved_name(self, i, j):
        filename = 'slice_%s_{:02d}_{:02d}.%s'.format(i,j) %(self.basename, self.ext)
        import os
        return os.path.join(self.dest, filename)
        

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
                newFilename = self.get_saved_name(i, j)
                cropedImage.save(newFilename, savedFileFormat)


def do_slice(options):
    import os
    fromDir = options.folder
    toDir = options.dest or fromDir
    row = options.row
    col = options.col
    targets = os.listdir(fromDir)
    for filename in targets:
        fullFilename = os.path.join(fromDir, filename)
        print 'slice %s' %( fullFilename )
        tmp = Image(fullFilename, rows=row, columns=col, dest=toDir)
        tmp.slice()
    

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Divide image into pieces')
    parser.add_argument('folder', type=str,\
                        help='Divide images in folder into pieces')
    parser.add_argument('--row', type=int, default=1,\
                        help='Divide images into given rows')
    parser.add_argument('--col', type=int, default=1,\
                        help='Divide images into given columns')
    parser.add_argument('--dest', type=str, \
                        help='Save destination of divided images, default will save in same folder')
    options = parser.parse_args()
    do_slice(options)
