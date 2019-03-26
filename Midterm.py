
def CSUMBy():
  pic = makePicture(pickAFile()) ## use getPic() for testing, and otter? image? or logo, or both?
  for x in range(0,getWidth(pic)):
    for y in range(0,getHeight(pic)):
      p = getPixel(pic,x,y)
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      if(r >= 170 and g >=170 and b >= 170): ##Bay Blue r:10 g:50 b:84 
      #range of color is strictly 170 to 255
        setRed(p,10)
        setGreen(p,50)
        setBlue(p,84)
      elif(r >= 85 and g > 85 and b > 85): ##Valley Green r:67 g:107 b:92
      #range of color is strictly 85 to 170 
        setRed(p,67)
        setGreen(p,107)
        setBlue(p,92)
      elif(r <85 and g<85 and b<85):##Golden Sand r:147 g:127 b:85
      #range of color is strictly less than 85 
        setRed(p,147)
        setGreen(p,127)
        setBlue(p,85)
      else: ## any pixels that are not in the ranges, set to Bay Blue
        setRed(p,10)
        setGreen(p,50)
        setBlue(p,84)
  repaint(pic)
  #writePictureTo(pic,"/home/nick/Workspaces/GitProjects/CST205 Midterm/CSUMBy.jpg")
  

def vintageTV(): 
## use SpeedBoatSmaller.jpg for first image ##1080x720 image, slightly too long
## use GreenScreenSmaller.png for second image ## CRT make small enough to take in a 1080x720 image inside it.
## These are great for the demo using pyCopy not chromakey
  pic = makePicture(pickAFile())
  tvFrame = makePicture(pickAFile())
  scanLines(pic)
  tvFrameX = 300 #300
  tvFrameY = 145 #145
  #distortImage(pic) ## this function needs to be made still
  #show(chromakey(pic,tvFrame))
  
  demo = pyCopy(pic,tvFrame,tvFrameX,tvFrameY)
  show(demo)
  #writePictureTo(demo,"/home/nick/Workspaces/GitProjects/CST205 Midterm/Vintage.jpg")
  
def scanLines(pic):## introduces scanlines into the image
  for x in range(0,getWidth(pic)):
    for y in range(0,getHeight(pic),4): 
    # the 4 step draws a scan line every 4 lines horizontally
      darkenColor(getPixel(pic,x,y))
  return pic

def darkenColor(pixel):
  pixColor = getColor(pixel)
  new_pixColor = makeDarker(makeDarker(makeDarker(pixColor)))
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

def chromakey(pic,tvFrame): 
  ## for use of Vintage TV to be put into the greenScreen CRT
  crtImage = pic
  tvFrame = tvFrame
  ##GreemScreenCRT green area is around 900x700 in size
  ##use provided image of TV screen 
  pixelsFrame = getPixels(tvFrame)
  pixelsImage = getPixels(crtImage)
  for pixel in pixelsImage: 
    r = pixel.getRed()
    b = pixel.getBlue()
    g = pixel.getGreen()
    redBlueAvg = (r+b)/2.0
    if (g > (redBlueAvg)*2.5):
      p = getPixel(tvFrame, 0 ,0)
      setColor(p, getColor(p))
  return tvFrame
  
  
  