#makes a function that takes the list and the settings and makes it an image
def screenprint(pixels, adjust):
  string = ""
  for a1 in pixels:
    for b1 in a1:
      temp = ""
      r = b1[0]
      g = b1[1]
      b = b1[2]
      if r + g + b < adjust.blk_wht_splt:
        temp = "โฌโ"
      else:
        temp = "โฌโ"
      if r > g/adjust.redaddgreen + b/adjust.redaddblue:
        temp = "๐ฅโ"
      elif g > r/adjust.greenaddred + b/adjust.greenaddblue:
        temp = "๐ฉโ"
      elif b > g/adjust.blueaddgreen + r/adjust.blueaddred:
        temp = "๐ฆโ"
      if adjust.yellow(r, g, b):
        temp = "๐จโ"
      if adjust.orange(r, g, b):
        temp = "๐งโ"
      if r + g + b < adjust.darklimit:
        temp = "โฌโ"
      elif r + g + b > adjust.lightlimit:
        temp = "โฌโ"
      string += temp 
    print(string)
    string = ""


#import stuff
def main():

  #ask which file and open the data as a list from it
  textfile = open('engine/ImageProcessing/image.txt', 'r')
  pixels = []
  pixels.append([])
  line = 0
  line2 = 0
  for a1 in textfile.readlines():
    a3 = a1.rstrip('\n')
    if a3 == "line":
      line+= 1
      pixels.append([])
      line2 = 0
    else:
      pixels[line].append([])
      linetxt = ""
      for a2 in a3:
        if a2 == " ":
          pixels[line][line2].append(int(linetxt))
          linetxt = ""
        else:
          linetxt += a2
      pixels[line][line2].append(int(linetxt))
      linetxt = ""
      line2 += 1


  #all of the adjustable settings
  class adjust:
    blk_wht_splt = 382.5
    redaddgreen = 1
    redaddblue = 1
    greenaddred = 1.5
    greenaddblue = 1.2
    blueaddred = 1.4
    blueaddgreen = 1.4

    darklimit = 70
    lightlimit = 680

    def yellow(r, g, b):
      if r+g-b>300: return True
    def orange(r, g, b):
      if r+g-b>300 and g<210: return True

  #runs the function
  screenprint(pixels, adjust)