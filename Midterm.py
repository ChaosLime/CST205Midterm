## Midterm Project -- CST 205
## Group Members:
## Mitchell Saunders
## Nicholas Saunders

def CSUMBy(): ##Call function to get CSUMBized photo
  #call custom function to setMediaPath() to same folder level as this file.
  setMediaPathToCurrentDir()
  pic = makePicture(pickAFile())
  artified= artify(pic)
  ##adding text
  textStyle = makeStyle(serif, bold, 50)
  addTextWithStyle(artified, 50, 100, "Go Otters!", textStyle, white)
  textStyle = makeStyle(serif, bold, 50)
  addTextWithStyle(artified, getWidth(artified)-300, getHeight(artified)-50, "CSUMB", textStyle, white)
  
  show(artified)  
  #writePictureTo(pic, getMediaPath() + "CSUMBy.png")
  
def artify(pic):
  pixels = getPixels(pic)
  for pixel in pixels:
    setRed(pixel, changeColor(pixel.getRed(),"red"))
    setGreen(pixel, changeColor(pixel.getGreen(),"green"))
    setBlue(pixel, changeColor(pixel.getBlue(),"blue"))
  return(pic)  
    	
def changeColor(colorValue,type): 
## issues with output colors, have 3 colors that are close to colors wanted, but still gets painted.
##Bay Blue r:10 g:50 b:84
##Valley Green r:67 g:107 b:92
##Golden Sand r:147 g:127 b:85
  if(type == "red"):#Red value check
    if (colorValue >= 0) and (colorValue <= 85):##Bay Blue
      colorValue = 10
    if (colorValue > 85) and (colorValue <= 170):##Valley Green
      colorValue = 67
    if (colorValue > 170) and (colorValue <= 255):##Golden Sand
      colorValue = 147
    return(colorValue)
    
  if(type == "green"):#Green value check
    if (colorValue >= 0) and (colorValue <= 85):##Bay Blue
      colorValue = 50
    if (colorValue > 85) and (colorValue <= 170):##Valley Green
      colorValue = 107
    if (colorValue > 170) and (colorValue <= 255):##Golden Sand
      colorValue = 127
    return(colorValue)
    
  if(type == "blue"):#Blue value check
    if (colorValue >= 0) and (colorValue <= 85):##Bay Blue
      colorValue = 84
    if (colorValue > 85) and (colorValue <= 170):##Valley Green
      colorValue = 92
    if (colorValue > 170) and (colorValue <= 255):##Golden Sand
      colorValue = 85
    return(colorValue)
  else:
    return 0


###Retro TV function starts here

def vintageTV(): 
  setMediaPathToCurrentDir()
  #pic = makePicture(getMediaPath() + "FullSpeedBoat.jpg")
  pic = makePicture(pickAFile())
  
  pic = changeContrastAndBrightness(pic, 1.5, 20)
  pic = rgbShift(pic)
  #choose from the following two functions which one more looks like a CRT
  pic = addScanLines(pic) #changed to put a scanline every other row
  #pic = splitRGB(pic)

  repaint(pic)
  
  writePictureTo(pic, getMediaPath() + "Vintage.png")

def changeContrastAndBrightness(pic, contrastAmount, brightnessAmount):
  #if desired contrast and brightness are desired to be left alone...
  #contrastAmount = 1 and brightnessAmount = 0
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      p = getPixel(pic, x, y)
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      
      nr = contrastAmount * (r - 128) + 128 + brightnessAmount
      ng = contrastAmount * (g - 128) + 128 + brightnessAmount
      nb = contrastAmount * (b - 128) + 128 + brightnessAmount
      
      if nr > 255:
        nr = 255
      elif nr < 0:
        nr = 0
      if ng > 255:
        ng = 255
      elif ng < 0:
        ng = 0
      if nb > 255:
        nb = 255
      elif nb < 0:
        nb = 0
      
      newColor = makeColor(nr, ng, nb)
      setColor(p, newColor)
  return pic

#use this or splitRGB  
def addScanLines(pic):
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic), 2):      
      #the 2 step draws a scan line every 2 lines horizontally
      darkenColor(getPixel(pic, x, y))
  return pic

#use this or addScanlines  
def splitRGB(pic):## CRT-ify image
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)): 
      p = getPixel(pic, x, y)
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      if y % 3 == 0:
        setColor(p, makeColor(r, 0, 0))
      elif (y + 1) % 3 == 0:
        setColor(p, makeColor(0 ,g, 0))
      elif (y + 2) % 3 == 0:
        setColor(p, makeColor(0, 0, b))
  return pic
  
def rgbShift(pic):## cause green to move to the right, and blue to the left
  shiftAmount = 2
  canvas = makeEmptyPicture(getWidth(pic), getHeight(pic))
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)): 
      destPix = getPixel(canvas, x, y)
      cp = getPixel(pic, x, y)
      r = getRed(cp)
      
      if x - shiftAmount >= 0:
        lp = getPixel(pic, x - shiftAmount, y)
        b = getBlue(lp)
      else:
        b = getBlue(cp)
      
      if x + shiftAmount < getWidth(pic):
        rp = getPixel(pic, x + shiftAmount, y)
        g = getGreen(rp)
      else:
        g = getGreen(cp)

      setColor(destPix, makeColor(r, g, b))
  return canvas

def darkenColor(pixel):
  pixColor = getColor(pixel)
  new_pixColor = makeDarker(makeDarker(makeDarker(pixColor)))
  #implemented makeDarker three times to be sure lines where very distinct.
  #better way to do this?
  setColor(pixel, new_pixColor)
  return pixel
  
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

#to allow mediaPath to be correct an linux, macos and windows.
def setMediaPathToCurrentDir():
  fullPathToFile = os.path.abspath(__file__)
  if fullPathToFile.startswith('/'):
    setMediaPath(os.path.dirname(fullPathToFile))
  else:
    setMediaPath(os.path.dirname(fullPathToFile) + '\\')




#The section below is old code that can be removed before submitting
####=============================================
####=============================================
####=============================================
####=============================================

#abandoned - Remove before submitting
def splitImageIntoRGB(pic):
  canvas = makeEmptyPicture(getWidth(pic), getHeight(pic)*3, black)
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic) - 3, 3):
      op1 = getPixel(pic, x, y + 0)
      op2 = getPixel(pic, x, y + 1)
      op3 = getPixel(pic, x, y + 2)
      np1 = getPixel(canvas, x, (y*3) + 0)
      np2 = getPixel(canvas, x, (y*3) + 1)
      np3 = getPixel(canvas, x, (y*3) + 2)
      
      color1 = getColor(op1)
      color2 = getColor(op2)
      color3 = getColor(op3)
      
      setColor(np1, color1)
      setColor(np2, color2)
      setColor(np3, color3) 
      
      # the 4 step draws a scan line every 4 lines horizontally
      #darkenColor(getPixel(pic, x, y))
  return canvas

#abandoned - Remove before submitting
def betterSplitImageIntoRGB(pic):
  canvas = makeEmptyPicture(getWidth(pic), getHeight(pic)*3, black)
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic) - 3):
      op1 = getPixel(pic, x, y + 0)
      np1 = getPixel(canvas, x, (y*3) + 0)
      
      color1 = getColor(op1)
      color2 = getColor(op2)
      color3 = getColor(op3)
      
      setColor(np1, color1)
      setColor(np2, color2)
      setColor(np3, color3) 
      
      # the 4 step draws a scan line every 4 lines horizontally
      #darkenColor(getPixel(pic, x, y))
  return canvas

#abandoned - remove before submitting
def betterSplitRGB(pic):
  canvas = makeEmptyPicture(getWidth(pic)*3, getHeight(pic))
  for x in range(0, getWidth(pic)-1):
    for y in range(0, getHeight(pic)):
      p = getPixel(pic, x, y)
      newPixR = getPixel(canvas, (x*3) + 0, y)
      newPixG = getPixel(canvas, (x*3) + 1, y)
      newPixB = getPixel(canvas, (x*3) + 2, y)
      rCol = makeColor(getRed(p), 0, 0)
      gCol = makeColor(0, getGreen(p), 0)
      bCol = makeColor(0, 0, getBlue(p))
      
      setColor(newPixR, rCol)
      setColor(newPixG, gCol)
      setColor(newPixB, bCol) 
      
      # the 4 step draws a scan line every 4 lines horizontally
      #darkenColor(getPixel(pic, x, y))
  return canvas
  
#abandoned - remove before submitting
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