import MLX90614
from machine import Pin,I2C
import time
import ssd1306
from piclib import *
# This code will show you how to make a Infra Red Thermometer using the MLX90614 sensor.


i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)
ir=MLX90614.MLX90614(i2c)
lcd=ssd1306.SSD1306_I2C(128,64,i2c)

#Display a picture 72*64 
def DisplayPicture(x,y,picture):
  for line in range(0,64):
    for bytes in range(0,9):
      for bits in range(0,8):
        if picture[9*line+bytes]&0x80>>bits:
          lcd.pixel(x+bytes*8+bits,y+line,1)
        else:
          lcd.pixel(x+bytes*8+bits,y+line,0)
  return

#Display a character 16*24 
def DisplayCharacter16X24(x,y,character):
  for line in range(0,24):
    for bytes in range(0,2):
      for bits in range(0,8):
        if character[line*2+bytes]&0x80>>bits:
          lcd.pixel(x+bytes*8+bits,y+line,1)
        else:
          lcd.pixel(x+bytes*8+bits,y+line,0)
  return

#---------------------run here------------------------------------  
#display logo
DisplayPicture(28,0,picture) 
lcd.show()
time.sleep(1)
lcd.fill(0)


#display O:123.4C
#        A:123.4C 
DisplayCharacter16X24(0,0,charArray[10]) #O
DisplayCharacter16X24(16*1,0,charArray[12]) #:
DisplayCharacter16X24(16*7,0,charArray[13]) #C

DisplayCharacter16X24(0,24,charArray[11]) #A
DisplayCharacter16X24(16*1,24,charArray[12]) #:
DisplayCharacter16X24(16*7,24,charArray[13]) #C
lcd.show()


while True:
  time.sleep(0.2)
  Object = ir.getObjCelsius() #  *C
  Ambient = ir.getEnvCelsius() # *C
  #Object = ir.getObjFahrenheit() # *F
  #Ambient = ir.getEnvFahrenheit() # *F
  #print("Object  %s *C"% Object)
  #print("Ambient %s *C"% Ambient)
  #print()
  ObjectInt = int(Object*10)
  AmbientInt = int(Ambient*10)
  if ObjectInt < 0:
    ObjectInt = abs(ObjectInt)
    DisplayCharacter16X24(16*2,0,charArray[15])# -
    temp1 = (ObjectInt%1000)//100
    if(temp1 == 0):
      DisplayCharacter16X24(16*3,0,charArray[16]) # space
    else:
      DisplayCharacter16X24(16*3,0,charArray[temp1])
    DisplayCharacter16X24(16*4,0,charArray[(ObjectInt%100)//10])
    DisplayCharacter16X24(16*5,0,charArray[14]) # .
    DisplayCharacter16X24(16*6,0,charArray[ObjectInt%10]) 
   
  else:
    temp1 = ObjectInt//1000
    temp2 = (ObjectInt%1000)//100
    if temp1 == 0:
      DisplayCharacter16X24(16*2,0,charArray[16]) # space
    else:
      DisplayCharacter16X24(16*2,0,charArray[temp1])
    if temp1 == 0 and temp2 == 0:
      DisplayCharacter16X24(16*3,0,charArray[16]) # space
    else:
      DisplayCharacter16X24(16*3,0,charArray[temp2])
    DisplayCharacter16X24(16*4,0,charArray[(ObjectInt%100)//10])
    DisplayCharacter16X24(16*5,0,charArray[14]) # .
    DisplayCharacter16X24(16*6,0,charArray[ObjectInt%10]) 
 
  if AmbientInt < 0:
    ObjectInt = abs(AmbientInt)
    DisplayCharacter16X24(16*2,24,charArray[15])# -
    temp1 = (AmbientInt%1000)//100
    if temp1 == 0:
      DisplayCharacter16X24(16*3,24,charArray[16]) # space
    else:
      DisplayCharacter16X24(16*3,24,charArray[temp1])
    DisplayCharacter16X24(16*4,24,charArray[(AmbientInt%100)//10])
    DisplayCharacter16X24(16*5,24,charArray[14]) # .
    DisplayCharacter16X24(16*6,24,charArray[AmbientInt%10]) 
   
  else:
    temp1 = AmbientInt//1000
    temp2 = (AmbientInt%1000)//100
    if temp1 == 0:
      DisplayCharacter16X24(16*2,24,charArray[16]) # space
    else:
      DisplayCharacter16X24(16*2,24,charArray[temp1])
    if temp1 == 0 and temp2 == 0:
      DisplayCharacter16X24(16*3,24,charArray[16]) # space
    else:
      DisplayCharacter16X24(16*3,24,charArray[temp2])
    DisplayCharacter16X24(16*4,24,charArray[(AmbientInt%100)//10])
    DisplayCharacter16X24(16*5,24,charArray[14]) # .
    DisplayCharacter16X24(16*6,24,charArray[AmbientInt%10])  
  lcd.show()



