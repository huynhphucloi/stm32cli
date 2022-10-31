import serial
import sys

class UART:

  def __init__(self, ch, baud):
    self.ser = serial.Serial()
    self.ser.port = ch
    self.ser.baudrate = baud
  
  def open(self):
    try:
      self.ser.open()
      print("UART open success!")
    except:
      print("Check your Port!")
      sys.exit()
    
  def available(self):
    return self.ser.in_waiting()
  
  def read(self):
    return self.ser.read(size=1)
  
  def write(self, data):
    ret =  self.ser.write(data)
    self.ser.flush()
    print(data)
    return ret
  
  def close(self):
    return self.ser.close()
  
  
  
    
  
  