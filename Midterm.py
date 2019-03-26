def CSUMBy():
  #call custom function to setMediaPath() to same folder level as this file.
  setMediaPathToCurrentDir()
  pic = makePicture(pickAFile()) ## use getPic() for testing, and otter? image? or logo, or both?
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      p = getPixel(pic, x, y)
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      if(r >= 170 and g >=170 and b >= 170): ##Bay Blue r:10 g:50 b:84 
      #range of color is 170 or greater
        setRed(p, 10)
        setGreen(p, 50)
        setBlue(p, 84)
      elif(r >= 85 and g >= 85 and b >= 85): ##Valley Green r:67 g:107 b:92
      #range of color is 85 to 169 
        setRed(p, 67)
        setGreen(p, 107)
        setBlue(p, 92)
      elif(r < 85 and g < 85 and b < 85):##Golden Sand r:147 g:127 b:85
      #range of color is strictly less than 85 
        setRed(p, 147)
        setGreen(p, 127)
        setBlue(p, 85)
      else: ## any pixels that are not in the ranges, set to Bay Blue
        setRed(p, 10)
        setGreen(p, 50)
        setBlue(p, 84)
  repaint(pic)
  
  writePictureTo(pic, getMediaPath() + "CSUMBy.png")
  

def vintageTV(): 
## use SpeedBoatSmaller.jpg for first image ##1080x720 image, slightly too long
## use GreenScreenSmaller.png for second image ## CRT make small enough to take in a 1080x720 image inside it.
## These are great for the demo using pyCopy not chromakey
  setMediaPathToCurrentDir()
  #hard coded image that we want to use for now.
  pic = makePicture(getMediaPath() + "SpeedBoatSmaller.jpg")
  #pic = makePicture(pickAFile())
  
  #Removed selection of TVFrame because that will be a fixed feature of our vintage function
  #tvFrame = makePicture(pickAFile())
  
  pic = addScanLines(pic)
  tvFrameX = 300 #300
  tvFrameY = 145 #145
  #distortImage(pic) ## this function needs to be made still
    
  pic = xferImageToCRT(pic)

  repaint(pic)
  
  writePictureTo(pic, getMediaPath() + "Vintage.png")
  
def addScanLines(pic):## introduces scanlines into the image
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic), 4): 
    # the 4 step draws a scan line every 4 lines horizontally
      darkenColor(getPixel(pic, x, y))
  return pic

def darkenColor(pixel):
  pixColor = getColor(pixel)
  new_pixColor = makeDarker(makeDarker(pixColor))
  #implemented makeDarker three times to be sure lines where very distinct.
  #better way to do this?
  setColor(pixel, new_pixColor)
  return pixel

#def distortImage(): ## introduces bending on edges of image

def pyCopy(source, target, targetX, targetY):
  sWidth = getWidth(source)
  sHeight = getHeight(source)
  tWidth = getWidth(target)
  tHeight = getHeight(target)
  
  for x in range(0, sWidth):
    for y in range(0, sHeight):
      oldPix = getPixel(source, x, y)
      newX = x + targetX
      newY = y + targetY
      #this will allow me to have some of the photos leave the frame a little bit without crashing
      if (newX < tWidth) and (newX >= 0) and (newY < tHeight) and (newY >= 0):
        newPix = getPixel(target, newX, newY)
        setColor(newPix, getColor(oldPix))
  return target

def xferImageToCRT(pic):
  #Requirements:
  #Image must be at least 945x720 in order to fill the greenscreen
  
  #hard coded the image that we will be using because this function is designed
  #around the features and sizes of the tvFrame that is listed below.
  tvFrame = makePicture(getMediaPath() + "GreenScreenCRTsmallerWMoreGreen.png")
  #upper left corner of small image (350,142)
  frameOriginX = 350
  frameOriginY = 142
  frameWidth = 945
  frameHeight = 725
  picWidth = getWidth(pic)
  picHeight = getHeight(pic)
  
  #create x and y offsets to locate the pic in the center of the tvFrame
  xOffset = frameOriginX + (frameWidth // 2) - (picWidth // 2)
  yOffset = frameOriginY + (frameHeight // 2) - (picHeight // 2)
  
  for x in range(0, frameOriginX + frameWidth):
    for y in range(0, frameOriginY + frameHeight):
      #moved bounds check out of if statement because it was too long
      inBoundsOfPic = (x < picWidth) and (x >= 0) and (y < picHeight) and (y >= 0)
      inBoundsOfTvFrame = (x + xOffset < getWidth(tvFrame)) and (x + xOffset >= 0) and \
                          (y + yOffset < getHeight(tvFrame)) and (y + yOffset >= 0)
      #this will check to make sure that the program is in bounds of pic and the tvFrame.
      if inBoundsOfPic and inBoundsOfTvFrame:
        pix = getPixel(pic, x, y)
        framePix = getPixel(tvFrame, x + xOffset, y + yOffset)
        r = getRed(framePix)
        g = getGreen(framePix)
        b = getBlue(framePix)
        newColor = getColor(pix)
        
        #create loose green color rule and use that to replace green in frame with the image
        if g > 200 and r < 150 and b < 150:
          setColor(framePix, newColor)
      
  return tvFrame
  
#to allow mediaPath to be correct an linux, macos and windows.
def setMediaPathToCurrentDir():
  fullPathToFile = os.path.abspath(__file__)
  if fullPathToFile.startswith('/'):
    setMediaPath(os.path.dirname(fullPathToFile))
  else:
    setMediaPath(os.path.dirname(fullPathToFile) + '\\')  