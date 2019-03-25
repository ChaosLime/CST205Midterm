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

def vintageTV(): 
## use SpeedBoatSmaller.jpg
## it is the correct resolution to fit into the TV frame
  pic = makePicture(pickAFile()) 
  scanLines(pic)
  #distortImage(pic) ## this function needs to be made still
  chromakey(pic)
  repaint(pic)
  
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

def chromakey(pic): 
  ## for use of Vintage TV to be put into the greenScreen CRT
  crtImage = pic
  tvFrame = makePicture(pickAFile())
  ##GreemScreenCRT green area is around 900x700 in size
  ##use provided image of TV screen 
  pixelsFrame = getPixels(tvFrame)
  pixelsImage = getPixels(crtImage)
  for pixel in pixelsFrame: 
    r = pixel.getRed()
    b = pixel.getBlue()
    g = pixel.getGreen()
    redBlueAvg = (r+b)/2.0
    if (g > (redBlueAvg)*2.0):
      p = getPixel(crtImage, 10 ,10)
      ## issues with the size of the crtImage on the TvFrame
      ## attempting debugging with green.png provided.
      ## perhaps image is going out of bounds?
      setColor(pixel, getColor(p))
  return tvFrame
  
  
  