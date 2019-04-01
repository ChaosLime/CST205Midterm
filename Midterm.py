## Midterm Project -- CST 205
## Group Members:
## Mitchell Saunders
## Nicholas Saunders

### CSUMBy function starts here ###

def CSUMBy(): ##Call function to get CSUMBized photo
  #call custom function to setMediaPath() to same folder level as this file, makes sure it works on Windows, macos, and linux platforms.
  setMediaPathToCurrentDir()
  
  pic = makePicture(getMediaPath() + "Playful_Otter.jpg")
  #pic = makePicture(pickAFile())
  logo = makePicture(getMediaPath() + "csumb-logo.png")
  artified= artify(pic)
  ##adding text
  textStyle = makeStyle(serif, bold, 100)
  addTextWithStyle(artified, 25, 100, "Go Otters!", textStyle, white)
  ##Adds Logo
  show(pyCopyIgnoreColor(logo,artified,getWidth(pic)-860,getHeight(pic)-250,makeColor(32,255,20)))
  
  #writePictureTo(pic, getMediaPath() + "CSUMBy.png")
  
def artify(pic):
  pixels = getPixels(pic)
  for pixel in pixels:
    setRed(pixel, changeColor(pixel.getRed(),"red"))
    setGreen(pixel, changeColor(pixel.getGreen(),"green"))
    setBlue(pixel, changeColor(pixel.getBlue(),"blue"))
  return(pic)  
    	
def changeColor(colorValue,type): 
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

def pyCopyIgnoreColor(source, target, targetX, targetY, colorToIgnore):
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
        if getColor(oldPix) != colorToIgnore:
          newPix = getPixel(target, newX, newY)
          setColor(newPix, getColor(oldPix))
  return target    

### Retro TV function starts here ###

def vintageTV(): 
  setMediaPathToCurrentDir()
  #pic = makePicture(getMediaPath() + "FullSpeedBoat.jpg")
  pic = makePicture(pickAFile())
  
  pic = changeContrastAndBrightness(pic, 1.5, 20)
  pic = rgbShift(pic, 3)
  #choose from the following two functions which one more looks like a CRT
  pic = addScanLines(pic, 4)
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
def addScanLines(pic, everyXrows):
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic), everyXrows):      
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
  
def rgbShift(pic, shiftAmount):## cause green to move to the right, and blue to the left
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
  new_pixColor = makeDarker(makeDarker(makeDarker(makeDarker(pixColor))))
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


